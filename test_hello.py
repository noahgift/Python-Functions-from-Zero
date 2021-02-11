from hello import with_input
from cli import callcolor
from click.testing import CliRunner

def test_with_input():
    """This is my library"""
    
    result = with_input("blue")
    assert result["old"] == "blue"

def test_cli():
    """This is my command-line tool"""
    runner = CliRunner()
    result = runner.invoke(callcolor, ['--color', 'blue'])
    assert result.exit_code == 0
    assert 'blue' in result.output
