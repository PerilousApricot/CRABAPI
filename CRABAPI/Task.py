""" Task - top-level Task class """
import CRABAPI.TopLevel
import CRABClient.Commands.submit
from WMCore.Configuration import ConfigSection
class Task(object):
    """
        Task - Wraps methods and attributes for a single analysis task
    """
    def __init__(self, submitClass = CRABClient.Commands.submit.submit):
        self.config = ConfigSection()
        self.apiLog, self.clientLog, self.tracebackLog = \
                CRABAPI.TopLevel.getAllLoggers()
        self.submitClass = submitClass

    def submit(self):
        """
            submit - Sends the current task to the server. Returns requestID
        """
        args = ['--debug.configInmemory', self.config, \
                '--skip-proxy','unittest-noproxy']
        submitCommand = self.submitClass(self.clientLog, args)
        return submitCommand()

    def kill(self):
        """
            kill - Tells the server to cancel the current task
        """
        raise NotImplementedError

    def __getattr__(self, name):
        """
            __getattr__ - expose certain values as attributes
        """
        if name == 'jobs':
            raise NotImplementedError
        else:
            raise AttributeError
