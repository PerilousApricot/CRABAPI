"""
    CRABAPI.RawCommand - wrapper if one wants to simply execute a CRAB command
        but doesn't want to subprocess.Popen()
"""
import CRABAPI
import logging

# NOTE: Not included in unittests
def execRaw(command, args):
    """
        execRaw - executes a given command with certain arguments and returns
                  the raw result back from the client
    """
    logger = logging.getLogger('CRAB3')

    try:
        mod = __import__('CRABClient.Commands.%s' % command, fromlist=command)
    except ImportError:
        raise CRABAPI.BadArgumentException( \
                                        'Could not find command "%s"' % command)

    try:
        cmdobj = getattr(mod, command)(logger, args)
        res = cmdobj()
    except SystemExit, se:
        # most likely an error from the OptionParser in Subcommand.
        # CRABClient #4283 should make this less ugly
        if se.code == 2:
            raise CRABAPI.BadArgumentException
    return res
