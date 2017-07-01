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


def export_report(file_name, filename="export.txt", year=2000, genre="First-person shooter", title="Counter-Strike"):
    with open(filename, 'w') as out_file:
        print(reports.count_games(file_name), end='\n', file=out_file)
        print(reports.decide(file_name, year), end='\n', file=out_file)
        print(reports.get_latest(file_name), end='\n', file=out_file)
        print(reports.get_genres(file_name), end='\n', file=out_file)
        print(reports.count_by_genre(file_name, genre), end='\n', file=out_file)
        print(reports.get_line_number_by_title(file_name, title), end='\n', file=out_file)
        print(reports.sort_abc(file_name), end='\n', file=out_file)
        print(reports.when_was_top_sold_fps(file_name), end='\n', file=out_file)


def main():
    try:
        export_report(file_read_in())
    except FileExistsError:
        print("File already exists.")

if __name__ == '__main__':
    main()