import configparser


config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUname():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPass():
        password = config.get('common data', 'password')
        return password
