#pip install xlsxWriter
import xlsxwriter
from main2 import screenscrape
from main2 import dictionary,column_names,column2_names,column3_names


data = []
data2 = []
data3 = []
data4 = []
screenscrape('home.html')
data4.append(screenscrape('home.html'))
data3.append(dictionary(column3_names))
data2.append(dictionary(column2_names))
data.append(dictionary(column_names))



screenscrape('home2.html')
data4.append(screenscrape('home2.html'))
data3.append(dictionary(column3_names))
data2.append(dictionary(column2_names))
data.append(dictionary(column_names))



workbook = xlsxwriter.Workbook("frompyy.xlsx")
worksheet = workbook.add_worksheet("Basic Details")
worksheet2 = workbook.add_worksheet("Facilities")
worksheet3 = workbook.add_worksheet("Room Details")
worksheet4 = workbook.add_worksheet("Enrolment of Students")

# {'Class': 'No. of Students', 'Pre-Primary': '0', 'I': '0', 'II': '0', 
# 'III': '0', 'IV': '0', 'V': '0', 'VI': '11', 'VII': '14', 'VIII': '16', 
# 'IX': '10', 'X': '23', 'XI': '0', 'XII': '0', 'Class(1-12)': '74', 
# 'Class(1-12) With Pre-Primary': '74', 'Total Teachers': '7'}



worksheet4.write(0,0,'#')
worksheet4.write(0,1,'Class')
worksheet4.write(0,2,'Pre-Primary')
worksheet4.write(0,3,'I')
worksheet4.write(0,4,'II')
worksheet4.write(0,5,'III')
worksheet4.write(0,6,'IV')
worksheet4.write(0,7,'V')
worksheet4.write(0,8,'VI')
worksheet4.write(0,9,'VII')
worksheet4.write(0,10,'VIII')
worksheet4.write(0,11,'IX')
worksheet4.write(0,12,'X')
worksheet4.write(0,13,'XI')
worksheet4.write(0,14,'XII')
worksheet4.write(0,15,'Class(1-12)')
worksheet4.write(0,16,'Class(1-12) With Pre-Primary')
worksheet4.write(0,17,'Total Teachers')


for index, entry in enumerate(data4):
    worksheet4.write(index+1,0, str(index))
    worksheet4.write(index+1,1, entry['Class'])
    worksheet4.write(index+1,2, entry['Pre-Primary'])
    worksheet4.write(index+1,3, entry['I'])
    worksheet4.write(index+1,4, entry['II'])
    worksheet4.write(index+1,5, entry['III'])
    worksheet4.write(index+1,6, entry['IV'])
    worksheet4.write(index+1,7, entry['V'])
    worksheet4.write(index+1,8, entry['VI'])
    worksheet4.write(index+1,9, entry['VII'])
    worksheet4.write(index+1,10, entry['VIII'])
    worksheet4.write(index+1,11, entry['IX'])
    worksheet4.write(index+1,12, entry['X'])
    worksheet4.write(index+1,13, entry['XI'])
    worksheet4.write(index+1,14, entry['XII'])
    worksheet4.write(index+1,15, entry['Class(1-12)'])
    worksheet4.write(index+1,16, entry['Class(1-12) With Pre-Primary'])
    worksheet4.write(index+1,17, entry['Total Teachers'])
    

worksheet3.write(0,0,'#')
worksheet3.write(0,1,'Class Rooms')
worksheet3.write(0,2,'Other Rooms')

for index, entry in enumerate(data3):
    worksheet3.write(index+1,0, str(index))
    worksheet3.write(index+1,1, entry['Class Rooms'])
    worksheet3.write(index+1,2, entry['Other Rooms'])
    


worksheet2.write(0,0,'#')
worksheet2.write(0,1,'Building Status')
worksheet2.write(0,2,'Boundary Wall')
worksheet2.write(0,3,'No. of Boys Toilets')
worksheet2.write(0,4,'No. of Girls Toilets')
worksheet2.write(0,5,'No. of CWSN Toilets')
worksheet2.write(0,6,'Drinking Water Availability')
worksheet2.write(0,7,'Hand Wash Facility')
worksheet2.write(0,8,'Functional Generator')
worksheet2.write(0,9,'Library')
worksheet2.write(0,10,'Reading Corner')
worksheet2.write(0,11,'Book Bank')
worksheet2.write(0,12,'Functional Laptop')
worksheet2.write(0,13,'Functional Desktop')
worksheet2.write(0,14,'Functional Tablet')
worksheet2.write(0,15,'Functional Scanner')
worksheet2.write(0,16,'Functional Printer')
worksheet2.write(0,17,'Functional LED')
worksheet2.write(0,18,'Functional DigiBoard')
worksheet2.write(0,19,'Internet')
worksheet2.write(0,20,'DTH')
worksheet2.write(0,21,'Functional Web Cam')

for index, entry in enumerate(data2):
    worksheet2.write(index+1,0, str(index))
    worksheet2.write(index+1,1, entry['Building Status'])
    worksheet2.write(index+1,2, entry['Boundary Wall'])
    worksheet2.write(index+1,3, entry['No. of Boys Toilets'])
    worksheet2.write(index+1,4, entry['No. of Girls Toilets'])
    worksheet2.write(index+1,5, entry['No. of CWSN Toilets'])
    worksheet2.write(index+1,6, entry['Drinking Water Availability'])
    worksheet2.write(index+1,7, entry['Hand Wash Facility'])
    worksheet2.write(index+1,8, entry['Functional Generator'])
    worksheet2.write(index+1,9, entry['Library'])
    worksheet2.write(index+1,10, entry['Reading Corner'])
    worksheet2.write(index+1,11, entry['Book Bank'])
    worksheet2.write(index+1,12, entry['Functional Laptop'])
    worksheet2.write(index+1,13, entry['Functional Desktop'])
    worksheet2.write(index+1,14, entry['Functional Tablet'])
    worksheet2.write(index+1,15, entry['Functional Scanner'])
    worksheet2.write(index+1,16, entry['Functional Printer'])
    worksheet2.write(index+1,17, entry['Functional LED'])
    worksheet2.write(index+1,18, entry['Functional DigiBoard'])
    worksheet2.write(index+1,19, entry['Internet'])
    worksheet2.write(index+1,20, entry['DTH'])
    worksheet2.write(index+1,21, entry['Functional Web Cam'])


worksheet.write(0,0,'#')
worksheet.write(0,1,'School Name')
worksheet.write(0,2,'UDISE CODE')
worksheet.write(0,3,'State')
worksheet.write(0,4,'District')
worksheet.write(0,5,'Block')
worksheet.write(0,6,'Cluster')
worksheet.write(0,7,'Village')
worksheet.write(0,8,'PinCode')
worksheet.write(0,9,'School Category')
worksheet.write(0,10,'School Type')
worksheet.write(0,11,'Class From')
worksheet.write(0,12,'Class To')
worksheet.write(0,13,'State Management')
worksheet.write(0,14,'National Management')
worksheet.write(0,15,'Status')
worksheet.write(0,16,'Location')
worksheet.write(0,17,'Aff Board Sec.')
worksheet.write(0,18,'Aff Board H.Sec.')
worksheet.write(0,19,'Year of Establishment')
worksheet.write(0,20,'Pre-Primary')

for index, entry in enumerate(data):
    worksheet.write(index+1,0, str(index))
    worksheet.write(index+1,1, entry['School Name'])
    worksheet.write(index+1,2, entry['UDISE CODE'])
    worksheet.write(index+1,3, entry['State'])
    worksheet.write(index+1,4, entry['District'])
    worksheet.write(index+1,5, entry['Block'])
    worksheet.write(index+1,6, entry['Cluster'])
    worksheet.write(index+1,7, entry['Village'])
    worksheet.write(index+1,8, entry['PinCode'])
    worksheet.write(index+1,9, entry['School Category'])
    worksheet.write(index+1,10, entry['School Type'])
    worksheet.write(index+1,11, entry['Class From'])
    worksheet.write(index+1,12, entry['Class To'])
    worksheet.write(index+1,13, entry['State Management'])
    worksheet.write(index+1,14, entry['National Management'])
    worksheet.write(index+1,15, entry['Status'])
    worksheet.write(index+1,16, entry['Location'])
    worksheet.write(index+1,17, entry['Aff Board Sec.'])
    worksheet.write(index+1,18, entry['Aff Board H.Sec.'])
    worksheet.write(index+1,19, entry['Year of Establishment'])
    worksheet.write(index+1,20, entry['Pre-Primary'])

workbook.close()


# worksheet = workbook.add_worksheet("Basic Details")
# worksheet2 = workbook.add_worksheet("Facilities")