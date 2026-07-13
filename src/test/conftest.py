import sys
from pathlib import Path

MAIN_PATH = Path(__file__).resolve().parents[1] / "main"

if str(MAIN_PATH) not in sys.path:
    sys.path.insert(0, str(MAIN_PATH))
