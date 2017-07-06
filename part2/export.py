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


def export_report(file_name, filename="export.txt", title="Counter-Strike"):
    with open(filename, 'w') as out_file:
        print(reports.get_most_played(file_name), end='\n', file=out_file)
        print(reports.sum_sold(file_name), end='\n', file=out_file)
        print(reports.get_selling_avg(file_name), end='\n', file=out_file)
        print(reports.count_longest_title(file_name), end='\n', file=out_file)
        print(reports.get_date_avg(file_name), end='\n', file=out_file)
        print(reports.get_game(file_name, title), end='\n', file=out_file)
        print(reports.count_grouped_by_genre(file_name), end='\n', file=out_file)
        print(reports.get_date_ordered(file_name), end='\n', file=out_file)


def main():
    try:
        export_report(file_read_in())
    except FileExistsError:
        print("File already exists.")

if __name__ == '__main__':
    main()