
import configparser

config = configparser.RawConfigParser()
config.read(".\\_Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        base_url = config.get('common info', 'baseURL')
        return base_url

    @staticmethod
    def getUserName():
        user = config.get('common info', 'username')
        return user

    @staticmethod
    def getPassword():
        passwd = config.get('common info', 'password')
        return passwd

    @staticmethod
    def getpageTitleBefLogin():
        pageTitle_befLogin = config.get('common info', 'pagetitle_beforelogin')
        return pageTitle_befLogin

    @staticmethod
    def getpageTitleAftLogin():
        pageTitle_aftLogin = config.get('common info', 'pagetitle_afterlogin')
        return pageTitle_aftLogin

    @staticmethod
    def getExcelFilePath():
        excelFile = config.get('common info', 'excel_file_path')
        return excelFile
