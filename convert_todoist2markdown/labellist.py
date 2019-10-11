from todoist.api import TodoistAPI

class LabelList:
    labels = []

    def __init__(self, api: TodoistAPI):
        self.labels = api.state['labels']

    def findNameById(self, labelId: int) -> str:
        label = self._filterByProp(self.labels, 'id', labelId)
        return label['name']

    def findNamesByIds(self, labelIds: list) -> list:
        labelNames = []
        for labelId in labelIds:
            labelNames.append(self.findNameById(labelId))
        return labelNames

    def findIdByName(self, name: str) -> int:
        return self._filterByProp(self.labels, 'name', name)['id']

    def _filterByProp(self, items: list, prop: str, value: str) -> list:
        for item in items:
            if (item[prop] == value):
                return item
