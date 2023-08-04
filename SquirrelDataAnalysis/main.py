# https://data.cityofnewyork.us/Environment/2018-Squirrel-Census-Fur-Color-Map/fak5-wcft
#DATA ANALYSIS
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur1_count = len(data[data["Primary Fur Color"] == "Gray"])
fur2_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
fur3_count = len(data[data["Primary Fur Color"] == "Black"])

# creating dataframe
data_dict = {"Primary fur color": ["Gray", "Cinnamon", "Black"], "Count": [fur1_count, fur2_count, fur3_count]}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("RecordFile.csv")