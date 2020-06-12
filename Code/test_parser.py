#-*-coding: utf8-*-
import sys
import outilParser

if __name__ == "__main__":
    try:
        file_1 = sys.argv[1]      #source file 1
        file_2 = sys.argv[2]      #source file 2
        file_3 = sys.argv[3]      #source file 3
        procedure = sys.argv[4]  #keywords necessary to do the text treatment

        if ".log" not in (file_1 and file_2 and file_3):
            raise IndexError
    except IndexError:
        raise SystemExit("******ERROR : Parameters missing******\n Usage : {sysargv[1,2]} files to treat (.log) ;  {sys.argv[3:]} procedure")

    ####Get the procedure messages####
    temp = outilParser.select_procedure(procedure)
    keywords = temp[0]
    ind = temp[1]

    ####Extraction of lines####
    #Let's get the lines from the log that interest us,
    #using the keyword to extract only the lines containing it
    #As a result, we have a list containing the interesting lines
    keywords_copy = keywords.copy()

    lines_file_1 = outilParser.select_lines(file_1, keywords_copy, 1,ind)    ##UE == 1
    lines_file_2 = outilParser.select_lines(file_2,keywords_copy, 2,ind)     ##eNodeB == 2
    lines_file_3 = outilParser.select_lines(file_3,keywords_copy, 3,ind)     ##EPC == 3

    ###Important
    lines_final = lines_file_1 + lines_file_2 + lines_file_3

    ##Deleting doubles and getting the final list of tuples
    treated_lines = outilParser.deleting_doubles(lines_final)
    treated_lines.sort()
    print("\n")


    #We convert that list of lines into a string
    #lines_text = outilParser.toString(lines_final)
    lines_text = outilParser.toString_debug(lines_final, procedure)
    print(lines_text)
    print("\n")

    lines_text_after_treatment = outilParser.toString_debug(treated_lines, procedure)
    print(lines_text_after_treatment)


    #####Creation of a new text file, let's call it result.txt
    #We will push all the recovered lines into this file
    text_file = open("result.txt", 'wt')
    text_file.write(lines_text)
    text_file.close()                   #Don't forget to close the file

    text_file_extra = open("mamalon.txt", 'wt')
    text_file_extra.write(lines_text_after_treatment)
    text_file_extra.close()

    proc = procedure.upper()
    outilParser.formatter(treated_lines, proc)


    ###########Latency test
    #lat_test = outilParser.get_latency(str(lines[1]),str(lines[-1]))
    #print(outilParser.get_time(str(lines[0])))
    #print("Latency test between \n  -----> {0} \n  and \n  -----> {1} \n  = {2} s".format(str(lines[0]),str(lines[-1]),lat_test))
    #print("\n")
