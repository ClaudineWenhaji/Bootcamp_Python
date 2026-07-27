from FileLoader import FileLoader


loader = FileLoader()
data = loader.load("/home/clwenhaj/image.csv")

loader.display(data, 12)
print(data.columns)
print(data['Sex'])
