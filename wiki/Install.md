# aiocheck Wiki
### [<- Back](Home)

# Install
### Using pip
```
pip install aiocheck
aiocheck localhost
```

### Using pip from GitHub
```
pip install "git+https://github.com/kruserr/aiocheck.git"
aiocheck localhost
```

### Using python interpreter directly from GitHub
```
git clone https://github.com/kruserr/aiocheck.git
cd aiocheck
python src/aiocheck/cli/main.py localhost
```

### Using python interpreter directly and setuptools from GitHub
```
git clone https://github.com/kruserr/aiocheck.git
cd aiocheck
pip install setuptools wheel
python setup.py install
aiocheck localhost
```

### Using binary from GitHub
```
git clone https://github.com/kruserr/aiocheck.git
cd aiocheck
./bin/aiocheck.exe localhost
```

### Using self-built binary from GitHub
```
git clone https://github.com/kruserr/aiocheck.git
cd aiocheck
pip install pyinstaller
pyinstaller --onefile --name aiocheck --distpath bin src/aiocheck/cli/main.py
./bin/aiocheck.exe localhost
```
