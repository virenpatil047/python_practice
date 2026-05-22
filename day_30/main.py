try:
    file = open("data.txt")
    
except FileNotFoundError:
    print("File not found")

else:
    content = file.read()
    print(content)

finally:
    print("Execution completed")