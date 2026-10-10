"""Public PyQuran package namespace."""

from pyquran.tools import arabic
from pyquran.tools import quran

try:
    from pyquran.core.pyquran import *  # noqa: F401,F403
except ModuleNotFoundError as exc:
    # Allow importing the package namespace before optional runtime deps exist.
    if exc.name not in {"numpy", "pyarabic"}:
        raise
