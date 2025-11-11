import json

def open_file():
    with open('jordartsdata.geojson', 'r', encoding="UTF-8") as file:
        data = json.load(file)

    geo_data_temp = []
    for key in data["features"]:
        geo_data_temp.append(key["properties"]["jg2_tx"].lower()) # Add coordinates to list

    return geo_data_temp


geo_data = open_file()