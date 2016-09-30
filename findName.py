#!/bin/bash/python3

import math, os, time

filepath = '/home/pettertaule/Linux-tutorial/files/'
htmlpath = '/home/pettertaule/Linux-tutorial/output/'

def findNames(secRemaining):
    m, s = divmod(secRemaining, 60)
    # Find files in path, and put them in filenames array
    filenames = []
    for filename in os.listdir(filepath):
        filenames.append(filename)

    #Reverse each string in filearray
    for i in range(len(filenames)):
        filenames[i] = filenames[i][::-1]

    # Sort array, and reverse each string back again
    filenames = sorted(filenames)
    for i in range(len(filenames)):
        filenames[i] = filenames[i][::-1]

    #Store first line to array
    people = []
    for i in range(len(filenames)):
        try:
            f = open(filepath + filenames[i],'r')
            people.append(f.readline().rstrip())
            f.close
        except Exception:
            pass

    #Remove empty elements
    people = list(filter(None, people))

    #Write html-file
    output = open(htmlpath + "competition.html", 'w')
    htmlstart = '<!DOCTYPE html>\n' + \
    '<html>\n' + \
    '<meta http-equiv="refresh" content="1" />\n' + \
    '<body>\n\n' + \
    '<h1>Konkurranse</h1>\n' + \
            '<h3> Tid igjen:\t' + str(m) + ':' + str(s) + '</h3>\n' \
    '<h3>Rangering</h3>\n' + \
    '<ol>\n'
    output.write(htmlstart)

    i = 0
    while ( i < 5 and i < len(people)):
        outputline = "<li>" + people[i] + "</li>" + "\n"
        output.write(outputline)
        i += 1

    htmlend = '</ol>\n</body>\n</html> \n'
    output.write(htmlend)

    output.close


def main():
    startTime = math.floor(time.time())
    secRemaining = 300
    while (secRemaining >= 0):
        time.sleep(1)
        findNames(secRemaining)
        secRemaining = 300 + startTime - math.floor(time.time())


if __name__ == "__main__":
    main()
