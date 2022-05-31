class Topic:
    def __init__(self, id, topic, storage_folder):
        self.id: int = id
        self.topic: str = topic
        self.storage_folder: str = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"