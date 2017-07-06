import math

# Report functions


def get_most_played(file_name):
    whole_list = load_data_into_list(file_name)
    maximum = float(whole_list[0][1])
    title = whole_list[0][0]
    for element in whole_list:
        if maximum < float(element[1]):
            maximum = float(element[1])
            title = element[0]
            break
    return title


def sum_sold(file_name):
    whole_list = load_data_into_list(file_name)
    return sum(float(line[1]) for line in whole_list)


def get_selling_avg(file_name):
    whole_list = load_data_into_list(file_name)
    return sum_sold(file_name) / sum(1 for line in whole_list)


def count_longest_title(file_name):
    whole_list = load_data_into_list(file_name)
    return max(len(line[0]) for line in whole_list)


def get_date_avg(file_name):
    whole_list = load_data_into_list(file_name)
    return math.ceil(sum(float(line[2]) for line in whole_list) / sum(1 for line in whole_list))


def get_game(file_name, title):
    whole_list = load_data_into_list(file_name)
    dType = [str, float, int, str, str]
    for item in whole_list:
        if item[0] == title:
            prop_list = [t(x) for t, x in zip(dType, item)]
    return prop_list


def count_grouped_by_genre(file_name):
    whole_list = load_data_into_list(file_name)
    dict_of_gend = {}
    list_of_genres = []
    for line in whole_list:
        if line[3] not in list_of_genres:
            list_of_genres.append(line[3])
    for genre in sorted(list_of_genres):
        number = 0
        for item in whole_list:
            if item[3] == genre:
                number += 1
        dict_of_gend.update({genre: number})
    return dict_of_gend


def get_date_ordered(file_name):
    whole_list = load_data_into_list(file_name)
    dict_of_list = {}
    for item in whole_list:
        dict_of_list.update({item[0]: item[2]})
    ord_list = [(k, dict_of_list[k]) for k in sorted(dict_of_list, key=dict_of_list.get, reverse=True)]
    for itera in range(len(ord_list)-1):
        for i in range(len(ord_list)-1):
            if ord_list[i][1] == ord_list[i+1][1]:
                if ord_list[i][0].lower() > ord_list[i+1][0].lower():
                    ord_list[i], ord_list[i+1] = ord_list[i+1], ord_list[i]
    fin_list = [item[0] for item in ord_list]
    return fin_list


def load_data_into_list(file_name):
    whole_list = []
    with open(file_name) as input_file:
        my_list = input_file.read().split('\n')
        for line in my_list:
            whole_list.append(line.split('\t'))
    return whole_list
