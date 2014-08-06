CRABAPI Design
==============

To make things as consistently and reproducibly testable as possble, functional
units that touch anything external are abstracted behind a layer of inderection,
this allows us to much more easily mock out client/server interactions. Where
needed, CRABClient will be modified to inject specific dependencies useful for
testing, but otherwise as little as possible will be changed in the client.

Desired Functionality
---------------------
This API is not intended to be a mere superset of the functionality provided by
CRABClient or CRABServer. It's easier to do a few things well than a lot of 
things well. To that end, this is the first functionality targeted.

* Task submission
  * Input python configuration (locally or via URL)
  * Input user library sandbox (locally or via URL)
  * Input crab configuration file (locally or in-memory)
* Task resubmission
  * Modify site white/blacklist
  * Select specific jobs
* Task status
  * Job status (compressing Job/ASO/Publication status into a single value)
  * Mapping various error codes into python classes (e.g. CMSSW error 8002 would
    become CRABAPI.CMSSWError(8002)) with helpers to compare lists
  * Output dataset
  * Output <units> published

Classes
-------
Ideally the surface area of the API should be as minimal as possible, while
still providing the necessary abstractions to the clients

* Task - A task nearly but doesn't 100% map to a CRAB3 task. A better definition
       would be "A task takes all or part of an input dataset, applies a user's
       configuration and stores the outputs on a SE". The distinction is that
       currently CRAB3 doesn't natively support things like extending datasets
       or resplitting tasks that were too coarsly split beforehand. A future
       extension of the API will merge multiple CRAB3 tasks behind the scenes
       into a single API-facing task.
  * Mutating methods
    * Submit
    * Resubmit
  * Informational methods
    * isComplete()
    * publishedData() - Lumimask (or similar) of published outputs
    * inputData() - Lumimask (or similar) of input to the task
    * failedData() - Lumimask (or similar) of terminally failed jobs
  * Prepopulated attributes
    * jobs - A generator returning every job in the task. This is a generator
             to eventually support pagination of CRAB status calls
    * failedJobs - Same as above, but returning jobs that have terminally failed
    * outputDataset
    * destinationSite
    * inputDataset
* Job - Directly maps to an individual job, including all the phases: execution,
        ASO, publication.
    * Mutating methods
      * Resubmit
    * Informational methods
      * didFail()

Convention
----------

* Properties of objects are exposed as regular attributes.
* Lists of jobs are exposed as generators and can be iterated over.
* The API will Do What I Mean (DWIM) for the most probable use cases.
* Round-trips to information services and handled and cached transparently by
  default.
