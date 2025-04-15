from stats import word_count

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
    

def main ():
    print(f"{word_count(get_book_text("./books/frankenstein.txt"))} words found in the document")

main()