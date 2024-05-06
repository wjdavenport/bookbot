def hello_world():
    print("Hello, world!")

# hello_world()

# ...from boot.dev: https://www.boot.dev/lessons/d6536f09-dc1d-4922-a2a5-a73c536ee09d
# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["number"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_list = file_contents.split()
    print(len(word_list))

    word_dict = {}
    char_dict = {}

    for word in word_list:
        word = word.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1 

    print(f"Distinct words in this file: {len(word_dict.keys())}")
    print(f"Distinct characters in this file: {len(char_dict.keys())}")
    print(f"Making an index for the word dictionary...\n")

    word_count_list = []
    char_count_list = []
    for word in word_dict.keys():
        word_count_list.append({"word": word,  "number": word_dict[word]})
    for character in char_dict.keys():
        if character.isalpha():
            char_count_list.append({"alphachar": character, "number": char_dict[character]})

    word_count_list.sort(reverse=True, key=sort_on)
    char_count_list.sort(reverse=True, key=sort_on)

    for entry in word_count_list:
        print(f"{entry['word']} {entry['number']}")
    for entry in char_count_list:
        print(f"{entry['alphachar']} {entry['number']}")

    

    
    

    
    

        


main()
