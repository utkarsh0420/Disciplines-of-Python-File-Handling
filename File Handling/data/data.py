try:
    with open("/Prime 2.0 AI-ML/Python/File Handling/data/data.txt","r") as f:
        print(f.read())
except FileNotFoundError:  # FileNotFoundError - Exception
    print("File not found")
finally:
    print("Python is case sensitive language")
    