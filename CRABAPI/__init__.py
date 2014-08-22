""" CRABAPI - https://github.com/PerilousApricot/CRABAPI
    Normally I keep __init__.py blank, but this is a but of delicious
    syntactic sugar for some common operations"""

from CRABAPI.TopLevel import getTask, setLogging, getAllLoggers, getLogger

__all__ = ["getTask", "setLogging", "getAllLoggers", "getLogger"]

def setUpPackage():
    """ Need to make sure logging is initialized before any tests run. This
        should NOT be called by client functions, it is used by the testing
        suite """
    import logging
    setLogging(logging.DEBUG, logging.DEBUG, logging.DEBUG)
