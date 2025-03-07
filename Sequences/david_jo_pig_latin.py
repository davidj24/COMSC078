# David Jo. Assignment 4 "Sequences" Part 2
# Program prupose: To use lists to create a program that converts sentences to pig latin

def main():
    while True:

        words = input("Enter a sentence to conver to pig latin: ").lower().split()

        if not words:
            return
        
        pig_latin = []

        for word in words:
            i = 0
            while word[i] not in "aeiouy": # This is getting all the consonants before the first vowel
                i += 1
            if i == 0:
                pig_latin.append(word + "way")
            else:
                pig_latin.append(word[i:] + word[:i] + "ay") # I was so close to getting this all in 1 case but the damn w makes it so I can't :(
        
        print(" ".join(pig_latin))


if __name__ == "__main__":
    main()