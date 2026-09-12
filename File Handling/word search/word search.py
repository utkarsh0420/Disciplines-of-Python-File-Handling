# f = open("/Prime 2.0 AI-ML/Python/File handling/word search/sample.txt", "x")
data = True
word = input("Enter word to search from file :")
line = 1 # initialzed 1 for line count

with open("/Prime 2.0 AI-ML/Python/File handling/word search/sample.txt", "r") as f:
    while data:
        data = f.readline()

        if (word in data): 
            print(f"{word} found at line {line}")
            break

        line += 1 # increment by 1 after reading one line 
