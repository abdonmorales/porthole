#!/usr/bin/env python3

'''
    Porthole About Dialog
    Shows information about Porthole

    Copyright (C) 2003 - 2008 Fredrik Arnerup and Daniel G. Taylor

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
'''


import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from porthole import backends, config
from porthole.loaders.loaders import decode_text, get_textfile, load_web_page
from porthole.utils import debug
from porthole.version import copyright, version

portage_lib = backends.portage_lib

class AboutDialog:
    """Class to hold about dialog and functionality."""

    def __init__(self):
        # setup glade
        self.gladefile = config.Prefs.DATA_PATH + 'glade/about.glade' #config.Prefs.use_gladefile
        self.wtree = Gtk.Builder()

        self.wtree.set_translation_domain(config.Prefs.APP)

        self.wtree.add_objects_from_file(self.gladefile, ["about_dialog"])
        # register callbacks
        callbacks = {"on_ok_clicked" : self.ok_clicked,
                     "on_homepage_clicked" : self.homepage_clicked}
        self.wtree.connect_signals(callbacks)
        self.wtree.get_object('porthole-about-img').set_from_file(config.Prefs.DATA_PATH + "pixmaps/porthole-about.png")
        self.copyright = self.wtree.get_object('copyright_label')
        self.copyright.set_label(copyright)
        self.authorview = self.wtree.get_object('authorview')
        self.licenseview = self.wtree.get_object('licenseview')
        license_file = portage_lib.settings.portdir + "/licenses/GPL-2"
        author_file = config.Prefs.AUTHORS
        self.licenseview.get_buffer().set_text(decode_text(get_textfile(license_file)))
        self.authorview.get_buffer().set_text(decode_text(get_textfile(author_file)))
        window = self.wtree.get_object("about_dialog")
        window.set_title(_("About Porthole %s") % version)
        debug.dprint("ABOUT: Showing About dialog")

    def ok_clicked(self, widget):
        """Get rid of the about dialog!"""
        self.wtree.get_object("about_dialog").destroy()

    def homepage_clicked(self, widget):
        """Open Porthole's Homepage!"""
        load_web_page("http://porthole.sourceforge.net")
