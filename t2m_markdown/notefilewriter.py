from pathlib import Path
import os


class NoteFileWriter:
    directory       = None
    content         = None
    appendFilename  = None
    name            = None

    def __init__(self, directory: str, content: str,
        appendFilename: str = None, name: str = None):

        self.directory      = directory
        self.content        = content
        self.appendFilename = appendFilename
        self.name           = name

    def write(self):
        flag = ('a' if self.appendFilename else 'w')
        shortPath = self._getShortPath()

        if (self.appendFilename):
            print('Appending to', shortPath)
        else:
            print('Creating', shortPath)

        with open(self._getPath(), flag) as f:
            f.write(self.content)

    def hasFileContent(self) -> bool:
        size = os.path.getsize(self._getPath())
        return bool(size > 0)

    def _getShortPath(self) -> str:
        return Path(*Path(self._getPath()).parts[-3:])

    def _getFileSafeName(self):
        if (self.appendFilename):
            return appendFilename

        assert(len(self.name) > 0)
        limit = 100
        words = self.name.split(' ')[:7]
        name = ' '.join(words)[0:100]
        name = name.strip('.')

        keepchars = (' ','.','_')
        return "".join(
            c for c in name if c.isalnum() or c in keepchars
        ).rstrip()

    def _getFilename(self) -> str:
        if (self.appendFilename):
            return self.appendFilename
        return self._getFileSafeName() + '.md'

    def _getPath(self):
        return (self.directory + '/' + self._getFilename()).replace('//', '/')
