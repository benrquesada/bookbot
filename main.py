from stats import word_count, character_count, sorted_caracter_dicts
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
    

def main ():


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
        


    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    wc = word_count(book_text)
    character_dict = character_count(book_text)
    sorted_caracter_dict_list = sorted_caracter_dicts(character_dict)
    
    
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for dict in sorted_caracter_dict_list:
        letter = dict["character"]
        if letter.isalpha():
            print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")
    
main()