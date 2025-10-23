import json

def openJson():
    pass
 #   try:
#        with open('jordartsdata.geojson', 'w', encoding='utf-8') as fil:

def swe_soil_type_to_eng_soil_type(data_list):
    for item in range(len(data_list)):
        match data_list[item]:
            case"Torv":
                data_list[]



def convert_data_to_numeric(soil_type_data_json):
    # soil_type_data_json 2D list with soil types as the rows and the numerical values for that soil type as the columns
    for section in soil_type_data_json:

        # return = [soil Suction Head(ssh), Hydraulic Conductivity, Porosity]
        match section:
            case "clay":
                soil_type_data_json[section].append([2,5,6])
                break


    return soil_type_data_json


test_list = [["clay"],["clay"],["clay"]]
test_list = convert_data_to_numeric(test_list)

print(test_list)

