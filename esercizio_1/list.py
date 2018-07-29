import re
dates = ['7/12/1970','2/1/2012','5/6/2011','1/4/1983',
'4/17/1090',
'3/19/2010',
'11/11/2019',
'8/23/2022',
'6/24/1980',
'12/2/1999',
'9/6/2002',
'10/17/2011',
'9/11/2001']


dates2 = ['7-12-1970','2-1-2012','5-6-2011','1-4-1983',
'4-17-1090',
'3-19-2010',
'11-11-2019',
'8-23-2022',
'6-24-1980',
'12-2-1999',
'9-6-2002',
'10-17-2011',
'9-11-2001']

# =============================================================================
# leo = r'[Ll][Ee][Oo]'
# blah = 'lEonardo'
# if re.search(leo, blah):
#     print(blah,'it matches')
# else:
#     print('nice try')
# =============================================================================
def parseMyDate(data):
    myReg = r'(\d{1,2})[-/](\d{1,2})[-/](\d\d\d\d)'
    mygroup = re.search(myReg, data)
    giorno = mygroup.group(2)
    mese = mygroup.group(1)
    anno = mygroup.group(3)


    mesi = ['Gennaio','Febbraio','Marzo','Aprile','Maggio',
            'Giugno','Luglio','Agosto', 'Settembre',
            'Ottobre','Novembre', 'Dicembre']    
    return "{} {} {}".format(giorno, mesi[int(mese)-1], anno)
    

for date in dates2:
    print(parseMyDate(date))