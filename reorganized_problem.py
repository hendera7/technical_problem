from distance_formula import distance as dis_form  # format for input: (lat1, lat2, lon1, lon2)
from operator import itemgetter


CUSTOMER_LIST = 'customer_list.txt'
SF_LAT = 37.7866
SF_LON = -122.41284


def open_txt(file_path):
    """
    Opens file and reads file to a list of nested lists - each list is one row of the .txt file
    """
    data_list = []
    nested_list = []

    with open(file_path, 'r') as file_in:
        reader = file_in.readlines()
        for row in reader:
            row = row[2:-3]
            nested_list = row.split(",")
            data_list.append(nested_list)

    return data_list


def organize_list_to_dict(data_list):
    """
    Takes the list of lists and reorganizes the items and then converts each nested list to a dictionary
    """
    working_list = data_list

    for list in working_list:
        list.insert(3, list[0])
        del list [0]

    for list in working_list:
            for item in list:
                if item[0] == " ":
                    item = item[1:]
                if item[1] == " ":
                    item = item[2:]

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


def distance_calc(data_list):
    """
    Calculates distance and adds distance as a key to each dictionary with the 
    appropriate value for each user
    """
    for dict in data_list:
        distance = dis_form(SF_LAT, dict["latitude"], SF_LON, dict["longitude"])
        dict["Distance"] = round(distance, 3)

    return data_list


def sort_data(data_list):
    """
    Takes the data and sorts each user into either 'invited' or 'not invited' group based on 
    distance and then displays the information by group with formatting
    """
    all_data = []
    invited = []
    not_invited = []

    for dict in data_list:
        if dict["Distance"] <= 100:
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


def detect_dups(list_of_dicts):
    """
    Detects duplicates and prints record of said duplicates
    """
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


def write_to_txt(list_input):
    """
    Writes working list of organized and formatted information to .txt file
    """
    with open('Output_2.txt', 'w') as convert_file:
        for list in list_input:
            for dict in list:
                convert_file.write("%s\n" % dict)


data_import = open_txt(CUSTOMER_LIST)
working_data = organize_list_to_dict(data_import)
sorted_data = sorted(working_data, key=itemgetter('user_id'))
dist_list = distance_calc(sorted_data)
organized_list = sort_data(dist_list)

write_to_txt(organized_list)




if __name__ == "__main__":
    duplicate_test = detect_dups(sorted_data)
    print(duplicate_test)


