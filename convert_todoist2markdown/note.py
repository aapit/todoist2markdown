import datetime
import os
from convert_todoist2markdown.task import Task
from convert_todoist2markdown.labellist import LabelList

class Note:
    task = None
    allLabels = None

    def __init__(self, task: Task, allLabels: LabelList):
        self.task = task
        self.allLabels = allLabels

    def render(self) -> str:
        template = open('./template.md', 'r')
        labelNames = self.allLabels.findNamesByIds(self.task.labelIds)
        date = ''.join([self.task.dateAdded[0:4],
                        self.task.dateAdded[5:7],
                        self.task.dateAdded[8:10]]
        )
        author = os.getenv('NOTE_AUTHOR')
        return template.read().format(
            date    = date,
            author  = author,
            tags    = ", ".join(labelNames),
            note    = self.task.content
        )

    def getFileSafeName(self):
        limit = 100
        words = self.task.content.split(' ')[:7]
        name = ' '.join(words)[0:100]
        name = name.strip('.')

        keepchars = (' ','.','_')
        return "".join(
            c for c in name if c.isalnum() or c in keepchars
        ).rstrip()

    def getFilename(self):
        return self.getFileSafeName() + '.md'

    def getPath(self):
        return os.getenv('NOTE_FOLDER') + '/' + self.getFilename()

    def write(self):
        with open(self.getPath(), "w") as f:
            f.write(self.render())

    def verifyWritten(self):
        size = os.path.getsize(self.getPath())
        return size > 0
