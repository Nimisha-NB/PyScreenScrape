from bs4 import BeautifulSoup
import json

enrol_names = ['Pre-Primary','I','II','III','IV','V','VI','VII','VIII','IX','X',
    'XI','XII','Class(1-12)','Class(1-12) With Pre-Primary']
column_names = ['School Name','UDISE CODE','State','District','Block','Cluster','Village',
    'PinCode','School Category','School Type','Class From','Class To','State Management',
    'National Management','Status','Location','Aff Board Sec.','Aff Board H.Sec.','Year of Establishment','Pre-Primary' ]
column2_names = ['Building Status','Boundary Wall','No. of Boys Toilets','No. of Girls Toilets','No. of CWSN Toilets',
    'Drinking Water Availability','Hand Wash Facility','Functional Generator','Library','Reading Corner',
    'Book Bank','Functional Laptop','Functional Desktop','Functional Tablet','Functional Scanner','Functional Printer','Functional LED',
    'Functional DigiBoard','Internet','DTH','Functional Web Cam']
column3_names = ['Class Rooms','Other Rooms']
nope = ['Facilities','Room Details','Enrolment of The Students','Note','Basic Details']

def dictionary(column):
    main_dict = {}
    
    for detail in data_list:
        #if keys are in column_names and values are not in column_names and nope
        if detail in column and data_list[data_list.index(detail)+1] not in column and data_list[data_list.index(detail)+1] not in nope:
            #values are the next elements' to column_names
            main_dict[detail]=data_list[data_list.index(detail)+1]
        # if keys are in column_names and values are in nope OR values are in column_names
        elif (detail in column and data_list[data_list.index(detail)+1] in nope) or (detail in column and data_list[data_list.index(detail)+1] in column):
            # values are empty strings to those keys
            main_dict[detail]=' '
    return (main_dict)

def screenscrape(htmlfile):
    with open(htmlfile,'r') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content , 'lxml')
        stuff2 = soup.find_all('div', class_ = "card mt-2 mb-5")
        for j in stuff2:
            details2 = j.text.replace('\n',' ').replace('\t',' ').replace(':',' ')


    json_file = json.dumps(details2)
    # print(json_file)
    temp=[]
    for i in json_file.split('  '):
        temp.append(i.strip())
    global data_list
    data_list=[]
    for element in temp:
        if element in ['','"','\'']:
            pass
        else:
            data_list.append(element)

    # print(data_list)
    # print(enrol_list[::-1][-2].split('No. of Students')[-1].split())
    # print(enrol_list[::-1])
    


    # for the last enrolment of students
    enrol_list = []
    for enrolment in range(100):
        if data_list[::-1][enrolment]!='Enrolment of The Students':
            enrol_list.append(data_list[::-1][enrolment])
        else:
            break
    
    enrol_dict = {'Class':'No. of Students'}
    for num in range(15):
        enrol_dict[enrol_names[num]]=enrol_list[::-1][-2].split('No. of Students')[-1].split()[num]
    enrol_dict['Total Teachers'] = enrol_list[0].split()[-1]
    # for detail in enrol_names:
    #             enrol_dict[detail]=enrol_list[::-1][-2].split('No. of Students')[-1].split()[num]
        
    return(enrol_dict)
    # print(enrol_list[0].split()[-1]) 

