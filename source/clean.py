# Cleaning utility. Cleans source CSV keys and values in the CSV file to exlude \" characters

def clean_key(key):
    key = key.replace("ï»¿", "")
    key = key.replace("/", "_")
    key = key.replace(" ", "_")
    key = key.replace("Latitude", "lat")
    key = key.replace("Longitude", "long")
    key = key.replace("Incidence_Rate", "incident_rate")
    key = key.replace("Case-Fatality_Ratio", "case_fatality_ratio")

    if key == "Long_":
        key = "Long"
    return key.lower()

def clean_value(value):
    value = value.replace(", ", "-")
    value = value.replace(",", "-")
    if "''" not in value:
        value = value.replace("'", "''")
    return value

def create_combined_key(province_state, country_region):
    if province_state != "":
        return "{}-{}".format(clean_value(province_state), clean_value(country_region))
    else:
        return clean_value(country_region)
