import time
import csv
import json
from MongoAPI import MongoAPI

def batch(iterable, n=1):
    l = len(iterable)
    c = 0
    for b in range(0, l, n):
        c+=1
        print(f'Batch {c} of {l/n}')
        yield iterable[b:min(b + n,l)]

with open('data/worldcities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = {"database": "MikesDB", "collection": "places", "Document": []}
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            city = { "city": row[0], "lat": row[2], "lon": row[3] }
            print(json.dumps(city))
            line_count += 1
            data["Document"].append(city)
    print(f'Processed {line_count} lines.')
    client = MongoAPI(data)
    for cities in batch(data["Document"], 100):
        client.collection.insert_many(cities)
        time.sleep(0.5)
