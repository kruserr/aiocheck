from aiocheck import Database, Host
import pytest


def test___init__():
    Database()
    Database('')
    Database('verbose')
    Database('status')
    Database([''])
    Database((''))

def test_insert():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)

    db.insert(Host(addr1, db))
    db.insert(Host(addr2, db))

    assert db._Database__hosts[0].get_addr() == addr1
    assert db._Database__hosts[1].get_addr() == addr2

    with pytest.raises(ValueError):
        db.insert(addr1)
    with pytest.raises(ValueError):
        db.insert([addr1])
    with pytest.raises(ValueError):
        db.insert((addr1))

def test_select():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)

    db.insert(Host(addr1, db))

    assert db.select()[0].get_addr() == addr1
    assert db.select(addr1).get_addr() == addr1
    assert db.select(addr2) == None

    assert db.select(addr3) == None
    assert db.select([addr1, addr2, addr3]) == None
    assert db.select((addr1, addr2, addr3)) == None

def test_insert_error():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)

    db.insert_error(host1.get_json())
    assert db._Database__errors[0] == host1.get_json()

def test_select_error():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)

    db.insert_error(host1.get_json())
    assert len(db.select_error()) == 1
    assert db.select_error()[0] == host1.get_json()
    assert db.select_error(addr1) == host1.get_json()
    assert db.select_error(addr2) == {}

    assert db.select_error(addr3) == {}
    assert db.select_error([addr1, addr2, addr3]) == {}
    assert db.select_error((addr1, addr2, addr3)) == {}

    db.insert_error(host1.get_json())
    assert len(db.select_error()) == 1

def test_select_newest_errors():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)

    assert db.select_newest_errors() == []
    db.insert_error(host1.get_json())
    assert len(db.select_newest_errors()) == 1
    assert db.select_newest_errors()[0] == host1.get_json()
    db.insert_error(host1.get_json())
    assert len(db.select_newest_errors()) == 1
    assert db.select_newest_errors()[0] == host1.get_json()

def test___error_equal():
    db = Database()
    addr1 = 'localhost'
    addr2 = '127.0.0.1'
    addr3 = 'x011?!-\n/\\nw#!/.,x;{test}[lol]'
    host1 = Host(addr1, db)
    host2 = Host(addr2, db)
    host3 = Host(addr2, db)

    assert db._Database__error_equal(host1.get_json(), host1.get_json()) == True
    assert db._Database__error_equal(host1.get_json(), host2.get_json()) == False

    host3._Host__alive = True
    assert db._Database__error_equal(host2.get_json(), host3.get_json()) == False
