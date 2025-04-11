def count_words(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.read().split())
    except FileNotFoundError:
        return "File not found!"


def word_counter():
    # Test case 1: Non-empty file
    with open('test_file.txt', 'w') as file:
        file.write("Hello world! This is a test file.")
    assert count_words('test_file.txt') == 7, "Test case 1 failed!"

    # Test case 2: Empty file
    open('empty_file.txt', 'w').close()
    assert count_words('empty_file.txt') == 0, "Test case 2 failed!"

    # Test case 3: Nonexistent file
    assert count_words('nonexistent_file.txt') == "File not found!", "Test case 3 failed!"


    print("All test cases passed!")


if __name__ == "__main__":
    word_counter()
