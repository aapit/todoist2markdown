# @author   David Spreekmeester <@aapit>
from todoist.api import TodoistAPI

class LabelList:
    labels = []

    def __init__(self, api: TodoistAPI):
        self.labels = api.state['labels']

    def findNamesByIds(self, labelIds: list) -> list:
        labelNames = []
        for labelId in labelIds:
            labelNames.append(self._findNameById(labelId))
        return labelNames

    def findIdByName(self, name: str) -> int:
        matchesLabel    = lambda l: l['name'] == name
        foundLabel      = list(filter(matchesLabel, self.labels))
        if len(foundLabel):
            return foundLabel[0]['id']

    def _findNameById(self, labelId: int) -> str:
        matchesLabel    = lambda l: l['id'] == labelId
        foundLabel      = list(filter(matchesLabel, self.labels))
        if len(foundLabel):
            return foundLabel[0]['name']
