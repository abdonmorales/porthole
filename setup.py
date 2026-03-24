#!/usr/bin/env python3

from setuptools import setup, find_packages

datadir = "share/porthole/"

setup(
    name="porthole",
    version="0.7.0",
    description="GTK+ frontend to Portage",
    author="Fredrik Arnerup, Daniel G. Taylor, Brian Dolbec, William F. Wheeler",
    author_email="dol-sen@users.sourceforge.net",
    url="https://github.com/abdonmorales/porthole",
    packages=find_packages(include=["porthole", "porthole.*"]),
    package_data={
        "porthole": [
            "glade/*.glade",
            "pixmaps/*.png",
            "pixmaps/*.svg",
            "help/*.html",
            "help/*.css",
            "help/*.png",
            "config/*.xml",
            "i18n/*.pot",
            "i18n/*.po",
            "i18n/TRANSLATING",
        ],
    },
    scripts=["scripts/porthole"],
    data_files=[
        (datadir + "pixmaps", [
            "porthole/pixmaps/porthole-about.png",
            "porthole/pixmaps/porthole-icon.png",
            "porthole/pixmaps/porthole-clock-20x20.png",
            "porthole/pixmaps/porthole-clock.png",
            "porthole/pixmaps/porthole.svg",
        ]),
        (datadir + "help", [
            "porthole/help/advemerge.html", "porthole/help/advemerge.png",
            "porthole/help/changelog.png", "porthole/help/custcmd.html",
            "porthole/help/custcmd.png", "porthole/help/customize.html",
            "porthole/help/dependencies.png", "porthole/help/index.html",
            "porthole/help/install.html", "porthole/help/installedfiles.png",
            "porthole/help/mainwindow.html", "porthole/help/mainwindow.png",
            "porthole/help/porthole.css", "porthole/help/queuetab.png",
            "porthole/help/search.html", "porthole/help/summarytab.png",
            "porthole/help/sync.html", "porthole/help/termrefs.html",
            "porthole/help/termwindow.html", "porthole/help/termwindow.png",
            "porthole/help/toc.html", "porthole/help/unmerge.html",
            "porthole/help/update.html", "porthole/help/warningtab.png",
            "porthole/help/depview.png", "porthole/help/ebuildtable_explained2.png",
            "porthole/help/upgradeables.png",
        ]),
        (datadir + "glade", [
            "porthole/glade/config.glade", "porthole/glade/advemerge.glade",
            "porthole/glade/porthole.glade", "porthole/glade/about.glade",
        ]),
        (datadir, [
            "scripts/dopot.sh", "scripts/pocompile.sh", "AUTHORS",
        ]),
        (datadir + "config", [
            "porthole/config/configuration.xml",
        ]),
        (datadir + "i18n", [
            "porthole/i18n/messages.pot", "porthole/i18n/vi.po",
            "porthole/i18n/fr_FR.po", "porthole/i18n/de_DE.po",
            "porthole/i18n/pl.po", "porthole/i18n/ru.po",
            "porthole/i18n/TRANSLATING",
        ]),
        ("share/applications", ["porthole.desktop"]),
        ("share/pixmaps", ["porthole/pixmaps/porthole-icon.png"]),
    ],
    python_requires=">=3.9",
)
