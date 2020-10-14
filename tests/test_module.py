import pytest
from src.pygration.command import main
from click.testing import CliRunner

def test_no_argv():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert result.output == 'Hello, World!\n'

def test_name():
    runner = CliRunner()
    result = runner.invoke(main, ['--name=Peter'])
    assert result.exit_code == 0
    assert result.output == 'Hello, Peter!\n'