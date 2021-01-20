import json

class FileService:
    '''
        Contains methods responsible with handling files.
    '''
    def __init__(self, filepath):
        '''
            Configure the filepath for use in methods.
        '''
        self.filepath = filepath

    def read_appsettings(self):
        '''
            Reads the appsettings for use in the program.  
            Returns:
                appsettings: dictionary, containing the appsettings.
        '''
        try:
            with open(self.filepath, "r") as file_content:
                appsettings = json.load(file_content)
        except FileNotFoundError:
            print("Failed, file not found.")
        except PermissionError:
            print("Failed, file permissions error.")
            
        return appsettings