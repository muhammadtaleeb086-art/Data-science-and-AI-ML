# TEXT ANALYZER
"""
Take input

Calculate:

word count

character count

vowel count

most frequent word

Print results properly formatted
"""

def text_analyzer(text):
    # Initialize counts
    word_count = 0
    char_count = 0
    vowel_count = 0
    word_freq = {}

    # Define vowels
    vowels = 'aeiouAEIOU'

    # Split text into words
    words = text.split()

    # Count words and characters
    for word in words:
        word_count += 1
        char_count += len(word)

        # Count vowels in the word
        for char in word:
            if char in vowels:
                vowel_count += 1

        # Update word frequency
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Find the most frequent word
    most_frequent_word = max(word_freq, key=word_freq.get)

    # Print results
    print(f"Word Count: {word_count}")
    print(f"Character Count: {char_count}")
    print(f"Vowel Count: {vowel_count}")
    print(f"Most Frequent Word: '{most_frequent_word}' (appears {word_freq[most_frequent_word]} times)")

# Example usage
if __name__ == "__main__":
    input_text = input("Enter a text to analyze: ")
    text_analyzer(input_text)
