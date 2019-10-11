# @author   David Spreekmeester <@aapit>
class Comment:
    id = None
    itemId = None
    content = ''

    def __init__(self, data: list):
        self.id         = data['id']
        self.itemId     = data['item_id']
        self.content    = data['content']
