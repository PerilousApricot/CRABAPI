. venv/bin/activate
export PYTHONPATH=WMCore/src/python:CRABClient/src/python:CRABServer/src/python:$PYTHONPATH
cmsset
cd $(ls CMSSW_*|head -n1)/src
cmsenv
