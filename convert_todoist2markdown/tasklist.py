from todoist.api import TodoistAPI
from convert_todoist2markdown.task import Task
from convert_todoist2markdown.labellist import LabelList

class TaskList:
    api = None
    tasks = []
    labelList = None

    def __init__(self, api: TodoistAPI, labelList: LabelList):
        self.api = api
        self.labelList = labelList
        self._parseApiTasks(api)

    def render(self):
        for task in self.tasks:
            print(task.render(self.labelList))

    def filterUnchecked(self):
        tasks = []
        for task in self.tasks:
            if (task.checked == 0):
                tasks.append(task)
        self.tasks = tasks

    def filterByLabel(self, labelName: str):
        labelId = self.labelList.findIdByName(labelName)
        tasks = []
        for task in self.tasks:
            if (len(task.labelIds) == 0):
                continue
            if (not(labelId in task.labelIds)):
                continue
            tasks.append(task)
        self.tasks = tasks

    def _parseApiTasks(self, api: TodoistAPI):
        for taskData in api.state['items']:
            self.tasks.append(Task(taskData, api))
