with open('file IO/myfile.txt', 'r') as f:
    print(type(f))
    
    #Move to the 10th byteof the file
    f.seek(10)
    
    #Read the next 5 bytes
    data = f.read(5)
    print(data)
    
# truncate the file to 20 bytes
with open('file IO/myfile.txt', 'w') as f:
    f.write("This is a sample file for testing.")
    f.truncate(20)
with open('file IO/myfile.txt', 'r') as f:
    data = f.read()
    print(data)