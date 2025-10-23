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

