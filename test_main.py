import pytest
from main import main

def test_main_function():
    """Test that main function runs without errors"""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")

def test_main_output(capsys):
    """Test that main prints expected output"""
    main()
    captured = capsys.readouterr()
    assert "Hello from lms!" in captured.out
    assert "I am Main !" in captured.out