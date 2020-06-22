# aiocheck
A python asyncio host health checker using native ping commands.

Example:
```
aiocheck 10.20.30.40 10.20.30.50 10.20.30.60
```

stdout:
```
###########
# Running #
###########

Addresses: ['10.20.30.50', '10.20.30.40', '10.20.30.60']

Press CTRL+C to exit 
```

aiocheck_log.csv:
```
address, alive, timestamp
10.20.30.60, False, 2020-06-22 17:35:40.398753
10.20.30.40, False, 2020-06-22 17:35:40.398729
10.20.30.50, False, 2020-06-22 17:35:40.398660
```

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

# Develop

### Open in VS Code
```
git clone https://github.com/kruserr/aiocheck.git
cd aiocheck
code .
```

### Run VS Code Tasks
CTRL+SHIFT+B

or

CTRL+P
```
>Tasks: Run Task
```
