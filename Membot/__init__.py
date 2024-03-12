import config
import logging

API_ID = config.API_ID
API_HASH = config.API_HASH
PATH = config.PATH
logging.basicConfig(
     filename='mem_err.log',
     level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - \033[32;1m%(message)s\033[0m',
     datefmt='%H:%M:%S'
 )

console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s - \033[32;1m%(message)s\033[0m')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
