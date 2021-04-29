import random 
import logging

items = [
    './TaskGenerator/Variant_0.md',
    './TaskGenerator/Variant_1.md'
]

readmefilename = "README.md"
loggingfilename = "./TaskGenerator/TaskHistory.log"

taskname = random.sample(items,  1)[0]
print(taskname)

with open(readmefilename, 'r') as readmefilehandle:
        readmecontent = readmefilehandle.read()

with open(taskname, 'r') as taskfilehandle:
        taskcontent = taskfilehandle.read()

newreadmecontent = readmecontent.split("## Aufgabenvariante")[0] + taskcontent

with open(readmefilename, 'w') as readmefilehandle:
        readmefilehandle.write(newreadmecontent)

logger = logging.getLogger('Task_History')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(loggingfilename)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.debug(taskname)
                
print("Aus die Maus!")
