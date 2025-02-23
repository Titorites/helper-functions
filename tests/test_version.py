"""Unit tests for __version__.py."""

import ken.helper_functions


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(ken.helper_functions, "__version__")
    assert ken.helper_functions.__version__ != "0.0.0"
