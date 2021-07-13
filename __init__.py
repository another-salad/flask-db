"""Init file for Flask-DB"""

import sys
import os


sys.path.append(os.path.abspath(os.path.join(__file__, "/app/")))
sys.path.append(os.path.abspath(os.path.join(__file__, "/app/common/")))
sys.path.append(os.path.abspath(os.path.join(__file__, "/app/local/")))
sys.path.append(os.path.abspath(os.path.join(__file__, "/tests/")))
