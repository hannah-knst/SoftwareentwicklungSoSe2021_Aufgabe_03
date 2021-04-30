import os

git_message = os.environ['MESSAGE']
git_user = os.environ['USER']

print(git_message)
print(git_user)

# The script replace actual task descriptions by copying content from individual task 
# files to a specific task sheet. 
# 
#     items                        README.md
#               Random Selection                           
#     +-----+   during fork        +-------------+
#   +-----+ |   operations         | General     |  constant
#   |     | | ----------+          | Information |
#   |     | |           |          +-------------+
#   |     |-+           +--------->| Variable    |
#   +-----+                        | Part        | 
#                                  +-------------+

import random 
import logging

items = [
    './.github/workflows/tasks/Variant_0.md',
    './.github/workflows/tasks/Variant_1.md'
]

readmefilename = "./README.md"
loggingfilename = "./.content/task.log"
splitingWords="## Aufgabenvariante"

taskname = random.sample(items,  1)[0]
print(taskname)

# Read from original README.md
with open(readmefilename, 'r') as readmefilehandle:
        readmecontent = readmefilehandle.read()

# Read actual task description
with open(taskname, 'r') as taskfilehandle:
        taskcontent = taskfilehandle.read()

newreadmecontent = readmecontent.split(splitingWords)[0] + taskcontent

# Write adapted README.md
with open(readmefilename, 'w') as readmefilehandle:
        readmefilehandle.write(newreadmecontent)

# Write task identifier to separate file
with open(loggingfilename, 'w') as loggingfilehandle:
        loggingfilehandle.write(taskname)
