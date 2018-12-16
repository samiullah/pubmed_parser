import os
import glob
import csv
from importlib import reload
import re
import io
import sys
reload(sys)
from lxml import etree as ET
from lxml import html
import ast

try:
    from itertools import zip_longest as zip_longest
except:
    from itertools import izip_longest as zip_longest
dictList = []

print("***Getting the latest pubmed xml downloaded file*****")

#get the latest file with xml extension downloaded from pubmed
files_path = os.path.join('/Users/srijan/Downloads','*.xml')
files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True
)
print("*** File is located at " + files_path)

#print the file path
xml_file = files[0]
print('************************')

print('***** Parsing Begins now *******')
tree = ET.parse(xml_file)
root = tree.getroot()




#name csv file as searchterm+timestamp


def parse_authors(tree):
    # global affiliations_text
    dictList = []
    affiliations = list()
    naam = list()


    authors_tree = tree.xpath('//AuthorList/Author')
    authors = list()
        
    for each in root.findall('.//AuthorList/Author'):
        aff = each.find('.//AffiliationInfo/Affiliation');
        auth = each.find('.//ForeName');

        if aff is not None and auth is not None:
           
            lst = re.findall('\S+@\S+',aff.text)
   
            affiliations.append(lst)
            naam.append(auth.text)
            values = ",".join(map(str, affiliations))
            affiliations_text = values

    

    
    print(affiliations)

       

    m=ast.literal_eval(affiliations_text)
   
    # print(authors_text)

    for item in m:
        if len(item) == 0:
            print('No Email')
        else:
            print(item)

    dict_out = {
    'authors': naam
    #'affiliation': m
    }

    x= dict_out['authors']

    # we need to remove noemail keep null
    # only email address
    # we need to remove duplicate email addresses
    # if record>9000  =>add custom range
    # make record <9000 for custom range
    # Rename files
    # count xml files 
    # append all data to csv to only one files
    # csv filename shd have date range
    # dnt allow duplicate data

    #write code for sending emails based on number of emails based on number



    d=[x,m]
    export_data = zip_longest(*d, fillvalue = '')
    file = 'numbers.csv'
    with open(file, 'w', encoding="utf8", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("Author","Email Address"))
        wr.writerows(export_data)
    myfile.close()



  
      
parse_authors(tree)

print("***** Parsing Complete *****")