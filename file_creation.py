# Problem: 2

import datetime;

def timestamp ():
    current_time = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    return current_time

def file_creation(filename):
    list = [filename,".txt"]
    string = "".join(list)
# Writing on the file
    file = open(string,"w")
    file.write(filename)
    return file


if __name__== "__main__":
    datetime = timestamp()
    file_creation(datetime)
