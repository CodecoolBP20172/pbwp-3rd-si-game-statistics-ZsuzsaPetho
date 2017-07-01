
# Report functions


def count_games(file_name='game_stat.txt'):
    number = len(list_loader(file_name))
    return number


def decide(file_name, year):
    whole_list = list_loader(file_name)
    for item in whole_list:
        if year == int(item[2]):
            return True
    return False


def get_latest(file_name):
    whole_list = list_loader(file_name)
    title = whole_list[0][0]
    date = int(whole_list[0][2])
    for item in whole_list:
        if int(item[2]) > date:
            title = item[0]
            date = int(item[2])
    return title


def count_by_genre(file_name, genre):
    whole_list = list_loader(file_name)
    number = 0
    for item in whole_list:
        if item[3] == genre:
            number += 1
    return number


def get_line_number_by_title(file_name, title):
    whole_list = list_loader(file_name)
    number = 0
    for item in whole_list:
        number += 1
        if item[0] == title:
            break
    if whole_list[-1][0] != title and number == len(whole_list):
        raise ValueError
    return number


def sort_abc(file_name):
    whole_list = list_loader(file_name)
    title_list = []
    for item in whole_list:
        title_list.append(item[0])
    iterations = 1
    N = len(title_list)
    while iterations < N:
        j = 0
        while j <= (N-2):
            if title_list[j] > title_list[j+1]:
                title_list[j], title_list[j+1] = title_list[j+1], title_list[j]
            j += 1
        iterations += 1
    return title_list


def get_genres(file_name):
    whole_list = list_loader(file_name)
    genres_list = []
    for item in whole_list:
        if item[3] not in genres_list:
            genres_list.append(item[3])
    genres_list = sorted(genres_list)
    for i in range(len(genres_list)-1):
        if genres_list[i].lower() > genres_list[i+1].lower():
            genres_list[i], genres_list[i+1] = genres_list[i+1], genres_list[i]
    return genres_list


def when_was_top_sold_fps(file_name):
    whole_list = list_loader(file_name)
    selected_list = []
    for item in whole_list:
        if item[3] == 'First-person shooter':
            selected_list.append(item)
    if selected_list == []:
        raise ValueError
    most_sold = float(selected_list[0][1])
    year = int(selected_list[0][2])
    for item in selected_list:
        if most_sold < float(item[1]):
            most_sold = float(item[1])
            year = int(item[2])
    return year


def list_loader(file_name):
    whole_list = []
    with open(file_name) as f:
        for line in f.read().split('\n'):
            my_list = line.split("\t")
            whole_list.append(my_list)
    if whole_list[-1] == [""]:
        whole_list.pop()
    return whole_list
