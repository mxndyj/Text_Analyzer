
### 
### Author: Mandy Jiang
### Class: CSC110
### Description: This program is designed to read a file the user inputs
### and determine the sizes, capitalization, frequency, and punctuation of the words 
### in the file. It converts the information into visual bar graphics using graphics.


from graphics import graphics

def read_file(file, word_count):
    '''
    This function will read  the file and find all the
    unique words in the file and put the words into a dictionary.
    file = the text file from the user
    word_count =  empty dict from main
    '''
    file_name = open(file, 'r')
    for line in file_name:
        if line != '\n': 
            split = line.strip('\n').split(' ')
            for i in range(len(split)):
                if split[i] not in word_count:  #placing unique words into dict
                    word_count[split[i]] = 0
                else:
                    word_count[split[i]] += 1

max1=0
max2=0
max3=0
smallword=''
medword=''
largeword=''

def which_length(word_count, gui):
    '''
    This function will look thru the dictionary and
    find the words that are small, medium, and large
    and count the occurances while also creating the bars
    word_count = the dictionary 
    gui = the graphics canvas
    '''
    total = (450 / len(word_count))
    small = 0
    med = 0
    large = 0
    
    global max2,max1,smallword,medword,largeword,max3
  
    for key in word_count:  # determining length of word and more frequent words
        if len(key) < 5:
            small += 1
            if word_count[key]>max1:
                max1=word_count[key]
                smallword=key
        elif len(key) >= 5 and len(key) <= 7:
            med+= 1
            if word_count[key]>max2:
                max2=word_count[key]
                medword=key
        elif len(key) >= 8:
            large += 1
            if word_count[key]>max3:
                max3=word_count[key]
                largeword=key
    gui.rectangle(40, 190, 150, total * small, 'blue') # drawing the bars
    gui.text(40, 190, 'small words', 'white', 10)
    gui.rectangle(40, 190 + total * small, 150,total * med, 'green')
    gui.text(40, 190 + total * small, 'medium words', 'white', 10)
    gui.rectangle(40, 190 + total * small + total * med,150, total * large, 'red')
    gui.text(40, 190 + total * small + total * med,'large words', 'white', 10)
    

def caps(word_count, gui):
    '''
    This function will look through a  dict 
    and determine if a word is capitalized. It will also draw the bars for the capitalized/non-cap.
    word_count: dict from main
    gui: graphics canvas
    '''
    cap= 0
    non_cap = 0
    
    total = (450 / len(word_count))
    for key in word_count:
        if len(key) != 0:
            if key[0].isupper():
                cap += 1
            else:
                non_cap += 1
    gui.rectangle(240, 190, 150, total * cap, 'blue')
    gui.text(240, 190, 'Capitalized', 'white', 10)
    gui.rectangle(240, 190 + total * cap, 150,total * non_cap, 'green')
    gui.text(240, 190 + total * cap, 'Non Capitalized', 'white',10)

def punctuation(gui, word_count):
    '''
    This function will run through the dictionary and
    find the words that are punctuated or not punctuated
    counting the occurances for each. It will also
    create the bars and text for the punctuated/not punctuated.
    word_count = dict from main
    gui =  graphics canvas
    '''
    punct = 0
    non_punct = 0
    
    punctuation = ['.', ',', '!', '?'] #listing what I'm looking for 
    total = (450 / len(word_count)) #comparison variable 
    for key in word_count: 
        if len(key) != 0:
            if key[-1] in punctuation:
                punct += 1
            else:
                non_punct += 1
        gui.rectangle(440, 190, 150, total * punct, 'blue') #drawing bars
        gui.text(440, 190, 'Punctuated', 'white', 10)
        gui.rectangle(440, 190 + total * punct, 150,total* non_punct,'green')
        gui.text(440, 190 + total * punct, 'Non Punctuated','white', 10)

def chart(word_count, file, gui):
    '''
    This function will finish the graphic visual by writing the text and labels 
    that are shown above the bar graphics. It will also use global
    variables to find the most used words. it is also
    calling other function to bring the program together.
    word_count: dict from main
    gui: canvas 
    '''

    
    mostused= str(smallword)+' ('+str(max1)+'x) '+ str(medword)+' ('+str(max2)+'x) '+str(largeword)+ ' ('+str(max3)+'x)'
    gui.rectangle(0, 0, 650, 700, 'gray')
    read_file(file, word_count)
    gui.text(40, 25, file, 'cyan', 17)
    gui.text(40, 65, 'Total Unique Words: ' + str(len(word_count)), 'white', 17)
    gui.text(40, 110, 'Most used words (s/m/l): ' , 'white', 11)
    gui.text(240, 110, mostused, 'red', 11)
    gui.text(40, 150, 'Word Lengths', 'white', 17)
    gui.text(240, 150, 'Cap/Non-Cap', 'white', 17)
    gui.text(435, 150, 'Punct/Non-Punct', 'white', 17)
    
    which_length(word_count, gui)
    caps(word_count, gui)
    punctuation(gui, word_count)

def main():
    file = input('Enter a file name: \n')
    gui = graphics(650, 700, 'infographic')
    word_count = {}
    chart(word_count, file, gui)
    while True:
        gui.update()

main()
