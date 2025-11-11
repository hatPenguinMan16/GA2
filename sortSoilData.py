import json
from rFile import geo_data

def swe_soil_type_to_eng_soil_type(data_list):
    temp_data_list = [] # See if dict-comps can be used.
    conv = {
        "gyttja": "silty clay",
        "sand": "sand",
        "morän med hög halt av finkornigt material": "clay loam",
        "svamsediment, grovsilt-finsand": "silt loam",
        "morän, ospecificerad": "loam"
    }

    for i in ("moran med lag halt av finkornigt material", "svallad moran", "mycket stenig och blockig moran", "vittringsjord"):
        conv[i] = "sandy loam"
    for i in ("lera-silt, tidvis under vatten", "svamsediment, ler-silt"):
        conv[i] = "silty clay loam"
    for i in ("svamsediment", "morän omvaxlande med sorterade sediment", "osorterat material, grovt-fint", "osorterat material, ospecificerat", "svamsediment", "morän omvaxlande med sorterade sediment", "osorterat material, grovt-fint", "osorterat material, ospecificerat", "morän"):
        conv[i] = "NONE"


    for item in data_list:
        if item in conv:
            temp_data_list.append((conv[item]))
        else:
            continue

    for item in temp_data_list:
        if item == "NONE":
            temp_data_list.remove(item)
    return temp_data_list



def convert_data_to_numeric(char_geo_data):
    temp_num_geo_data = []
    num_conv = {"clay": [316.3, 0.3, 0.27],
                "silty clay": [292.2, 0.5, 0.29],
                "sandy clay": [239.0, 0.6, 0.22],
                "clay loam": [208.8, 1.0, 0.21],
                "silty clay loam": [273.0, 1.0, 0.30],
                "sandy clay loam": [218.5, 1.5, 0.02],
                "silt loam": [166.8, 3.4, 0.34],
                "sandy loam": [110.1, 10.9, 0.29],
                "loam": [88.9, 7.6, 0.30],
                "loamy sand": [61.3, 29.9, 0.28],
                "sand": [49.5, 117.8, 0.29]}
    for item in char_geo_data:
        if item in num_conv:
            temp_num_geo_data.append((num_conv[item]))
    return temp_num_geo_data


temp_geo_data = swe_soil_type_to_eng_soil_type(geo_data)
print(temp_geo_data)
a = convert_data_to_numeric(temp_geo_data)
print(a)


