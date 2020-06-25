import aiocheck
from aiocheck.cli.main import main

import os
import sys
import asyncio
import argparse


class cli():
    """
        Class to interact with the program using the CLI.

        Example:
        ```
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

        This class allows for a interactive CLI experiance,
        and also a no menu option where it is more suited
        to be used for scripting in python.

        It also features a timeout setting, where you may
        wish to only run the program for a given number of 
        seconds.
    """

    def __init__(self, func_args = '', timeout = None, menu = True):
        parser = argparse.ArgumentParser(description='Healthcheck')

        parser.add_argument(
            'addresses', metavar='address', type=str, default=[], nargs='*',
            help='One or more addresses to ping',
        )
        parser.add_argument(
            '--mode', '-m',
            help='Set logging mode | verbose, status | default verbose',
            default='verbose',
        )

        if len(func_args) == 0:
            try:
                self.__args = parser.parse_args()
            except:
                self.__args = parser.parse_args(func_args.split())
        else:
            self.__args = parser.parse_args(func_args.split())
        
        self.__exit = False
        self.__menu = menu
        self.__timeout = timeout
        self.__db = aiocheck.Database(self.__args.mode)
        self.__args.addresses = set(self.__args.addresses)

        self.__loop = asyncio.get_event_loop()

    def __clear_console(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def __get_header(self, text):
        def wrap():
            result = ''
            for _ in range(len(text) + 4):
                result += '#'
            return result
        
        return f"{wrap()}\n# {text} #\n{wrap()}\n\nAddresses: {list(self.__args.addresses)}\n"
    
    def __func_menu(self):
        if len(self.__args.addresses) == 0:
            select = ''
            while select != '0':
                self.__clear_console()
                print(f"{self.__get_header('Menu')}\n[1] - Run\n[2] - Add Address\n[0] - Exit\n")

                select = input()
                
                if select == '0':
                    self.__exit = True
                    return
                
                if select == '1':
                    if len(self.__args.addresses) == 0:
                        input('No Address Provided ')
                    else:
                        break
                
                if select == '2':
                    self.__clear_console()
                    print(f"{self.__get_header('Add Address')}")

                    inner_select = input('Enter an Address: ')
                    self.__args.addresses.update(inner_select.split())

    def run_forever(self):
        """
            Start the eventloop with run_forever

            Example:
            ```
            aiocheck.cli().run_forever()
            ```
        """

        if self.__menu:
            self.__func_menu()

        if self.__exit:
            return

        self.__clear_console()
        sys.stdout.write(f"{self.__get_header('Running')}\nPress CTRL+C to exit ")

        for address in self.__args.addresses:
            self.__db.insert(aiocheck.Host(address, self.__db))
        
        asyncio.ensure_future(self.__func_timeout())

        try:
            self.__loop.run_forever()
        except KeyboardInterrupt:
            pass

    def stop(self):
        """
            Stop the event loop
        """

        self.__loop.stop()

    async def __func_timeout(self):
        if self.__timeout is not None:
            await asyncio.sleep(self.__timeout)
            self.__loop.stop()
