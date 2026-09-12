with open("/Prime 2.0 AI-ML/Python/File Handling/read/names.txt", "w") as f:
    data = f.write("Python\n")
    data = f.write("Artificial Intelligence\n")
    data = f.write("Machine Learning\n")
    data = f.write("Deep Learning - Neural Networks\n")
    data = f.write("Utkarsh Nikam\n")
with open("/Prime 2.0 AI-ML/Python/File Handling/read/names.txt", "r") as f:
    data = f.read()
    print(data)