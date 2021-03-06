import logging
import locale

from src.config import env
from src.app import App

class Setup:
    def __init__(self):
        self.set_logging()
        self.set_locale()

    def set_logging(self):
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)
        logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

    def set_locale(self):
        locale.setlocale(locale.LC_ALL, env.LOCALE)

    def init_app(self):
        app = App()
        app.do_routine()

        if env.HAS_ROUTINE:
            app.start_routine()