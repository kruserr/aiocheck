import aiocheck


def main():
    """
        Entrypoint for running the CLI script
    """

    aiocheck.cli().run_forever()

if __name__ == "__main__":
    main()
