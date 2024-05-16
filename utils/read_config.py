import configparser


def read_config():
    """
    The `read_config` function reads a configuration file using ConfigParser and returns a dictionary
    with log level information.
    :return: A dictionary containing the log level value read from the config file is being returned.
    """
    # Create a ConfigParser object and read config file
    config = configparser.ConfigParser()
    config.read('./config/config.ini')

    # Access values from config file and create a dict
    log_level = config.get('logger', 'level')
    config_data = {
        'log_level': log_level
    }

    return config_data

config_data = read_config()
