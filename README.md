CRABAPI
=======

Simple (almost minimal) wrapper API around the CRAB REST interface. The
intention isn't to provide a 1-to-1 mapping between CRABClient and
CRABAPI. The goal is to simply, efficiently and consistently implement the 
functionality most needed by those who would wish to script against the
CRABServer.

Usage
-----

First, a bit of example code:

```python
import CRABAPI as api

myTask = api.loadTask("task_id")
failedJobs = []
for job in myTask.jobs:
    if job.didFail() and job.failureReason == "blah":
        failedJobs.append(job)
if failedJobs:
    myTask.resubmit(failedJobs)
```

There are a few important things to note about the idioms and conventions
that will hold throughout the API:

* Properties of objects are exposed as regular attributes
* Lists of jobs are exposed as generators and can be iterated over
* The API will Do What I Mean (DWIM) for the most probable use cases (e.g. there
  is no need to tell the API where the current proxy is, it assumes to look in
  the default locations)
* Round-trips to information services are handled and cached transparently by
  default

Classes Provided
----------------

### Task

A task is an instruction to execute a user-provided python configuration file 
within (optionally) the user-provided environment, store the output at a desired 
target site, and publish the output in DBS.

### Job

A job is a unit of work within a task, the number of which are controlled by the
combination of the input dataset, (optional) lumi mask, and job splitting
algorithm.

Contributions
-------------

Contributions to this project need to fit the [DMWM coding standards](https://github.com/dmwm/WMCore/blob/master/standards/.pylintrc) as well as have test coverage that covers any updated
lines of code. Executing ```bin/check-commit.sh``` will let you know if your
working area passes muster. Code that doesn't 100% fit within the pylint
rules or have 100% test coverage will not be accepted.

One note: Since the conception of WMCore, it has become more common for test
cases to be named ```test_foo``` instead of ```foo_t```, and common testing
tools have all begun to require that naming scheme. To that end, tests should
be within the regular source tree and have their file/class names prefixed with
``` test_ ```
