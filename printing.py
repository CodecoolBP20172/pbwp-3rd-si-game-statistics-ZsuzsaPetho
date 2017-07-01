import reports
import sys


def file_read_in():
    if len(sys.argv) < 2:
        file_name = 'game_stat.txt'
    else:
        try:
            file_name = sys.argv[1]
        except FileNotFoundError:
            print("File not found! Check your argument and try to run the program again")
    return file_name


def basic_printing(file_name):
    print('How many games are in the file?')
    print(reports.count_games(file_name), end='\n\n')
    print('Is there a game from a given year?')
    year = int(input("What year do you want to check? "))
    print(reports.decide(file_name, year), end='\n\n')
    print('Which was the latest game?')
    print(reports.get_latest(file_name), end='\n\n')
    print('What are the genres?')
    print(reports.get_genres(file_name), end='\n\n')
    print('How many games do we have by genre?')
    genre = input("What genre do you want to count? ")
    print(reports.count_by_genre(file_name, genre), end='\n\n')
    try:
        print('What is the line number of the given game (by title)?')
        title = input("What title are you looking for? ")
        print(reports.get_line_number_by_title(file_name, title), end='\n\n')
    except ValueError:
        print("Given title is not in the database!", end='\n\n')
    print('What is the alphabetical ordered list of the titles?')
    print(reports.sort_abc(file_name), end='\n\n')
    print('What is the release date of the top sold "First-person shooter" game?')
    print(reports.when_was_top_sold_fps(file_name), end='\n\n')


def main():
    try:
        basic_printing(file_read_in())
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
