def openFile(file):
    with open(file, 'r') as f:
        return f.read()

def writeFile(file, text):
    with open(file, 'w') as f:
        f.write(text)