import logging
from logging.handlers import RotatingFileHandler
import os
import pathlib

class Log:

    # Création du dossier des logs (si besoin)
    _dir = os.path.join(os.getcwd(), "log")
    pathlib.Path(_dir).mkdir(parents=True, exist_ok=True)
    # logger
    _logger = logging.getLogger('Rotating Log')
    _logger.setLevel(logging.INFO)
    formatter = logging.Formatter( '%(asctime)s : %(message)s')
    handler = RotatingFileHandler( os.path.join(_dir, "log.txt"), encoding='utf-8', maxBytes=204800, backupCount=5)
    handler.setFormatter(formatter)
    _logger.addHandler(handler)

    _logger.info('-' * 80)

    @classmethod
    def set_callback(cls, func):
        cls._func = func
    
    @classmethod
    def add(cls, text):
        cls._logger.info( text )
        try:
            cls._func( text )
        except:
            pass