#-*-coding: utf8-*-
import sys
import outilParser

if __name__ == "__main__":
    try:
        file = sys.argv[1]      #source file
        keywords = sys.argv[2:]  #keywords necessary to do the text treatment
    except IndexError:
        raise SystemExit("******ERROR : Parameters missing******\n Usage : {sysargv[1]} file to treat ;  {sys.argv[2:]} keywords")

    #print("\n")
    print("Keywords: {0}".format(keywords))
    #print("\n")

    #Let's get the lines from the log that interest us,
    #using the keyword to extract only the lines containing it
    #As a result, we have a list containing the interesting lines
    lines = outilParser.select_lines(file, keywords)

    #Latency test
    lat_test = outilParser.get_latency(str(lines[1]),str(lines[-1]))
    #print(outilParser.get_time(str(lines[0])))
    print("Latency test between \n  -----> {0} \n  and \n  -----> {1} \n  = {2} s".format(str(lines[0]),str(lines[-1]),lat_test))
    print("\n")

    #We convert that list of lines into a string
    lines_text = outilParser.toString(lines, keywords)
    print(lines_text)  #print for debugging
    print("\n")

    #We output the total number of lines only, and not all the content
    #print(outilParser.showOnly_nbLines(lines, keywords))


    #Creation of a new text file, let's call it result.txt
    #We will push all the recovered lines into this file
    text_file = open("result.txt", 'wt')
    n = text_file.write(lines_text)

    #Don't forget to close the file
    text_file.close()
