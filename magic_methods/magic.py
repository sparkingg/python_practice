import os
import tempfile
class File:
    def __init__(self, path_to_file):
        if os.path.exists(path_to_file):
            self.path_to_file = path_to_file
        else:
            self.path_to_file = path_to_file
            with open(self.path_to_file, 'w'):
                pass
    def __str__(self):
        return self.path_to_file
    def __iter__(self):
        obj = yield from open(self.path_to_file)
        return obj

    def read(self):
        with open(self.path_to_file) as f:
            file = f.read()
            return file

    def write(self, text):
        with open(self.path_to_file, 'w') as f:
            f.write(text)
            return f
    

    def __add__(self, file2):
        with open(self.path_to_file, 'r') as f:
            text_file1 = f.read()
        with open(file2.path_to_file, 'r') as d:
            text_file2 = d.read()
            random_path = tempfile.mkstemp()[1]
        new_path_to_file = os.path.join(tempfile.gettempdir(), random_path)
        text_file3 = text_file1 + text_file2
        with open(new_path_to_file, 'w') as g:           
            g.write(text_file3)
        exit_file = File(new_path_to_file)
        exit_file.path_to_file = new_path_to_file
        return exit_file
