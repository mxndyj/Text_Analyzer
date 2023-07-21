from graphics import graphics

def read_file(file, word_count):
    '''
    This function will read the file and find all the
    unique words in the file and put the words into a dictionary.
    file = the text file from the user
    word_count = empty dict from main
    '''
    with open(file, 'r') as file_name:
        for line in file_name:
            if line != '\n':
                split = line.strip('\n').split(' ')
                for i in range(len(split)):
                    if split[i] not in word_count:  # placing unique words into dict
                        word_count[split[i]] = 0
                    else:
                        word_count[split[i]] += 1

def find_word_lengths(word_count):
    '''
    This function will look through the dictionary and
    find the words that are small, medium, and large
    and count the occurrences while also creating the bars.
    word_count = the dictionary
    '''
    total = (450 / len(word_count)) # height for bars
    small = 0
    med = 0
    large = 0
    
    max1 = 0
    max2 = 0
    max3 = 0
    smallword = ''
    medword = ''
    largeword = ''
  
    for key in word_count:
        if len(key) < 5:
            small += 1
            if word_count[key] > max1:
                max1 = word_count[key]
                smallword = key
        elif len(key) >= 5 and len(key) <= 7:
            med += 1
            if word_count[key] > max2:
                max2 = word_count[key]
                medword = key
        elif len(key) >= 8:
            large += 1
            if word_count[key] > max3:
                max3 = word_count[key]
                largeword = key
                
    return small, med, large, max1, max2, max3, smallword, medword, largeword

def find_capitalization(word_count):
    '''
    This function will look through a dict
    and determine if a word is capitalized.
    word_count: dict from main
    '''
    cap = 0
    non_cap = 0
    
    for key in word_count:
        if len(key) != 0:
            if key[0].isupper():
                cap += 1
            else:
                non_cap += 1
                
    return cap, non_cap

def find_punctuation(word_count):
    '''
    This function will run through the dictionary and
    find the words that are punctuated or not punctuated,
    counting the occurrences for each.
    word_count = dict from main
    '''
    punct = 0
    non_punct = 0
    
    punctuation = ['.', ',', '!', '?']
    for key in word_count: 
        if len(key) != 0:
            if key[-1] in punctuation:
                punct += 1
            else:
                non_punct += 1
                
    return punct, non_punct

def draw_bars(gui, total, small, med, large, cap, non_cap, punct, non_punct):
    '''
    This function will draw the bars and text for the visualizations.
    gui = the graphics canvas
    '''
    gui.rectangle(40, 190, 150, total * small, 'blue')
    gui.text(40, 190, 'small words', 'white', 10)
    gui.rectangle(40, 190 + total * small, 150, total * med, 'green')
    gui.text(40, 190 + total * small, 'medium words', 'white', 10)
    gui.rectangle(40, 190 + total * small + total * med, 150, total * large, 'red')
    gui.text(40, 190 + total * small + total * med, 'large words', 'white', 10)

    gui.rectangle(240, 190, 150, total * cap, 'blue')
    gui.text(240, 190, 'Capitalized', 'white', 10)
    gui.rectangle(240, 190 + total * cap, 150, total * non_cap, 'green')
    gui.text(240, 190 + total * cap, 'Non Capitalized', 'white', 10)

    gui.rectangle(440, 190, 150, total * punct, 'blue')
    gui.text(440, 190, 'Punctuated', 'white', 10)
    gui.rectangle(440, 190 + total * punct, 150, total * non_punct, 'green')
    gui.text(440, 190 + total * punct, 'Non Punctuated', 'white', 10)

def main():
    file = input("Please enter the name of the text file: ")
    gui = graphics(650, 700, 'infographic')
    word_count = {}
    read_file(file, word_count)
    
    total = (450 / len(word_count))
    small, med, large, max1, max2, max3, smallword, medword, largeword = find_word_lengths(word_count)
    cap, non_cap = find_capitalization(word_count)
    punct, non_punct = find_punctuation(word_count)
    
    mostused = f'{smallword} ({max1}x) {medword} ({max2}x) {largeword} ({max3}x)'
    
    gui.rectangle(0, 0, 650, 700, 'gray')
    gui.text(40, 25, file, 'cyan', 17)
    gui.text(40, 65, 'Total Unique Words: ' + str(len(word_count)), 'white', 17)
    gui.text(40, 150, 'Word Lengths', 'white', 17)
    gui.text(240, 150, 'Cap/Non-Cap', 'white', 17)
    gui.text(435, 150, 'Punct/Non-Punct', 'white', 17)
    
    draw_bars(gui, total, small, med, large, cap, non_cap, punct, non_punct)
    
    gui.text(40, 110, 'Most used words (s/m/l): ', 'white', 11)
    gui.text(240, 110, mostused, 'red', 11)
    
    while True:
        gui.update()

main()