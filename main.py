def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print()
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"{word_count(text)} words found in the document.")
    print()

    sorted_characters = sort_characters(char_count(text))

    for char_dict in sorted_characters:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["count"]
            print(f"The '{char}' character was found {count} times")   
    print()
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    return len(text.split())

def char_count(text):
    characters = {}
    lower_case_text = text.lower()
    for char in lower_case_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_characters(characters):
    character_list = []
    for char, count in characters.items():
        char_dict = {"char": char, "count": count}
        character_list.append(char_dict)
    character_list.sort(key=lambda item: item["count"], reverse=True)
    return character_list
main()