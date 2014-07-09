""" Module storing top-level functions that are exported to the CRABAPI
    package. These functions can also be accessed from CRABAPI.<name>"""

import logging

API_LOGGER_NAME = 'CRAB3.CRABAPI'

def getTask(taskName):
    """ Given a task name, initialize a task object"""
    taskName += "test"
    raise NotImplementedError("Need to implement this: Load %s" % taskName)

def setLogging(apiLevel = logging.INFO,
                crabLevel = 100,
                crabTracebackLevel = 100):
    """Set logging parameters. Mutes the CRAB client by default.

      returns apiLogger"""
    crabLog = logging.getLogger('CRAB3')
    crabTracebackLog = logging.getLogger('CRAB3:traceback')
    apiLog = logging.getLogger(API_LOGGER_NAME)

    apiLog.setLevel(apiLevel)
    crabLog.setLevel(crabLevel)
    crabTracebackLog.setLevel(crabTracebackLevel)

    return apiLog

def getLogger():
    """ Helper function to get the logger back """
    return logging.getLogger(API_LOGGER_NAME)
