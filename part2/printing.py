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
    print(reports.get_most_played(file_name))
    print(reports.sum_sold(file_name))
    print(reports.get_selling_avg(file_name))
    print(reports.count_longest_title(file_name))
    print(reports.get_date_avg(file_name))
    print(reports.get_game(file_name, "Counter-Strike"))
    print(reports.count_grouped_by_genre(file_name))
    print(reports.get_date_ordered(file_name))


def main():
    try:
        basic_printing(file_read_in())
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()

