import sys
from stats import character_count, get_num_words, sorted_list


def main():
    if len(sys.argv) == 2:
        text = get_book_text(sys.argv[1])
        count = character_count(text)
        total = get_num_words(text)
        sort = sorted_list(count)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for item in sort:
        ch = item["char"]
        cht = item["num"]
        if ch.isalpha():
            print(f"{ch}: {cht}")
    print("============= END ===============")
   
def get_book_text(path):
    with open(path) as f:
        return f.read()
    



main()