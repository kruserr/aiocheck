"""
    Build script for pyinstaller
"""

import subprocess


subprocess.run(['pyinstaller', '--onefile', 'aiocheck.py'])
