import configparser

## this class is a singleton to not read the config file all the time
class configReader():
    
    _instance = None

    #called before __init__ and used to manage the singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    
    def __init__(self):
            self.config = configparser.ConfigParser()
            self.config.read('config.ini')
    
    ## getter for the users and password values
    def get_standard_user(self) -> str:
       return self.config['USERS']['standard']
    
    def get_locked_user(self) -> str:
       return self.config['USERS']['locked']
    
    def get_problem_user(self) -> str:
       return self.config['USERS']['problem']
    
    def get_badperf_user(self) -> str:
       return self.config['USERS']['bad_perf']
    
    def get_visual_user(self) -> str:
       return self.config['USERS']['visual']
    
    def get_password(self) -> str:
       return self.config['USERS']['secret_sauce']
    
    #getter for the timeout values
    def get_url_timeout(self) -> int:
        return int(self.config['TIMEOUT']['wait_url_timeout'])
    
    #getter for the urls
    def get_website_url(self) -> str:
       return self.config['URL']['saucedemo_url']
    
    
 
