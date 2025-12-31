# tests/conftest.py

import sys
from pathlib import Path

# This file lives in: secure-api-platform-demo/tests/conftest.py
# parents[1] is the project root: secure-api-platform-demo/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Add project root to Python path so "import app" works
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
