from stats import count_words, count_characters, sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(f"{book_path}")
    num_words = count_words(book_text)
    text_characters = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in sorted_list(text_characters):
        if(i["char"].isalpha()):
            print(f"{i["char"]}: {i["num"]}")
            
    print("============= END ===============")

main()