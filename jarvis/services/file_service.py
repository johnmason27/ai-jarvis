import json

class FileService:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_appsettings(self):
        with open(self.filepath, "r") as file_content:
            appsettings = json.load(file_content)
        return appsettings