"""Tests for porthole version module."""

import re


def test_version_format():
    """Version string should follow semver-like X.Y.Z format."""
    from porthole.version import version

    assert re.match(r"^\d+\.\d+\.\d+$", version), f"Version {version!r} does not match X.Y.Z format"


def test_version_value():
    """Current version should be 0.7.0."""
    from porthole.version import version

    assert version == "0.7.0"


def test_copyright_exists():
    """Copyright string should be present."""
    from porthole.version import copyright

    assert "Copyright" in copyright or "copyright" in copyright.lower()
