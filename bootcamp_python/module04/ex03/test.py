from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/clwenhaj/events.csv')


from HowManyMedals import how_many_medals
print(how_many_medals(data, 'Kjetil Andr Aamodt'))
