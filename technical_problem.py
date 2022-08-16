from distance_formula import distance as dis_form  # format for input: (lat1, lat2, lon1, lon2)
from operator import itemgetter
from math import radians, cos, sin, asin, sqrt


customer_list = 'customer_list.txt'

def open_txt(file_path):
    """
    Open text file and configure to a list of nested lists with information. 
    Sorts the information into the desired order of columns.
    """
    data_list = []
    nested_list = []

    with open(file_path, 'r') as file_in:
        reader = file_in.readlines()
        for row in reader:
            row = row[2:-3]
            nested_list = row.split(",")
            data_list.append(nested_list)
            
        new_list = data_list
        for list in new_list:
            list.insert(3, list[0])
            del list[0]

        for list in new_list:
            for item in list:
                if item[0] == " ":
                    item = item[1:]
                if item[1] == " ":
                    item = item[2:]

    return new_list


data_import = open_txt(customer_list)

# print("initial read", data_import)
# print(data_import[0][0])

def create_dictionary(data_list):
    """
    Creates a dictionary of the list information for easier access
    """
    new_list = []
    for item in data_list:
        try:
            temp_dict = {}
            temp_dict["user_id"] = int(item[0][10:])
            temp_dict["name"] = str(item[1][8:-1])
            temp_dict["latitude"] = float(item[2][11:-1])
            temp_dict["longitude"] = float(item[3][13:-1])
        except ValueError or KeyError:
            print("Invalid Input")    
        
        else:
            new_list.append(temp_dict)
    
    return new_list

working_data = create_dictionary(data_import)
sorted_data = sorted(working_data, key=itemgetter('user_id'))  # sorts the list in ascending order by user_id


def detect_dups(list_of_dicts):

    temp_list = []
    for dict in list_of_dicts:
        if dict["user_id"] in temp_list:
            print(dict["user_id"], dict["name"], ": User ID already in use. Please use a unique user ID.")
        else:
            temp_list.append(dict["user_id"])
    
    temp_list_2 =[]
    for dict in list_of_dicts:
        if dict["name"] in temp_list_2:
            print(dict["user_id"], dict["name"], ": Name already in use. Please use a unique user ID.")
        else:
            temp_list_2.append(dict["name"])

    return "Duplicate testing complete"

# duplicate_test = detect_dups(sorted_data)

sf_lat = 37.7866
sf_lon = -122.41284

# dis_form, format for input: (lat1, lat2, lon1, lon2)

def distance_calc(data_list):
    """
    Distance is calcualted and added as a key to each dictionary.
    Separates infrmation into one of two new lists for invited and one for not invited based on distance (and formattings).
    """
    all_data = []
    invited = []
    not_invited = []
    for dict in data_list:
        distance = dis_form(sf_lat, dict["latitude"], sf_lon, dict["longitude"])
        dict["Distance"] = round(distance, 3)
        if distance <= 100:
            invited.append(dict)
        else:
            not_invited.append(dict)

    divider = ["-----------------------"]
    header_1 = ["INVITE"]
    header_2 = ["NO INVITE"]
    empty = [""]

    all_data.append(header_1)
    all_data.append(divider)
    all_data.append(invited)
    all_data.append(empty)
    all_data.append(header_2)
    all_data.append(divider)
    all_data.append(not_invited)

    return all_data

dist_list = distance_calc(sorted_data)  # new working variable with all items in a sorted dictionary and divided into a list of invited and not-invited
# print(dist_list)
    

# with open('Output.txt', 'w') as convert_file:
     # convert_file.write(json.dumps(dist_list))


def write_to_txt(list_input):
    """
    Writes working list of organized and formatted informatin to .txt file
    """
    with open('Output.txt', 'w') as convert_file:
        for list in list_input:
            for dict in list:
                convert_file.write("%s\n" % dict)


write_to_txt(dist_list)


if __name__ == "__main__":
    duplicate_test = detect_dups(sorted_data)
    print(duplicate_test)
    print(data_import)
