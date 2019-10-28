# @author   David Spreekmeester <@aapit>
import datetime
import os
from t2m_todoist.task import Task
from t2m_markdown.notefilewriter import NoteFileWriter


class Note:
    task            = None
    appendFilename  = None # If provided, content will be added to existing note
    author          = None
    templatePath    = None
    content         = None
    writer          = None

    def __init__(self, task: Task, directory: str, appendFilename = None):
        self.task           = task
        self.appendFilename = appendFilename
        self.author         = os.getenv('NOTE_AUTHOR')
        self.templatePath   = os.getenv('NOTE_TEMPLATE_PATH')
        self.content        = self._getContent()
        renderedContent     = self._render()
        self.writer         = self._createWriter(directory, renderedContent)

    def write(self) -> None:
        self.writer.write()

    def hasFileContent(self) -> bool:
        return self.writer.hasFileContent()

    def _createWriter(self, directory: str, renderedContent: str) -> NoteFileWriter:
        filenameHint        = self.task.content if not self.appendFilename else None
        return NoteFileWriter(directory, renderedContent,
            appendFilename = self.appendFilename,
            name = filenameHint)

    def _render(self) -> str:
        template    = open(self.templatePath, 'r').read()
        tags        = ", ".join(self.task.labelNames)
        date        = self._extractSimpleDate()
        content     = self.content

        if (self.appendFilename):
            return "\n\n## " + date \
                + "\n" + ('-' * 50) \
                + "\n" \
                + content
        return template.format(
            date        = date,
            author      = self.author,
            tags        = tags,
            content     = content
        )

    # Returns the pure textual content,
    # consisting of task description and comments
    def _getContent(self) -> str:
        content = self.task.content
        if (len(self.task.comments)):
            content += "\n\n" + self._getCommentFlatList()
        return content

    def _getCommentFlatList(self) -> str:
        getComment   = lambda c: c.content
        return "\n\n".join(map(getComment, self.task.comments))

    def _extractSimpleDate(self) -> str:
        d = self.task.dateAdded
        return ''.join([d[0:4], d[5:7], d[8:10]])
