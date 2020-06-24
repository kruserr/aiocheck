from aiocheck import Database
import subprocess
import pytest
import signal
import time
import os


def test_cli():
    db = Database()
    try:
        os.remove(db.get_log_file())
    except FileNotFoundError:
        pass

    p1 = subprocess.Popen(['aiocheck'])
    time.sleep(1)
    p1.terminate()
    p1.wait()

    with pytest.raises(FileNotFoundError):
        with open(db.get_log_file(), 'r') as f:
            pass
    
    p2 = subprocess.Popen(['aiocheck', 'localhost'])
    time.sleep(10)
    p2.terminate()
    p2.wait()

    with pytest.raises(FileNotFoundError):
        with open(db.get_log_file(), 'r') as f:
            pass
    
    addr1 = '10.20.30.40'

    p3 = subprocess.Popen(['aiocheck', 'localhost', addr1])
    time.sleep(10)
    p3.terminate()
    p3.wait()

    with open(db.get_log_file(), 'r') as f:
        data = f.read()
    rows = data.split('\n')
    assert rows[0] == db.get_csv_header().replace('\n', '')
    assert rows[1].split(',')[0] == addr1


if __name__ == "__main__":
    test_cli()
