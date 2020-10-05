from click.testing import CliRunner
from pysizer import main

def test_pysizer_main():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert "Picture resizing took" in  result.output

