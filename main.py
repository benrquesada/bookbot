def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main ():
    print(get_book_text("./books/frankenstein.txt"))

main()