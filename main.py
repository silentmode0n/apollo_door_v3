import os

# set current work dir
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import logging  # noqa: E402
from app import App  # noqa: E402
from app.parser import parser  # noqa: E402
from app.config import LOG_FILE  # noqa: E402
from app.debug import debug_condition  # noqa: E402


logging.basicConfig(level=logging.INFO,
                        filename=LOG_FILE,
                        filemode='a',
                        encoding='UTF-8',
                        format="%(asctime)s %(levelname)s %(message)s")


if __name__ == "__main__":
    try:
        args = parser.parse_args()
        condition = {key:value for (key, value) in vars(args).items() if value is not None and key != 'debug'}
        if args.debug:
            debug_condition.update(condition)
            condition = debug_condition
            print()
            print('----- Run in DEBUG mode -----')
            print()
        app = App()
        app.run(condition)
    except Exception as e:
        logging.critical('Критическое исключение!', exc_info=True)
        print('Критическое исключение: ', e)