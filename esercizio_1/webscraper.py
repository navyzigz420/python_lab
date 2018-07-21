# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:52:37 2018

@author: Luca Passani
"""

import requests
import re
 
# I couldn't find a straight way to pretty print the tuple without messing
# with the pprint module. Wrote my own little function instead 
def prettyTuple(mytup):
    mystring = ""
    for i in range(len(mytup)):
        mystring = mystring+str(mytup[i])
        if i < len(mytup) -1:
            mystring = mystring+","
    mystring = mystring+"\n"
    return mystring

base_url = 'https://countrycode.org/'
r = requests.get(base_url)
html = r.text

lines = html.split("\n")

relevant = [l for l in lines if "<t" in l or "</t" in l]

#parsing the relevant lines
status= "start"
current_record = []

#regular expressions to parse the right HTML table cell
re_country = r'<td><a href="/(\w+)">([\w\-\. ]+)</a></td>'
re_countrycode = r'<td>([\d\-]+)</td>'
re_isocode = r'<td>([A-Z\/ ]+)</td>'
re_inhabitants = r'<td>([\d,]+)</td>'
re_area = r'<td>([\d,]+)</td>'
re_gdp = r'<td>([\d\.]+) (Million|Billion|Trillion)</td>'


field_counter = 0
all_data = []
header = ("Country","Country Code","ISO Codes","Population","Area","GDP")
all_data.append(header)

for line in relevant:
    
    if status == "start":
        
        #new tr = new record
        if "<tr>" in line:
            status = "new record"
            continue
        
        #end of tr tag = end of record
        if "</tr>" in line:
            status = "start"
            field_counter = 0
            current_record = []
            continue
        
        # Html contains repetition of two tables.
        # One is enough. end of table signals when we can stop
        if "</table>" in line:
            break
        
    if status == "new record":
        if "<td>" in line:
            #print(line)
            #country name
            if field_counter == 0:
                match = re.search(re_country, line)
                #print(match.group(2))
                if match and match.group(2):
                    current_record.append(match.group(2))
                field_counter = 1
                continue
            
            #country code
            elif field_counter == 1:
                match = re.search(re_countrycode, line)
                #print(match.group(1))
                if match and match.group(1):
                    current_record.append(match.group(1))
                else:
                    current_record.append("")
                field_counter = 2
                continue
            
            #iso code
            elif field_counter == 2:
                match = re.search(re_isocode, line)
                #print(match.group(1))
                if match and match.group(1):
                    current_record.append(match.group(1))
                else:
                    current_record.append("")
                field_counter = 3
                continue
            
            #inhabitants
            elif field_counter == 3:
                match = re.search(re_inhabitants, line)
                #print(match.group(1))
                if match and match.group(1):
                    #current_record.append(match.group(1))
                    #let's remove commans and turn into an int
                    current_record.append(int(match.group(1).replace(",","")))
                else:
                    current_record.append(0)
                field_counter = 4
                continue        
            
            #area
            elif field_counter == 4:
                match = re.search(re_area, line)
                #print(match.group(1))
                if match and match.group(1):
                    #current_record.append(match.group(1))
                    #let's remove commans and turn into an int
                    current_record.append(int(match.group(1).replace(",","")))
                else:
                    current_record.append(0)
                field_counter = 5
                continue        
            
            #GDP
            elif field_counter == 5:
                match = re.search(re_gdp, line)
                #print(match.group(1))
                if match and match.group(1) and match.group(2):
                    multiplier = 1
                    if "Trillion" in match.group(2):
                        multiplier = 1000000
                    if "Billion" in match.group(2):
                        multiplier = 1000
                    amount = float(match.group(1)) * multiplier
                    current_record.append(int(amount))
                    #let's remove commans and turn into an int
                    #current_record.append(int(match.group(1).replace(",","")))
                else:
                    current_record.append(0)
                continue        
            
            
            else:
                continue
                
        if "</tr>" in line:
            #print(current_record)
            if len(current_record) < 6: #only add complete records
                #print("discarding "+str(current_record))
                pass
            else:
                record = tuple(current_record)
                all_data.append(record)
            status = "start"
            field_counter = 0
            current_record = []
            continue

#let's write data into a file
with open("countrydata.csv","w") as f:
    for el in all_data:
        f.write(prettyTuple(el))
        
        
        