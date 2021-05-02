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

import os
import random 

git_message = os.environ['MESSAGE']
git_user = os.environ['USER']

githubbotname = "github-classroom[bot]"
readmefilename = "./README.md"
loggingfilename = "./.content/task.log"
splitingWords="## Aufgabenvariante"

print(git_message)
print(git_user)

if git_user != githubbotname:
  print("This is not an initial commit")

if git_user == githubbotname:

  items = [
    './.content/tasks/Variant_0.md',
    './.content/tasks/Variant_1.md'
  ]
   
  # Select task file
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
    loggingfilehandle.write(taskname.split('/')[-1])
 