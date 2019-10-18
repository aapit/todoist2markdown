# @author   David Spreekmeester <@aapit>
from todoist.api import TodoistAPI
from t2m_todoist.task import Task
from t2m_todoist.labellist import LabelList


class TaskList:
    api = None
    tasks = None
    allLabels = None # A list of all labels in use

    def __init__(self, api: TodoistAPI, allLabels: LabelList):
        self.api = api
        self.tasks = []
        self.allLabels = allLabels
        self._parseApiTasks(api)

    # Only fetch incomplete tasks
    def filterOpen(self):
        tasks = []
        for task in self.tasks:
            if (task.dateCompleted == None):
                tasks.append(task)
        self.tasks = tasks
        return self

    # Only fetch tasks with label
    def filterByLabel(self, labelName: str):
        labelId = self.allLabels.findIdByName(labelName)
        tasks = []
        for task in self.tasks:
            if (len(task.labelIds) == 0):
                continue
            if (not(labelId in task.labelIds)):
                continue
            tasks.append(task)
        self.tasks = tasks
        return self

    def _parseApiTasks(self, api: TodoistAPI):
        for taskData in api.state['items']:
            self.tasks.append(Task(taskData, api, self.allLabels))
