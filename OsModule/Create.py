import os
# Create a new directory

os.mkdir('OsModule/new_director')

for i in range(3):
    os.mkdir(f"OsModule/new_director/Day_{i+1}")
    

print(os.getcwd())