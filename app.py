#!/opt/miniconda3/bin/python3
__author__ = "Vishnu Prasad"
__version__ = "1.0"
__status__ = "Dev"

import gc

from flask import Flask
from service import serv
from utility import FileReader

gc.collect()
app = Flask(__name__)
app.config["COMPRESS_LEVEL"] = 6
app.register_blueprint(serv)
config = FileReader().file_reader()
if __name__ == '__main__':
    app.run(host=config["host"], port=config["port"], debug=True, threaded=True,
            use_reloader=False)
