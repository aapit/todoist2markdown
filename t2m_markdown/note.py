# @author   David Spreekmeester <@aapit>
import datetime
import os
from t2m_todoist.task import Task
from t2m_todoist.labellist import LabelList


class Note:
    task = None

    def __init__(self, task: Task):
        self.task = task

    def render(self) -> str:
        template = open(os.getenv('NOTE_TEMPLATE_PATH'), 'r')

        getContent = lambda c: c.content
        commentFlatList = "\n\n".join(map(getContent, self.task.comments))

        return template.read().format(
            date        = self._extractSimpleDate(),
            author      = os.getenv('NOTE_AUTHOR'),
            tags        = ", ".join(self.task.labelNames),
            note        = self.task.content,
            comments    = commentFlatList
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

    def _extractSimpleDate(self) -> str:
        return ''.join([self.task.dateAdded[0:4],
                        self.task.dateAdded[5:7],
                        self.task.dateAdded[8:10]]
        )
