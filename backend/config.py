import configparser 

config = configparser .RawConfigParser()
config.read('application.properties')


def get(section: str, key: str):
    return config[section][key]
