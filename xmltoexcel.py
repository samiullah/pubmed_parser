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
    dictList = []
    affiliations = list()
    if tree.xpath('//AffiliationInfo/Affiliation') is not None:
        for affil in tree.xpath('//AffiliationInfo/Affiliation'):
            affiliations.append(affil.text)
            affiliations_text = '; '.join(affiliations)

    authors_tree = tree.xpath('//AuthorList/Author')
    authors = list()
    if authors_tree is not None:
        for a in authors_tree:
            firstname = a.find('ForeName').text if a.find('ForeName') is not None else ''
            lastname = a.find('LastName').text if a.find('LastName') is not None else ''
            fullname = (firstname + ' ' + lastname).strip()
            if fullname == '':
                fullname = a.find('CollectiveName').text if a.find('CollectiveName') is not None else ''
            authors.append(fullname)
        authors_text = '; '.join(authors)
    else:
        authors_text = ''

    dict_out = {
    'authors': authors_text,
    'affiliation': affiliations_text}

    x= dict_out['authors'].split(';')
    print (x)
    y = dict_out['affiliation'].split(';')

    newl = list()
    print(type(newl))
    pattern = r"[\w.]+@[\w.]+"
    for item in y:
        if re.findall(pattern,item):
            newl.append(item)
        else:
            newl.append("noemail@mailinator.com")

    d=[x,newl]
    export_data = zip_longest(*d, fillvalue = '')
    file = 'numbers.csv'
    with open(file, 'w', encoding="utf8", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("Author", "Email"))
        wr.writerows(export_data)
    myfile.close()


  
      
parse_authors(tree)

print("***** Parsing Complete *****")







# re_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')

# with open("test.csv") as fh_in:    
#     with open("mailout.csv", "a+") as fh_out:
#         for line in fh_in:
#             match_list = re_pattern.findall(line)
#             if match_list:
#                 fh_out.write(match_list[0]+"\r\n") 

# #count the number of emails scrapped
# reader=csv.reader(open("mailout.csv"))
# count=0
# for row in reader:
#     count+=1
#     print "total no in row "+str(count)+" is "+str(len(row))
#     for i in row:
#         print (i)


