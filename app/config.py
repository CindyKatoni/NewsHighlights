class Config:
    '''
    General configuration parent class. Configurations used in production
    and Development stages.
    '''
    pass



class ProdConfig(Config):
    '''
    Has configurations used in Production Stages.

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Has Configurations used in the Development Stages. DEBUG=TRUE to enable debug
    mode in our app.

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True