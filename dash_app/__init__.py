import functools
import json
import os
from typing import Dict
import configparser

'''
Load config from config.toml
'''
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

with open("./config.toml", "rb") as f:
    CONFIG = tomllib.load(f)


PATH_DATA = os.path.join(os.getcwd(),CONFIG['paths']['data']) 
PATH_TEMP = os.path.join(os.getcwd(),CONFIG['paths']['temp']) 

class LayoutID:
    URL = "url"
    MQTT = "mqtt"

class Mqtt:
    BROKER_URL = "127.0.0.1"
    BROKER_PORT = 8083
    TOPIC_STATUS = "testtopic"
    TOPIC_NMEA = "testtopic"