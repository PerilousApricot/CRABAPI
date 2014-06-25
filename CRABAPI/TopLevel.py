""" Module storing top-level functions that are exported to the CRABAPI
    package. These functions can also be accessed from CRABAPI.<name>"""

def getTask(taskName):
    """ Given a task name, initialize a task object"""
    taskName += "test"
    raise NotImplementedError("Need to implement this: Load %s" % taskName)
