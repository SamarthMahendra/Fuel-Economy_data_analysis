import requests



url = 'https://raw.githubusercontent.com/DrUzair/MLSD/master/Datasets/vehicles.csv'

def get_data(url):
    response = requests.get(url)
    return response.text

data = get_data(url)
# save as csv
with open('vehicles.csv', 'w') as f:
    f.write(data)



