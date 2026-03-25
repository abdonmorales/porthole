#!/usr/bin/env python3

"""
    ============
    | File Selector |
    -----------------------------------------------------------
    A graphical multipage notebook class
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

        from fileselector import FileSel
"""


import os

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


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
