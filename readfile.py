# Problem: 1

def readfile(name):
    file = open(name,"r")
    return file.read()

if __name__== "__main__":
    filename = "20012024235627.txt"
    print(readfile(filename))