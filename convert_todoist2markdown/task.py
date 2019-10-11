from todoist.api import TodoistAPI

class Task:
    api = None
    id = None
    content = ''
    labelIds = []
    dateAdded = None
    checked = None

    def __init__(self, taskData: list, api: TodoistAPI):
        self.api        = api
        #print(apiData)
        self.id         = taskData['id']
        self.content    = taskData['content']
        self.labelIds   = taskData['labels']
        self.dateAdded  = taskData['date_added']
        self.checked    = taskData['checked']

    def complete(self):
        item = self.api.items.get_by_id(self.id)
        item.complete()
        self.api.commit()
        print('— Completed task')
        print("\t" + self.content[0:80])
