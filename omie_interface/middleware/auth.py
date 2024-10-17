

from omie_interface.config import CONFIG






def auth(credential:str)->bool:
    if credential == CONFIG['token_agendup']:
       return True
    else:
        return False
    


