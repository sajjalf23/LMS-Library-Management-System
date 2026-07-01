import pytest
from lms.main import main

def test_main_function():
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from lms!\n"