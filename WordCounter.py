def get_user_input():
    text = input("Enter a sentence or paragraph: ")
    return text

def count_words(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def display_results(word_count):
    print("Word Count:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

def main():
    text = get_user_input()
    word_count = count_words(text)
    display_results(word_count)

if __name__ == "__main__":
    main()
