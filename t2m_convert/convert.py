from t2m_todoist.tasklist import TaskList
from t2m_markdown.note import Note


class ConvertTrigger:
    tag     = None

    def __init__(self, tag: str):
        self.tag = tag

    def matches(self, taskList: TaskList) -> TaskList:
        return taskList.filterOpen().filterByLabel(self.tag)

class ConvertAction:
    dir             = None
    appendFilename  = None

    def __init__(self, dir: str, appendFilename: str = None):
        self.dir            = dir
        self.appendFilename = appendFilename

    def run(self, matchingList: TaskList):
        for task in matchingList.tasks:
            note = Note(task, self.dir, self.appendFilename)
            note.write()
            if (note.hasFileContent()):
                task.complete()

class ConvertRoutine:
    trigger = None
    action  = None

    def __init__(self, trigger: ConvertTrigger, action: ConvertAction):
        self.trigger    = trigger
        self.action     = action
