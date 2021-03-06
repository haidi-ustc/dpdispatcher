import logging
import os

ROOT_PATH=__path__[0]
NAME="dpdispatcher"
SHORT_CMD="dpdisp"
dlog = logging.getLogger(__name__)
dlog.setLevel(logging.INFO)
dlogf = logging.FileHandler(os.getcwd()+os.sep+SHORT_CMD+'.log')
dlogf_formatter=logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
#dlogf_formatter=logging.Formatter('%(asctime)s - %(name)s - [%(filename)s:%(funcName)s - %(lineno)d ] - %(levelname)s \n %(message)s')
dlogf.setFormatter(dlogf_formatter)
dlog.addHandler(dlogf)

__author__    = "DeepModeling Team"
__copyright__ = "Copyright 2019"
__status__    = "Development"
try:
    from ._version import version as __version__
except ImportError:
    __version__ = 'unkown'
try:
    from ._date import date as __date__
except ImportError:
    __date__ = 'unkown'

def info():
    """
        Show basic information about """+NAME+""", its location and version.
    """

    print('DeepModeling\n------------')
    print('Version: ' + __version__)
    print('Date:    ' + __date__)
    print('Path:    ' + ROOT_PATH)
    print('')
    print('Dependency')
    print('------------')
    for modui in ['monty', 'paramiko' ]:
        try:
            mm = __import__(modui)
            print('%10s %10s   %s' % (modui, mm.__version__, mm.__path__[0]))
        except ImportError:
            print('%10s %10s Not Found' % (modui, ''))
    print()

