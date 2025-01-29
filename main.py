def wc(text):
    words = text.split()
    return len(words)

def charCount(text):
    lowercase = text.lower()
    letter_count = {" ":0,"a":0,"b":0,"c":0,"d":0,"e":0,"d":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

    for letter in lowercase:
        if letter in letter_count:
            letter_count[letter] += 1
    
    return letter_count
    

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
	    file_contents = f.read()

    print(f"--- Begin report of {file_path} ---")

    unsorted_letters = charCount(file_contents)
    sorted_letters = dict(sorted(unsorted_letters.items(), key=lambda item: item[1], reverse=True))
    
    print(f"{wc(file_contents)} words found in the document")
    print("")
    for letter in sorted_letters:
        count = sorted_letters[letter]
        if letter != " ":
            print(f"The \'{letter}\' character was found {count} times")


    print("--- End report ---")

main()