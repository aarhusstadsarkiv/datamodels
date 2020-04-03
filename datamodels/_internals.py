"""Auxiliary methods and classes used in datamodel implementations."""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from warnings import warn

# -----------------------------------------------------------------------------
# Warnings
# -----------------------------------------------------------------------------


class OverwriteWarning(UserWarning):
    """Warning to raise when a field will be overwritten during init."""


def warn_overwrite(message: str) -> None:
    """Helper function to raise an OverwriteWarning.

    Parameters
    ----------
    message : str
        The warning message to display.

    Raises
    -------
    OverwriteWarning
    """
    warn(message, OverwriteWarning)


# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------


def size_fmt(size: float) -> str:
    """Formats a file size in binary multiples to a human readable string.

    Parameters
    ----------
    size : float
        The file size in bytes.

    Returns
    -------
    str
        Human readable string representing size in binary multiples.
    """
    for unit in ["B", "KiB", "MiB", "GiB", "TiB"]:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.1f} {unit}"
