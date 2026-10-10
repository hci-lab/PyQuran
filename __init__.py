"""
"""
from pyquran.tools import quran
from pyquran.tools import arabic

try:
    from pyquran.core.pyquran import *  # noqa: F401,F403
except ModuleNotFoundError as exc:
    if exc.name not in {"numpy", "pyarabic"}:
        raise
