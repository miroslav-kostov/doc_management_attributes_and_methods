from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        try:
            current_category = [category for category in self.categories if category.id == category_id][0]
            if current_category:
                current_category.name = new_name
        except:
            pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        try:
            current_topic = [topic for topic in self.topics if topic.id == topic_id][0]
            if current_topic:
                current_topic.topic = new_topic
                current_topic.storage_folder = new_storage_folder
        except:
            pass

    def edit_document(self, document_id: int, new_file_name: str):
        try:
            current_doc = [doc for doc in self.documents if doc.id == document_id][0]
            if current_doc:
                current_doc.file_name = new_file_name
        except:
            pass

    def delete_category(self, category_id):
        try:
             current_category = [category for category in self.categories if category.id == category_id][0]
             if current_category:
                 self.categories.remove(current_category)
        except:
            pass

    def delete_topic(self, topic_id):
        try:
            current_topic = [topic for topic in self.topics if topic.id == topic_id][0]
            if current_topic:
                self.topics.remove(current_topic)
        except:
            pass

    def delete_document(self, document_id: int):
        try:
            current_doc = [doc for doc in self.documents if doc.id == document_id][0]
            if current_doc:
                self.documents.remove(current_doc)
        except:
            pass

    def get_document(self, document_id):
        try:
            current_doc = [doc for doc in self.documents if doc.id == document_id][0]
            if current_doc:
                return current_doc
        except:
            pass

    def __repr__(self):
        res = ""
        for doc in self.documents:
            res += repr(doc) + "\n"
        return res

