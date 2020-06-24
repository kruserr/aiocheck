from aiocheck import Database, Host
import pytest
import json


def test___init__():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert host1._Host__db == db
    assert host1._Host__addr == addr1

def test___str__():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert str(host1) == json.dumps(host1.get_json(), indent=4, default=str)

def test___eq__():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert (host1 == host1) == True
    assert (host1 == host2) == False

def test_get_csv():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert host1.get_csv() == f"{host1._Host__addr}, {host1._Host__alive}, {host1._Host__timestamp}\n"

def test_get_json():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert host1.get_json() == {
        'addr': host1._Host__addr,
        'alive': host1._Host__alive,
        'timestamp': host1._Host__timestamp,
        'errors': host1._Host__errors,
        'data': host1._Host__data,
    }

def test_get_timestamp():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert host1.get_timestamp() == host1._Host__timestamp

def test_get_addr():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert host1.get_addr() == host1._Host__addr

def test_is_alive():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    assert host1.is_alive() == host1._Host__alive

def test_is_alive():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)

    errors = []
    host1._Host__check_error(errors, '100%', 'host_packet_loss') == []
