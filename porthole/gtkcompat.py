"""
Compatibility layer to let the codebase run with either classic PyGTK (GTK2)
or PyGObject/GTK3 while keeping the original ``import gtk`` style imports.

Strategy
--------
* Try PyGTK first (keeps GTK2 compatibility on Gentoo installs that still have it).
* Fallback to PyGObject with ``gi.pygtkcompat`` to provide ``gtk``/``gobject``/``pango``
  module shims.  We also provide a small ``gtk.glade.XML`` wrapper that loads
  GtkBuilder ``.ui`` files generated from the legacy ``.glade`` definitions.
"""

import os
import sys
import subprocess
import tempfile
import types
try:
    from shutil import which
except ImportError:  # Python 2 compatibility
    from distutils.spawn import find_executable as which
import shutil

USE_PYGTK = False
USE_GI = False


def _resolve_glade_file(gladefile):
    """
    When running under GTK3 we need GtkBuilder .ui files.
    Prefer a sibling .ui or a copy in glade3/, otherwise try to
    convert on the fly with gtk-builder-convert if present.
    """
    path = os.path.abspath(gladefile)
    base, ext = os.path.splitext(path)
    candidates = []
    if ext == ".glade":
        candidates.append(base + ".ui")  # same directory
        candidates.append(os.path.join(os.path.dirname(os.path.dirname(path)),
                                       "glade3", os.path.basename(base) + ".ui"))
    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate

    converter = which("gtk-builder-convert")
    if converter and os.path.exists(path):
        tmp_ui = os.path.join(tempfile.gettempdir(), "%s.ui" % os.path.basename(base))
        try:
            subprocess.run([sys.executable, converter, path, tmp_ui],
                           check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return tmp_ui
        except Exception:
            pass
    # fall back to original path; may still work on systems with libglade
    return path


def _setup_pygtk():
    import pygtk

    pygtk.require("2.0")
    import gtk  # noqa: F401
    import gobject  # noqa: F401
    import pango  # noqa: F401
    globals().update({"gtk": gtk, "gobject": gobject, "pango": pango})
    globals().update({"USE_PYGTK": True})


def _setup_gi():
    import gi

    gi.require_version("Gtk", "3.0")
    gi.require_version("Gdk", "3.0")
    gi.require_version("Pango", "1.0")
    gi.require_version("GObject", "2.0")

    # Expose gtk/gobject style modules
    gi.pygtkcompat.enable()
    gi.pygtkcompat.enable_gtk(version="3.0")
    gi.pygtkcompat.enable_gdk(version="3.0")
    try:
        gi.pygtkcompat.enable_vte()
    except Exception:
        # vte is optional; ignore if unavailable
        pass

    import gtk  # provided by pygtkcompat
    import gobject  # provided by pygtkcompat
    import pango  # provided by pygtkcompat
    from gi.repository import Gtk

    # Provide stub pygtk module so existing "import pygtk" keeps working
    pygtk_stub = types.SimpleNamespace(require=lambda *args, **kwargs: None)
    sys.modules.setdefault("pygtk", pygtk_stub)

    class _GladeXML(object):
        def __init__(self, gladefile, root=None, domain=None):
            self._gladefile = _resolve_glade_file(gladefile)
            self.builder = Gtk.Builder()
            if domain:
                self.builder.set_translation_domain(domain)
            self.builder.add_from_file(self._gladefile)
            self.root = root

        def get_widget(self, name):
            return self.builder.get_object(name)

        def connect_signals(self, callbacks):
            self.builder.connect_signals(callbacks)

        def signal_autoconnect(self, callbacks):
            self.builder.connect_signals(callbacks)

    class _GladeModule(types.SimpleNamespace):
        def __init__(self):
            super().__init__(XML=_GladeXML)

        def bindtextdomain(self, *args, **kwargs):
            return None

        def textdomain(self, *args, **kwargs):
            return None

    # Attach glade compatibility
    gtk.glade = _GladeModule()
    sys.modules["gtk.glade"] = gtk.glade

    globals().update({"gtk": gtk, "gobject": gobject, "pango": pango})
    globals().update({"USE_GI": True})


try:
    _setup_pygtk()
except Exception as e_pygtk:
    try:
        _setup_gi()
    except Exception as e_gi:
        raise ImportError("Unable to load GTK; PyGTK failed with '%s' and PyGObject failed with '%s'"
                          % (e_pygtk, e_gi))

__all__ = ["gtk", "gobject", "pango", "USE_PYGTK", "USE_GI", "_resolve_glade_file"]
