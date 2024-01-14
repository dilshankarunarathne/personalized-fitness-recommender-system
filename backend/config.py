import configparser 

config = configparser.RawConfigParser()
config.read('backend/application.properties')


def get(section: str, key: str):
    return config[section][key]

# TODO remove this
# print(config.sections())
# print(get('data', 'dataset'))
