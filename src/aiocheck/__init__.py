"""
    aiocheck

    A python asyncio host health checker using native ping commands.

    Example:
    ```
    import aiocheck
    
    addrs = ''
    for i in range(0, 3):
        for j in range(1, 255):
            addrs += f"10.20.{i}.{j} "

    cli = aiocheck.cli(
        addrs,
        timeout=10,
        menu=False,
    )
    cli.run_forever()
    ```

    :copyright: 2020 kruserr
    :license: MIT
"""


from aiocheck.Database import Database
from aiocheck.Host import Host
from aiocheck.cli import cli
