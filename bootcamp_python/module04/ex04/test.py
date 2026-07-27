from FileLoader import FileLoader


loader = FileLoader()
data = loader.load('/home/clwenhaj/events.csv')

print(data.columns)
from SpatioTemporalData import SpatioTemporalData


sp = SpatioTemporalData(data)
print(sp.where(1896))

print(sp.when('Paris'))
