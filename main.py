from stats import word_count
from stats import char_count
from stats import report
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    try:
        book_txt = get_book_text(sys.argv[1])
    except:
        print(f"File not found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(word_count(sys.argv[1]))
    print("--------- Character Count -------")
    char_dict = char_count(book_txt)
    char_list = report(char_dict)
    for item in char_list:
        for entry in item:
            print(f"{entry}: {item[entry]}")
    print("============= END ===============")

    # __name__
if __name__=="__main__":
    main()