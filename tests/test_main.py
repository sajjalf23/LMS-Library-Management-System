import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
# pyrefly: ignore [missing-import]
from lms.main import main


def test_main_function():
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from lms!" in captured.out