Subject1=int(input('Enter score between (0-100)'))
Subject2=int(input('Enter score between (0-100)'))
Subject3=int(input('Enter score between (0-100)'))
average= (Subject1+Subject2+Subject3)/3

if (average>80):
    print('Grade A')
if (average>70):
    print('Grade B')
if (average<69):
    print('Grade F')

