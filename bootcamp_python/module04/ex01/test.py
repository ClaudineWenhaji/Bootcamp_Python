from FileLoader import FileLoader
from YoungestFellah import youngest_fellah


loader = FileLoader()
data = loader.load('/home/clwenhaj/events.csv')

print(youngest_fellah(data, 2004))
