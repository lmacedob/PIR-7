#-*-coding: utf8-*-

def from_file(filename, keyword):
    """Cette methode recupere une ligne depuis un fichier texte"""
    res = list()
    count = 0
    with open(filename, 'r') as my_file:
        for line in my_file:
            if keyword in line:
                count += 1
                res.append(line.split("\n"))
    my_file.close()
    return res


def show(list, keyword):
    count = len(list)
    res = "Total number of lines including the keyword \" {} \" -> {} \n".format(keyword, count)
    res += "--------------------------------------------------------------------- \n"
    for _ in list:
        res += str(_) + "\n"
    return res
