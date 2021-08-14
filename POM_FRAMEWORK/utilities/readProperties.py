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

    @staticmethod
    def getFirstName():
        firstname = config.get('common data', 'firstname')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('common data', 'lastname')
        return lastname

    @staticmethod
    def getPostal():
        postal = config.get('common data', 'postal')
        return postal
