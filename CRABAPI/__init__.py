""" CRABAPI - https://github.com/PerilousApricot/CRABAPI
    Normally I keep __init__.py blank, but this is a but of delicious
    syntactic sugar for some common operations"""

from CRABAPI.TopLevel import getTask, setLogging, getAllLoggers

__all__ = ["getTask", "setLogging", "getAllLoggers"]
