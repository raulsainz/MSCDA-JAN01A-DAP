# =============================================================================
# Created By  : Raul Sainz
# Created Date: 2021-03-21
# =============================================================================
"""The Module Has Been Build for DAP Project"""
# =============================================================================
# Installs all the necesary libraries used in the notebooks
# =============================================================================

import sys
import subprocess
import importlib
import pip
# implement pip as a subprocess:
def install_library(lib_name): 
    try:
        importlib.import_module(lib_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib_name])
libs = [ 'psycopg2',                  
        'pymongo',                  #MongoDB Driver
        'urllib',                   #Library to url encode the password
        'os',                       #os library to interact with host OS
        'math',
        'termcolor' ,               #Function to print console message with colors
        'datetime' ,                #Library for getting tim
        'requests',                 #Library allows to send send HTTP requests
        'urllib' ,                  #Library to make URL request to Wikipedia API
        'matplotlib',
        'seaborn',
        'nltk',                  #ligrary for naturale language processing
        'string',
        'json',
        'io',
        'bs4',
        're',
        'requests']
for lib in libs:
    print('installing library {}...'.format(lib))
    install_library(lib)