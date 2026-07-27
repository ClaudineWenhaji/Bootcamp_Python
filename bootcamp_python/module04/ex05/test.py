from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/clwenhaj/events.csv')


from HowManyMedalsByCountry import how_many_medals_by_country

print(data['Team'].head())

print(how_many_medals_by_country(data, 'Argentina'))
