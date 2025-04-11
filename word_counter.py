def count_words(file_path):
    """Counts the number of words in a given text file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found!"
