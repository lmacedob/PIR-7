#-*-coding: utf8-*-
import sys
import outilParser

if __name__ == "__main__":
    file = sys.argv[1]      #source file
    keyword = sys.argv[2]   #keyword to do the text treatment

    #Let's get the lines from the log that interest us,
    #using the keyword to extract only the lines containing it
    #As a result, we have a list containing the interesting lines
    lines = outilParser.from_file(file, keyword)

    #We convert that list of lines into a string
    lines_text = outilParser.show(lines, keyword)
    print(lines_text)  #print for debugging

    #Creation of a new text file, let's call it result.txt
    #We will push to this file all the recovered lines
    text_file = open("result.txt", 'wt')
    n = text_file.write(lines_text)
    text_file.close() #Don't forget to close the file
