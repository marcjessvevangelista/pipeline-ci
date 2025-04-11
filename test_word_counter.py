def test_word_counter():
    # Create a temporary test file
    test_file = 'test_file.txt'
    with open(test_file, 'w') as file:
        file.write("Hello world! This is a test file.")
    

    # Test the word count
    assert count_words(test_file) == 7, "Test case 1 failed!"


    # Test with an empty file
    empty_file = 'empty_file.txt'
    with open(empty_file, 'w') as file:
        pass


    assert count_words(empty_file) == 0, "Test case 2 failed!"


    # Test with a nonexistent file
    assert count_words('nonexistent_file.txt') == "File not found!", "Test case 3 failed!"

    print("All test cases passed!")
    

# Run the tests
if __name__ == "__main__":
    test_word_counter()
