# @author   David Spreekmeester <@aapit>
from todoist.api import TodoistAPI
from t2m_todoist.labellist import LabelList
from t2m_todoist.tasklist import TaskList
from t2m_markdown.note import Note
import os
from dotenv import load_dotenv


load_dotenv(override = True)
api = TodoistAPI(os.getenv('TODOIST_TOKEN'))
api.sync()

labelList = LabelList(api)
taskList = TaskList(api, labelList).filterOpen().filterByLabel('note')

print('Found ' + str(len(taskList.tasks)) + ' tasks labeled \'note\'.')
for task in taskList.tasks:
    note = Note(task)
    note.write()
    if (note.verifyWritten()):
        task.complete()
