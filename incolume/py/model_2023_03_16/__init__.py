"""
Principal Module.

Update metadata from version by semver
"""
import logging
from pathlib import Path

try:
    from tomli import load
except (ImportError, ModuleNotFoundError) as e:
    logging.error(e)
    from tomlib import load


configfile = Path(__file__).parents[3].joinpath("pyproject.toml")
versionfile = Path(__file__).parent.joinpath("version.txt")

with configfile.open("rb") as f:
    versionfile.write_text(f"{load(f)['tool']['poetry']['version']}\n")

__version__ = versionfile.read_text().strip()

if __name__ == "__main__":
    print(__version__)
