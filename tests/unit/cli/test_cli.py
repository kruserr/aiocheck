import aiocheck

import pytest
import os


def test_cli():
    db = aiocheck.Database()
    try:
        os.remove(db.get_log_file())
    except FileNotFoundError:
        pass

    aiocheck.cli(
        timeout=1,
        menu=False,
    ).run_forever()
    with pytest.raises(FileNotFoundError):
        with open(db.get_log_file(), 'r') as f:
            pass

    aiocheck.cli(
        'localhost',
        timeout=10,
        menu=False,
    ).run_forever()
    with pytest.raises(FileNotFoundError):
        with open(db.get_log_file(), 'r') as f:
            pass
    
    addr1 = '10.20.30.40'
    aiocheck.cli(
        f"localhost {addr1}",
        timeout=10,
        menu=False,
    ).run_forever()
    with open(db.get_log_file(), 'r') as f:
        data = f.read()
    rows = data.split('\n')
    assert rows[0] == db.get_csv_header().replace('\n', '')
    assert rows[1].split(',')[0] == addr1
