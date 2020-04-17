#-*-coding: utf8-*-
import time
from datetime import datetime

#brief : gets and filters specific lines from a given file using some keywords
#parameters :   "filename" -> filename (located in the same folder as this script)
#               "keywords" -> keywords
#return : list - a list containing all the recovered lines
def select_lines(filename, keywords):
    """Cette methode recupere une ligne depuis un fichier texte"""
    res = list()
    count = 0
    with open(filename, 'r') as my_file:
        for line in my_file:
            for word in keywords:
                if word in line:
                    count += 1
                    fir = line.split("\n")
                    res.append(fir[0])
                    break

    my_file.close()
    return res

#brief : methode to show a resume of the total lines found
#parameters :   "list" -> a list of the filtered lines
#                "keywords" -> the keywords
#return : string - total number of lines and the lines
def show(list, keywords):
    count = len(list)
    res = "Total number of lines including the keywords  {}  -> {}".format(keywords, count)
    res += "\n---------------------------------------------------------------------------\n"
    for _ in list:
        res += str(_) + "\n"
    return res

#brief : methode to show a resume of the total lines found
#parameters :   "list" -> a list of the filtered lines
#                "keywords" -> the keywords
#return : string - total number of lines
def show_nbLines(list, keywords):
    count = len(list)
    k = ""
    if len(list)>1:
        for _ in range(len(keywords)): k += keywords[_]
    else: k = keywords[0]
    return "Total number of lines including the keyword(s) \" {} \" -> {} \n".format(k, count)


#brief : methode to get the latency between two specific lines
#parameters : "line1" and "line2" are the selected lines
#return : int - latency
def get_latency(line1, line2):
    FMT = '%H:%M:%S.%f'
    recovered1 = get_time(line1)                        #Problems getting the latency !!!!
    recovered2 = get_time(line2)
    t1 = datetime.strptime(recovered1, FMT)
    t2 = datetime.strptime(recovered2, FMT)
    res = t2 - t1
    return res


#brief : methode to get the time stamp
#parameters : "l" is a single line
#return : int - the time stamp
def get_time(l):
    parsed = l.split(" ", 1)
    ok = parsed[0].strip('[\'')
    return ok
