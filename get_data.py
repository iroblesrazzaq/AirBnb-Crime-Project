import requests
import pandas as pd


# api_url = 'https://data.cityofchicago.org/resource/m6dm-c72p.json?$where=within_box(pickup_centroid_location, 41.795146, -87.606069, 41.784, -87.594741)&&$offset=0'
# #more than 780,000 but less than 790,000

# #pickup_centroid_latitude==41.9798553089&&pickup_centroid_longitude==-87.6940960217'


# #'https://data.cityofchicago.org/resource/m6dm-c72p.json?$where=pickup_centroid_latitude==41.9798553089&&pickup_centroid_longitude==-87.6940960217'

# #$where=pickup_community_area==41&&tip==0'
# #'https://data.cityofchicago.org/resource/m6dm-c72p.json?$where=pickup_centroid_latitude > 41.7930'

# response = requests.get(api_url)
# data = response.json()

# # print(type(data))
# # print(len(data))
# # print(data)

# t = pd.DataFrame.from_records(data)

# # print(t)
# # print(t[:0])
# # print(t.iloc[15:20,0:5].head())




# t.to_csv("csv2.csv", index=False)

# # api_url = 'https://data.cityofchicago.org/resource/m6dm-c72p.json?$where=within_box(pickup_centroid_location, 41.795146, -87.606069, 41.784, -87.594741)&&$offset=1000'
# # c = requests.get(api_url).json()
# # g = pd.DataFrame.from_records(c)
# # g.to_csv("fil", mode='a')

# t = pd.DataFrame()

# p = pd.read_csv("csv2.csv")

# print(p['pickup_centroid_location'])

api_url = 'https://data.cityofchicago.org/resource/m6dm-c72p.json?$where=within_box(pickup_centroid_location, 41.795146, -87.606069, 41.784, -87.594741)'
j = requests.get(api_url).json()
df = pd.DataFrame.from_records(j)
df.to_csv("fill2.csv", index=False, mode='w')

# counter = 1
for i in range(0, 1000000):
    api_url = 'https://data.cityofchicago.org/resource/m6dm-c72p.json?$where=within_box(pickup_centroid_location, 41.795146, -87.606069, 41.784, -87.594741)&&$offset='+str(1000*i)
    j = requests.get(api_url).json()
    df = pd.DataFrame.from_records(j)
    if len(j) == 0:
        break
    df.to_csv("fill2.csv", index=False, mode='a', header=False)
    # counter += 1