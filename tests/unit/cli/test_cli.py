import aiocheck

import pytest
import os


def test_cli():
    db = aiocheck.Database()
    try:
        os.remove(db.get_log_file())
        os.remove(db.get_persist_file())
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
        rows = f.readlines()
    assert rows[0] == db.get_csv_header()
    assert rows[1].split(',')[0] == addr1
    
    addr2 = '10.20.30.50'
    aiocheck.cli(
        f"localhost {addr2}",
        timeout=10,
        menu=False,
    ).run_forever()
    with open(db.get_log_file(), 'r') as f:
        rows = f.readlines()
    assert rows[0] == db.get_csv_header()
    assert rows[1].split(',')[0] == addr1
    addr2_in_rows = False
    for row in rows:
        if row.split(',')[0] == addr2:
            addr2_in_rows = True
    assert addr2_in_rows == True
    
    with open(db.get_log_file(), "r") as f:
        rows = f.readlines()[1:]
    with open(db.get_log_file(), 'w') as f:
        f.write("\n".join(rows))
    aiocheck.cli(
        f"localhost {addr2}",
        timeout=10,
        menu=False,
    ).run_forever()
    with open(db.get_log_file(), 'r') as f:
        rows = f.readlines()
    assert rows[0] == db.get_csv_header()
    assert rows[1].split(',')[0] == addr2
    
    aiocheck.cli(
        f"-m status localhost {addr1} {addr2}",
        timeout=10,
        menu=False,
    ).run_forever()
    with open(db.get_log_file(), 'r') as f:
        rows = f.readlines()
    assert rows[0] == db.get_csv_header()

    addr_in_rows = []
    for row in rows:
        if row.split(',')[0] == addr1:
            addr_in_rows.append(addr1)
        if row.split(',')[0] == addr2:
            addr_in_rows.append(addr2)

    assert len(addr_in_rows) == 2
    assert addr1 in addr_in_rows
    assert addr2 in addr_in_rows
    
    aiocheck.cli(
        f"-m status localhost {addr1}",
        timeout=10,
        menu=False,
    ).run_forever()
    with open(db.get_log_file(), 'r') as f:
        rows = f.readlines()
    assert rows[0] == db.get_csv_header()
    assert rows[1].split(',')[0] == addr1

    try:
        os.remove(db.get_log_file())
        os.remove(db.get_persist_file())
    except FileNotFoundError:
        pass
