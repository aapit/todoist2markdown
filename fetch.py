from todoist.api import TodoistAPI
from convert_todoist2markdown.labellist import LabelList
from convert_todoist2markdown.tasklist import TaskList
from convert_todoist2markdown.note import Note

import os
from dotenv import load_dotenv
load_dotenv(override = True)

api = TodoistAPI(os.getenv('TODOIST_TOKEN'))
api.sync()

labelList = LabelList(api)
taskList = TaskList(api, labelList)
taskList.filterUnchecked()
taskList.filterByLabel('note')

print('Found ' + str(len(taskList.tasks)) + ' tasks labeled \'note\'.')

for task in taskList.tasks:
    note = Note(task, labelList)
    note.write()
    if (note.verifyWritten()):
        task.complete()

#----
#def filterByProp(items: list, prop: str, value: str) -> list:
#    for item in items:
#        if (item[prop] == value):
#            return item
#
#def findInboxId() -> int:
#    return filterByProp(api.state['projects'], 'name', 'Inbox')['id']
