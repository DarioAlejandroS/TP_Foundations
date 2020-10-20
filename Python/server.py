from flask import Flask
from flask import request
import os
import sys

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def run_datapro():
       if sys.platform == 'win32': 
            os.system ("python C:\\Users\\Dario\\Desktop\\TP\\Python\\datapro.py")
            return "Entre en windows"
       else:
            # In Linux
            os.system ("python /home/datapro.py")
            os.system ("python /home/queries.py")
            return "Entre en Linux"

app.run(debug=True, host='0.0.0.0', port=5000)