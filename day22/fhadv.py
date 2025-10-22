with open("myfile.txt", "r") as f:
    print(type(f))
    f.seek(10) # move to 10th byte
    print(f.tell())#return current posn
    data = f.read(5) # read next 5 bytes
    print(data)
