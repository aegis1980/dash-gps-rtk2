import functools
import json
import os
from typing import Dict
import configparser

'''
Load config from config.toml
'''

config = configparser.ConfigParser()
config.read(os.path.join('config.ini'))

OG_DESCRIPTION = config['OpenGraph']['Description']

PATH_DATA = os.path.join(os.getcwd(),config['Paths']['Data']) 
PATH_TEMP = os.path.join(os.getcwd(),config['Paths']['Temp']) 

class LayoutID:

    MODAL_ABOUT = "modal-splash"
    MODAL_ABOUT_CLOSE = "modal-splash-close"

    MODAL_SETTINGS = "modal-settings"
    MODAL_SETTINGS_CLOSE = "modal-settings-close"
   
    NAVLINK_ABOUT = "navlink_about"
    NAVLINK_SETTINGS = "navlink_settings"

    
    TABS = "tabs"
    TAB_CONTENT = "tab-content"

    URL = "url"
