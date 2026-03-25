# Copyright 2003-2026 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

PYTHON_COMPAT=( python3_{9..13} )
DISTUTILS_USE_PEP517=setuptools

inherit distutils-r1 desktop xdg-utils

DESCRIPTION="GTK+ frontend to Portage"
HOMEPAGE="https://github.com/abdonmorales/porthole"
SRC_URI="https://github.com/abdonmorales/porthole/archive/refs/tags/v${PV}.tar.gz -> ${P}.tar.gz"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE="test"
RESTRICT="!test? ( test )"

RDEPEND="
	dev-python/pygobject:3[${PYTHON_USEDEP}]
	x11-libs/gtk+:3[introspection]
	sys-apps/portage
"
BDEPEND="
	test? (
		dev-python/pytest[${PYTHON_USEDEP}]
	)
"

S="${WORKDIR}/${P}"

distutils-r1_python_test() {
	epytest tests/
}

src_install() {
	distutils-r1_src_install
	domenu porthole.desktop
	doicon porthole/pixmaps/porthole-icon.png
}

pkg_postinst() {
	xdg_desktop_database_update
	xdg_icon_cache_update
}

pkg_postrm() {
	xdg_desktop_database_update
	xdg_icon_cache_update
}
