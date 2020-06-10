#-*-coding: utf8-*-
import time
from datetime import datetime
import constants

#brief : gets and filters specific lines from a given file using some keywords
#parameters :   "filename" -> filename (located in the same folder as this script)
#               "keywords" -> keywords
#return : list - a list containing all the recovered lines
def select_lines(filename, keywords, entity, procedure):
    """Cette methode recupere une ligne depuis un fichier texte"""
    res = list()
    rx = ''
    tx = ''
    time = ''
    counter = 0

    with open(filename, 'r') as my_file:
        for line in my_file:
            for word in keywords:
                if word[0] in line:
                    fir = line.split("\n")

                    tx = get_tx(entity, fir[0])
                    rx = get_rx(entity, fir[0])
                    time = get_time(str(fir[0]))

                    tup = (fir[0], time, tx, rx, word[1])
                    res.append(tup)
                    counter += 1
                    break
            if counter == constants.TOTAL_LINES[entity-1][procedure]:
                break
    my_file.close()
    return res

#brief : methode to show a resume of the total lines found
#parameters :   "list" -> a list of the filtered lines
#                "keywords" -> the keywords
#return : string - total number of lines and the lines
def toString(list):
    res= ''
    for _ in list:
        res += str(_) + "\n"
    return res


def toString_debug(list, procedure):
    count = len(list)
    res = "Total number of lines including the keywords  {}  -> {}".format(procedure, count)
    res += "\n Tuple example : (literal line, time, Tx, Rx, Description)"
    res += "\n---------------------------------------------------------------------------\n"
    for _ in list:
        res += str(_) + "\n"
    return res

#brief : methode to get the latency between two specific lines
#parameters : "line1" and "line2" are the selected lines
#return : int - latency
def get_latency(line1, line2):
    FMT = '%H:%M:%S.%f'
    recovered1 = get_time(line1)
    recovered2 = get_time(line2)
    t1 = datetime.strptime(recovered1, FMT)
    t2 = datetime.strptime(recovered2, FMT)
    res = t2 - t1
    return res


#brief : methode to get the time stamp
#parameters : "l" is a single line
#return : int - the time stamp
def get_time(line):
    parsed = line.split(" ", 1)
    res = parsed[0].strip('[\'')
    return res


def select_procedure(word):
    key = word.lower()
    res = []
    lines_index = []
    ind = 0
    if 'cell search' in key:
        res += constants.CELL_SEARCH
    elif 'rrc connection' in key:
        res += constants.RRC_CONNECTION
        ind = 1
    elif 'attach' in key:
        res += constants.ATTACH_AND_AUTHENTICATION
        ind = 2
    elif 'radio bearer setup' in key:
        res += constants.DEFAULT_RADIO_BEARER_SETUP
        ind = 3
    elif 'release' in key:
        res += constants.DETACH
        ind = 4
    elif 'all' in key:
        res += constants.ALL
        ind = 5
    lines_index.append(res)
    lines_index.append(ind)
    return lines_index

def get_rx(entity, line):
    res = ''
    ue = 'UE'
    enb = 'eNodeB'
    epc = 'EPC'
    if entity == 1:
        if 'Rx' in line or 'DL' in line:
            res = ue
        else: res = enb
    elif entity == 2:
        if 'Rx' in line or 'Received' in line:
            res = enb
        elif 'Tx' in line:
            res = ue
        elif 'Sending' in line:
            res = epc
    elif entity == 3:
        if 'Received' in line or 'UL' in line:
            res = epc
        else: res = enb
    return res

def get_tx(entity, line):
    res = ''
    ue = 'UE'
    enb = 'eNodeB'
    epc = 'EPC'
    if entity == 1:
        if 'Tx' in line:
            res = ue
        else: res = enb
    elif entity == 2:
        if 'Tx' in line or 'Sending' in line:
            res = enb
        elif 'Rx' in line:
            res = ue
        elif 'Received' in line:
            res = epc
    elif entity == 3:
        if 'Sending' in line or 'Packing' in line or 'Sent' in line:
            res = epc
        else: res = enb
    return res

def deleting_doubles(list_original):
    list = list_original.copy()
    res = []
    bingo = False
    time_e = ''
    time_r = ''
    for x in list:
        bingo = False
        for y in list:
            if y[4]==x[4] and y[2]==x[2] and y[3]==x[3] and y[0]!=x[0] and y[1]!=x[1]:
                if y[1] <= x[1]:
                    time_e = y[1]
                    time_r = x[1]
                else:
                    time_e = x[1]
                    time_r = y[1]
                ##tupla = (time_e, time_r, Tx, Rx, Description)
                tupla = (time_e, time_r, x[2], x[3], x[4])#, x[0], y[0])
                res.append(tupla)
                list.remove(x)
                list.remove(y)
                bingo = True
                break
        if bingo == False:
            ##tupla = (time_e, time_r, Tx, Rx, Description)
            tupla = ('0', x[1], x[2], x[3], x[4])#, x[0], x[0])
            res.append(tupla)
    return res

####Formatting the final list into PUML language
def formatter(list, procedure):
    w = '@startuml \nheader IBANEZ Israel, MACEDO Luis \ntitle {0}\n'.format(procedure)
    w += 'participant UE\nparticipant eNodeB\ncollections EPC\n'
    for elem in list:
        w += '{0} -> {1}: {2}\n'.format(elem[2], elem[3], elem[4])
    w += "@enduml\n"

    result_file = open("result.puml", "wt")
    result_file.write(w)
    result_file.close()
