#!/usr/bin/env python3
"""
Modernized setuptools installer for Porthole.
Kept data_files layout for Gentoo while allowing PEP 517 builds.
"""

from pathlib import Path

try:
    from setuptools import setup
except ImportError:  # fallback for very old environments
    from distutils.core import setup

from porthole.version import version as p_version

root = Path(__file__).parent
datadir = "share/porthole/"

long_description = ""
readme_path = root / "README"
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

setup(
    name="porthole",
    version=p_version,
    description="GTK+ frontend to Portage",
    long_description=long_description,
    author="Fredrik Arnerup, Daniel G. Taylor, Brian Dolbec, William F. Wheeler",
    author_email="dol-sen@users.sourceforge.net, "
                 "farnerup@users.sourceforge.net, dgt84@users.sourceforge.net, "
                 "tiredoldcoder@users.sourceforge.net",
    url="http://porthole.sourceforge.net",
    license="GPL-2",
    python_requires=">=3.8",
    packages=[
        'porthole', 'porthole.advancedemerge', 'porthole.backends', 'porthole.config',
        'porthole.db', 'porthole.dialogs', 'porthole.loaders', 'porthole.packagebook',
        'porthole.plugins', 'porthole.loaders', 'porthole.readers', 'porthole.terminal',
        'porthole.utils', 'porthole.views', 'porthole._xml', 'porthole.plugins.etc-proposals',
        'porthole.plugins.profuse'
    ],
    package_dir={'porthole': 'porthole'},
    scripts=["scripts/porthole"],
    include_package_data=True,
    data_files=[
        (datadir + "pixmaps",
         ["porthole/pixmaps/porthole-about.png", "porthole/pixmaps/porthole-icon.png",
          "porthole/pixmaps/porthole-clock-20x20.png", "porthole/pixmaps/porthole-clock.png",
          "porthole/pixmaps/porthole.svg"]),
        (datadir + "help",
         ["porthole/help/advemerge.html", "porthole/help/advemerge.png", "porthole/help/changelog.png",
          "porthole/help/custcmd.html", "porthole/help/custcmd.png", "porthole/help/customize.html",
          "porthole/help/dependencies.png", "porthole/help/index.html", "porthole/help/install.html",
          "porthole/help/installedfiles.png", "porthole/help/mainwindow.html", "porthole/help/mainwindow.png",
          "porthole/help/porthole.css", "porthole/help/queuetab.png", "porthole/help/search.html",
          "porthole/help/summarytab.png", "porthole/help/sync.html", "porthole/help/termrefs.html",
          "porthole/help/termwindow.html", "porthole/help/termwindow.png", "porthole/help/toc.html",
          "porthole/help/unmerge.html", "porthole/help/update.html", "porthole/help/warningtab.png",
          "porthole/help/depview.png", "porthole/help/ebuildtable_explained2.png",
          "porthole/help/upgradeables.png"]),
        (datadir + "glade",
         ["porthole/glade/config.glade", "porthole/glade/advemerge.glade",
          "porthole/glade/porthole.glade", "porthole/glade/about.glade"]),
        (datadir + "glade3",
         ["porthole/glade3/config.ui", "porthole/glade3/advemerge.ui",
          "porthole/glade3/porthole.ui", "porthole/glade3/about.ui"]),
        (datadir,
         ["scripts/dopot.sh", "scripts/pocompile.sh", "AUTHORS"]),
        (datadir + "config",
         ["porthole/config/configuration.xml"]),
        (datadir + "i18n",
         ["porthole/i18n/messages.pot", "porthole/i18n/vi.po", "porthole/i18n/fr_FR.po", "porthole/i18n/de_DE.po",
          "porthole/i18n/pl.po", "porthole/i18n/ru.po", "porthole/i18n/TRANSLATING"]),
        ("share/applications", ["porthole.desktop"]),
        ("share/pixmaps", ["porthole/pixmaps/porthole-icon.png"])
    ],
    classifiers=[
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Software Distribution"
    ],
)
