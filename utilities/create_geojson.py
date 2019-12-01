import csv, json
from geojson import Feature, FeatureCollection, Point

features = []
with open('../data2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader,None)
    for row in reader:
        # print(row[0])
        latitude, longitude = map(float, (row[1], row[0]))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'Unique_Squirrel_ID': row[2],
                }
            )
        )

collection = FeatureCollection(features)
with open("../map/static/map/GeoObs3.geojson", "w") as f:
    f.write('%s' % collection)
