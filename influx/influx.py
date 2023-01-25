import pandas as pd
from influxdb import DataFrameClient


client = DataFrameClient('localhost', 8086, 'Swarmbots')
client.create_database('SwarmbotsDB')
client.get_list_database()
client.switch_database('SwarmbotsDB')

Fields = ['X','Y','Theta','Timestamp']


for i in range(1):
    path = 'Robot'+ str(i) + '.csv'
    df = pd.read_csv(path, parse_dates=['Timestamp'], usecols=Fields)
    print(df.head())
    data = df.set_index(['Timestamp'])
    print(data)
    data.index = pd.to_datetime(data.index, unit='s')
    print(data)
    client.write_points(data,"Bot"+str(i)+"Coordinates",protocol='line')

