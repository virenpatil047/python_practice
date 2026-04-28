# file = open("my_file.txt")
# data = file.read()
# print(data)
# file.close()

# with open("new_file.txt", "a") as file:
#     file.write("New content")
    
with open("new_file.txt", "r") as file:
    content = file.read()
    print(int(content))