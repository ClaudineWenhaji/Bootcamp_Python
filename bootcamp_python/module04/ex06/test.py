from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/clwenhaj/events.csv')


from MyPlotLib import MyPlotLib

ploter = MyPlotLib()
#ploter.histogram(data, ['Height', 'Weight'])
#ploter.density(data, ['Height', 'Weight', 'City'])

ploter.box_plot(data, ['Height', 'Weight'])

ploter.pair_plot(data, ['Height', 'Weight'])
