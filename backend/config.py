import configparser 

config = configparser.RawConfigParser()
config.read('backend/application.properties')


def get(section: str, key: str):
    return config[section][key]


# print(config.sections())
# print(get('tesseract', 'dir'))
