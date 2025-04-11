def count_words(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.read().split())
    except FileNotFoundError:
        return "File not found!"


def word_counter():

    with open('test_file.txt', 'w') as file:
        file.write("Hello world! This is a test file.")
    assert count_words('test_file.txt') == 7, "Test case 1 failed!"


    
    open('empty_file.txt', 'w').close()
    assert count_words('empty_file.txt') == 0, "Test case 2 failed!"


    
    assert count_words('nonexistent_file.txt') == "File not found!", "Test case 3 failed!"
    
    
    print("All test cases passed!")


if __name__ == "__main__":
    word_counter()
