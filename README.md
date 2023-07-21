# Text_Analyzer
This is designed to read a text file provided by the user and analyze various 
characteristics of the words in the file, such as their sizes, capitalization, frequency, 
and punctuation usage. It then converts this information into a visual bar graph using the 
graphics library.

# Features
Here's how the program works:

Reading the File: The program starts by reading the input text file provided by the user and stores each word in the file into a dictionary (word_count). The dictionary is used to keep track of the unique words and their respective frequency (number of occurrences) in the file.

Analyzing Word Sizes: The program classifies words into three categories based on their lengths: small (less than 5 characters), medium (between 5 and 7 characters), and large (8 or more characters). It counts the occurrences of each category and calculates the most frequently used word in each category.

Analyzing Capitalization: The program determines whether each word in the file starts with a capital letter or not. It counts the number of capitalized and non-capitalized words and visualizes the results using bars.

Analyzing Punctuation: The program identifies whether each word in the file ends with punctuation (e.g., '.', ',', '!', '?'). It counts the number of punctuated and non-punctuated words and visualizes the results using bars.

Visual Representation: The program uses the graphics library to create an infographic with graphical representations of the analyzed data. The infographic includes three sets of bars:

Word Lengths: A bar for small, medium, and large words.
Capitalization: A bar for capitalized and non-capitalized words.
Punctuation: A bar for punctuated and non-punctuated words.
The most frequently used words in each category (small, medium, and large) are displayed along with the number of times they appear in parentheses.

User Interaction: The program prompts the user to enter the name of the text file they want to analyze. After providing the file name, the program displays the infographic and keeps it open for interactive visualization.

# How to use

- Place the program in a directory where you have the graphics library installed.
- Run the program using a Python interpreter. Type "python infographic.py" in terminal.
- Enter the name of the text file you want to analyze. I have included an example .txt file.
- Observe the infographic that represents the word characteristics in the input file.

# Concept Video
