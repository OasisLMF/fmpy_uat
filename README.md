# fmpy_uat
This repository is intended to hold the assets required for the UAT process for the fmpy developments introduced in oasislmf version 1.15

---

## MDK

Note that the version of the oasislmf to be tested in UAT is 1.15.6 and can be installed using the command 

> pip install oasislmf==1.15.6

The usual minimum requirements and dependencies exist for the package and can be found in the oasislmf repository at [oasislmf](https://github.com/OasisLMF/OasisLMF#minimum-python-requirements)

The test exposure files to be used can be found in the `exposures` directory of the repository, and the expected results for these files are in the `results` directory.

From version 1.15 onwards, fmpy is the default financial module which will be used in oasislmf, and so no flag is needed to use it. To test the previous fmcalc version, the flag ```-fmpy false``` should be used when running the MDK, which will fall back to the previous package

> oasislmf model run --config oasislmf.json –fmpy false

---

## Docker

The repository also allows you to spin up a deployed version of the model using the Oasis platform, and in this case the platform will contain two versions of the model – one with fmcalc and one with fmpy


To start the environment, you should run 

> docker-compose -f docker-compose-platform.yml -f docker-compose-worker.yml -f docker-compose-UI.yml up -d

And the UI will be available at 

> localhost:8080

---
