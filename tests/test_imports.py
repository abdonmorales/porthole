"""Tests for verifying module imports work correctly after Python 3 migration."""

import importlib
import sys


def test_import_version():
    """porthole.version should import cleanly."""
    mod = importlib.import_module("porthole.version")
    assert hasattr(mod, "version")


def test_import_importer():
    """porthole.importer should import cleanly."""
    mod = importlib.import_module("porthole.importer")
    assert hasattr(mod, "my_import")


def test_python_version():
    """Ensure we are running Python 3.9+."""
    assert sys.version_info >= (3, 9), f"Python 3.9+ required, got {sys.version}"


def test_version_module_has_correct_attributes():
    """porthole.version should have version and copyright."""
    from porthole.version import version, copyright

    assert isinstance(version, str)
    assert len(version.split(".")) == 3


def test_importer_my_import_callable():
    """my_import should be a callable."""
    from porthole.importer import my_import

    assert callable(my_import)
