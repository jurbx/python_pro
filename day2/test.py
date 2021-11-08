class File:
    def __init__(self, filename):
        self.name = filename


    def file_size(self):
        f = open(self.name)
        tmp = f.read()
        f.close()
        return len(tmp)


    def count_word(self):
        f = open(self.name)
        tmp = f.read()
        f.close()
        tmp = tmp.split()
        return f'Word in file {len(tmp)}'


print(File('text1.txt').count_word())