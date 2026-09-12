# with open("/Prime 2.0 AI-ML/Python/File Handling/Log/log.txt", "a") as f:
#     data = f.write("Python executed successfully!!!")
# with open("/Prime 2.0 AI-ML/Python/File Handling/Log/log.txt", "r") as f:
#     data = f.read()
#     print(data)/

""" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """

lst_of_logs = [
    "Python executed successfully.\n",
    "Using high power libraries like pytorch, scikit-learn, TensorFlow etc provide effective intelligence.\n",
    "python throws error for incorrect syntax."
]
with open("/Prime 2.0 AI-ML/Python/File Handling/Log/log.txt","a") as f:
    f.writelines(lst_of_logs)
with open("/Prime 2.0 AI-ML/Python/File Handling/Log/log.txt", "r") as f:
    data = f.read()
    print(data)