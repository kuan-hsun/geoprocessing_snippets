import re

pattern = re.compile(r'\d\d\d\d-\d\d-\d\d')
string = '2018-01-01'

match = pattern.match(string)

if match:
    if (int(string.split('-')[0]) >= 1970) and (int(string.split('-')[0]) < 2018):     
        print "�ŦX"
    elif int(string.split('-')[0]) == 2018:
        if (int(string.split('-')[1]) <= 1) and (int(string.split('-')[2]) <= 1):
            print "�ŦX"
        else:
            print "���ŦX"
    else:
        print "���ŦX"
else:
    print "���ŦX"
