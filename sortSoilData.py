import json

def openJson():
    pass
 #   try:
#        with open('jordartsdata.geojson', 'w', encoding='utf-8') as fil:

def swe_soil_type_to_eng_soil_type(data_list):
    for item in range(len(data_list)):
        match data_list[item]:
            case "moran med lag halt av finkornigt material" \
            "svallad moran" \
            "mycket stenig och blockig moran" \
            "vittringsjord":
                return "sandy loam"

            case "lera-silt, tidvis under vatten" \
            "svamsediment, ler-silt":
                return "silty clay loam"

            case "svamsediment" \
            "moran omvaxlande med sorterade sediment" \
            "osorterat material, grovt-fint" \
            "osorterat material, ospecificerat":
                return "varierande"

            case "gyttja":
                return "silty clay"

            case "svamsediment, grovsilt-finsand":
                return "silt loam"

            case "svamsediment, sand":
                return "sand"

            case "moran, ospecificerad":
                return "loam"

            case "moran med hog halt av finkornigt material":
                return "clay loam"

            case "torv" \
            "mossetorv" \
            "karrtorv" \
            "bleke och kalkgyttja" \
            "kalktuff" \
            "torv, tidvis under vatten" \
            "oklassat omrade, tidvis under vatten" \
            "flytjord eller skredjord" \
            "slamstromssediment, ler-block" \
            "talus" \
            "isälvssediment, sten-block" \
            "kalfjall" \
            "kulturlager" \
            "utfyllnad":
                return None


def convert_data_to_numeric(soil_type_data_json):
    for soil_texture in soil_type_data_json:
        match soil_texture:
            case "Clay":
                return [316.3, 0.3, 0.27]
            case "Silty Clay":
                return [292.2, 0.5, 0.29]
            case "Sandy Clay":
                return [239.0, 0.6, 0.22]
            case "Clay Loam":
                return [208.8, 1.0, 0.21]
            case "Silty Clay Loam":
                return [273.0, 1.0, 0.30]
            case "Sandy Clay Loam":
                return [218.5, 1.5, 0.02]
            case "Silt Loam":
                return [166.8, 3.4, 0.34]
            case "Loam":
                return [88.9, 7.6, 0.30]
            case "Sandy Loam":
                return [110.1, 10.9, 0.29]
            case "Loamy Sand":
                return [61.3, 29.9, 0.28]
            case "Sand":
                return [49.5, 117.8, 0.29]
            case _:
                return None


test_list = [["clay"],["clay"],["clay"]]
test_list = convert_data_to_numeric(test_list)

print(test_list)

