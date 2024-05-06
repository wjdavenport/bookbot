def hello_world():
    print("Hello, world!")

# hello_world()

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
                
    print(word_dict)
    print(char_dict)


main()
