class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: object):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: object):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: object):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        if self.search(self.categories, category_id) is not None:
            category = self.search(self.categories, category_id)
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        if self.search(self.topics, topic_id) is not None:
            topic = self.search(self.topics, topic_id)
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        if self.search(self.documents, document_id) is not None:
            document = self.search(self.documents, document_id)
            document.file_name = new_file_name

    @staticmethod
    def search(iterable, id: int):
        for object in iterable:
            if object.id == id:
                return object

    def delete_category(self, category_id):
        if self.search(self.categories, category_id) is not None:
            category = self.search(self.categories, category_id)
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        if self.search(self.topics, topic_id) is not None:
            topic = self.search(self.topics, topic_id)
            self.topics.remove(topic)

    def delete_document(self, document_id):
        if self.search(self.documents, document_id) is not None:
            document = self.search(self.documents, document_id)
            self.documents.remove(document)

    def get_document(self, document_id):
        return self.search(self.documents, document_id)

    def __repr__(self):
        return f'{"".join(map(str, [document for document in self.documents]))}\n'
