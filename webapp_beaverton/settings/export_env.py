import os

from webapp_beaverton.settings.env import env_variables

def set_env(env_now):

    """
    1. get current envirnoment now
    2. setting common envirnoment variable
    3. setting development or production variable
    """

    # get envirnoment now
    envirnoment = env_now

    # export common envirnoment variable
    export_env_variable('common')

    # export development or production variable
    if 'development' in envirnoment:
        export_env_variable('development')
        print('export development is success!')

    elif 'production' in envirnoment:
        export_env_variable('production')
        print('export production is success!')
    else:
        print('envirnoment is error!')

def export_env_variable(key):
    dic =  env_variables.get(key)
    for env_key in dic:
        os.environ[env_key] = dic[env_key]
    return True
