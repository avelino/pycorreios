import correios
from correios import *

# __all__ = (correios.__all__ + cod.__all__)

__author__ = 'Thaigo Avelino'

VERSION = (0, 1, 2)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version

__version__ = get_version()
