from src import get_from_config, write_entry_point, Setup


def main() -> None:
    setup: Setup = {
        'get': get_from_config,
        'mail': False,
        'verbose': False,
        'cloud': False,
    }

    write_entry_point(setup)


if __name__ == '__main__':
    main()
