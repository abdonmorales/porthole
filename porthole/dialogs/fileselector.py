#!/usr/bin/env python3

"""
    ============
    | File Save |
    -----------------------------------------------------------
    Copyright (C) 2003 - 2008 Fredrik Arnerup, Brian Dolbec,
    Daniel G. Taylor, Wm. F. Wheeler, Tommy Iorns

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

    -------------------------------------------------------------------------
    To use this program as a module:

        from fileselector import FileSelector
"""

import gi

gi.require_version('Gtk', '3.0')
import os
import os.path
from gettext import gettext as _

from gi.repository import Gtk

from porthole.utils import debug


class FileSel:
    """File selection dialog using Gtk.FileChooserDialog (replaces removed Gtk.FileSelection)."""
    def __init__(self, title):
        self.title = title
        self.result = False

    def run(self, parent, start_file, func):
        dialog = Gtk.FileChooserDialog(
            title=self.title,
            parent=parent,
            action=Gtk.FileChooserAction.SAVE,
        )
        dialog.add_buttons(
            "Cancel", Gtk.ResponseType.CANCEL,
            "OK", Gtk.ResponseType.OK,
        )
        dialog.set_modal(True)

        if start_file:
            if os.path.isdir(start_file):
                dialog.set_current_folder(start_file)
            else:
                folder = os.path.dirname(start_file)
                if folder:
                    dialog.set_current_folder(folder)
                dialog.set_current_name(os.path.basename(start_file))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filename = dialog.get_filename()
            dialog.destroy()
            if func(filename):
                self.result = True
        else:
            dialog.destroy()

        return self.result


class FileSelector:
    """Generic file selector dialog for opening or saving files"""

    def __init__(self, parent_window, target_path, callback=None, overwrite_confirm=True):
        self.window = parent_window
        self.callback = callback
        self.overwrite_confirm = overwrite_confirm
        self.filename = ''
        self.directory = target_path

    def _save_as_ok_func(self, filename):
        """file selector callback function"""
        debug.dprint("FILESELECTOR: Entering _save_as_ok_func")
        if self.overwrite_confirm and (not self.filename or filename != self.filename):
            if os.path.exists(filename):
                err = _("Ovewrite existing file '%s'?") % filename
                dialog = Gtk.MessageDialog(self.window, Gtk.DialogFlags.MODAL,
                                            Gtk.MessageType.QUESTION,
                                            Gtk.ButtonsType.YES_NO, err)
                result = dialog.run()
                dialog.destroy()
                if result != Gtk.ResponseType.YES:
                    return False

        self.filename = filename
        return True

    def save_as(self, title):
        debug.dprint("FILESELECTOR: Entering save_as()")
        return FileSel(title).run(self.window, self.filename, self._save_as_ok_func)

    def get_filename(self, title):
        debug.dprint("FILESELECTOR: Entering get_filename()")
        result = FileSel(title).run(self.window, self.directory, self._save_as_ok_func)
        if result:
            return self.filename
        else:
            return ''
