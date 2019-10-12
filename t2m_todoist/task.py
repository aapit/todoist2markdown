from todoist.api import TodoistAPI
from t2m_todoist.comment import Comment
from t2m_todoist.labellist import LabelList


class Task:
    api             = None
    id              = None
    content         = ''
    labelIds        = []
    labelNames      = []
    dateAdded       = None
    dateCompleted   = None
    checked         = None
    comments        = []

    def __init__(self, taskData: list, api: TodoistAPI, allLabels: LabelList):
        self.api            = api
        self.id             = taskData['id']
        self.content        = taskData['content']
        self.labelIds       = taskData['labels']
        self.dateAdded      = taskData['date_added']
        self.checked        = taskData['checked']
        self.dateCompleted  = taskData['date_completed']
        self.comments       = self._loadComments()
        self.labelNames     = self._loadLabelNames(allLabels)

    def complete(self):
        item = self.api.items.get_by_id(self.id)
        item.close()
        self.api.commit()
        print('— Completed task #' + str(self.id))
        print("\t" + self.content[0:80])

    def _loadComments(self) -> list:
        comments = []
        allCommentData = self.api.state['notes']
        itemCommentData = list(
            filter(lambda n: n['item_id'] == self.id, allCommentData)
        )

        for commentData in itemCommentData:
            comments.append(Comment(commentData))
        return comments

    def _loadLabelNames(self, allLabels: LabelList) -> list:
        return allLabels.findNamesByIds(self.labelIds)
