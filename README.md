# Porthole 0.7.0

[![CI](https://github.com/abdonmorales/porthole/actions/workflows/ci.yml/badge.svg)](https://github.com/abdonmorales/porthole/actions/workflows/ci.yml)

Porthole is a GTK-based frontend for Portage (the Gentoo package management system). It features a hierarchical view of packages and supports fast searches and dependency calculations. Porthole also supports basic emerge features (emerge, unmerge, sync, upgrade world).

Porthole is released under the GPL v2, see [COPYING](COPYING).

Porthole is partially based on an earlier program called gportage, which has been discontinued in favour of Porthole.

## What's New in 0.7.0

- **Python 3 support** -- Migrated the entire codebase from Python 2 to Python 3.9+
- **GTK 3 support** -- Migrated from PyGTK (GTK 2) to PyGObject (GTK 3) while preserving the original UI
- **Modern packaging** -- Added `pyproject.toml` with setuptools backend
- **CI/CD** -- Added GitHub Actions for linting, testing, and building
- **Gentoo ebuild** -- Updated ebuild using EAPI 8 and `distutils-r1` eclass
- **Linting** -- Added ruff configuration for code quality
- **Test suite** -- Added pytest-based test infrastructure

For a full history of changes, see [NEWS](NEWS).

## Requirements

- Python >= 3.9
- PyGObject (GTK 3 bindings)
- GTK 3
- Portage (Gentoo package manager)

### System Dependencies (Gentoo)

```bash
emerge --ask dev-python/pygobject x11-libs/gtk+:3
```

## Installation

### From Gentoo Ebuild (Recommended)

The recommended way to install Porthole on Gentoo is via the ebuild. Download the ebuild from the [Releases](https://github.com/abdonmorales/porthole/releases) page and place it in your local overlay:

```bash
# Create overlay directory structure
mkdir -p /var/db/repos/local/app-portage/porthole

# Copy the ebuild
cp porthole-0.7.0.ebuild /var/db/repos/local/app-portage/porthole/

# Generate manifest
cd /var/db/repos/local/app-portage/porthole
ebuild porthole-0.7.0.ebuild manifest

# Install
emerge --ask app-portage/porthole
```

### From Source

```bash
git clone https://github.com/abdonmorales/porthole.git
cd porthole
pip install .
```

### From Tarball

```bash
tar xzf porthole-0.7.0.tar.gz
cd porthole-0.7.0
python setup.py install
```

## Development

### Setting Up

```bash
git clone https://github.com/abdonmorales/porthole.git
cd porthole
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/ -v
```

### Linting

```bash
pip install ruff
ruff check porthole/ tests/
```

### Building

```bash
pip install build
python -m build
```

## Running Locally

To run Porthole from the source tree without installing:

```bash
python scripts/porthole --local
```

## Bug Reports

We welcome bug reports! Please use the issue tracker at:
https://github.com/abdonmorales/porthole/issues

Please include the version of Porthole you experienced the bug in.

## Contact

- Repository: https://github.com/abdonmorales/porthole
- Brian Dolbec (original lead): dol-sen@users.sourceforge.net

### Original Authors (inactive/retired)

- Fredrik Arnerup (inactive)
- Daniel G. Taylor (retired)
- William F. Wheeler (retired)

## License

Porthole is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. See [COPYING](COPYING) for details.
