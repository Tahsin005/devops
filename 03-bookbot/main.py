import sys

def get_alpha_frequency(text):
    freq = [0] * 52
    
    for char in text:
        # lowercase (a-z -> ASCII 97-122)
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            freq[index] += 1
            
        # uppercase (A-Z -> ASCII 65-90)
        elif 'A' <= char <= 'Z':
            index = ord(char) - ord('A') + 26
            freq[index] += 1
            
    return freq

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    try:
        with open(book_path, 'r') as file:
            content = file.read()
            result = get_alpha_frequency(content)
            for i, count in enumerate(result):
                letter = chr(i + ord('a')) if i < 26 else chr(i - 26 + ord('A'))
                print(f"{letter}: {count}")
    except FileNotFoundError:
        print(f"File not found: {book_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
