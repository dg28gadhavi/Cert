from fpdf import FPDF
from datetime import datetime
import random
import time
import os
import sys
import csv


print("************Welcome to TEST & CALIBRATION CERTIFICATE Demo**************")
print('')
print('')
name = input("Enter the Company Name: ")
add = input("Enter the Company Address: ")
print("Generating Your TEST Certificates......")
print("Cetificates for", name, "are being Generated.")

#TimeStamp/DateStamp
time = datetime.today().strftime('%d-%m-%Y')
time = str(time)
print (time)

#print(round(random.uniform(-0.5,5),1))

#Make and Change the Current Working Directory for the output file.
os.mkdir(name+"["+time+"]")
os.chdir(name+"["+time+"]")

class PDF(FPDF):

#Header
    def header(head):
        head.image('../logo.png', 10, 10, 50)

#Sidebar
        head.image('../side.png', 190, 0, 20)

#Footer
    def footer(foot):
        foot.set_y(-10)
        foot.image('../footer.jpg', 0, 192, 211)

pdf = PDF('P', 'mm', 'A4')

pdf.add_page()

#Body
pdf.set_font('helvetica', 'B', 19)
pdf.cell(180, 15, 'TEST & CALIBRATION CERTIFICATE', 0, True, 'R')

#Rectangle
#for i in range(1):
#    pdf.set_fill_color(255 - 15*i)
 #   pdf.rect(x=5+5*i, y=35+5*i, w=200-10*i, h=20-10*i, style="FD")

pdf.set_font('helvetica', '', 12)
#pdf.cell(180, 35, 'Company Name:'+name, 0, True, 'L')
#pdf.cell(180, -20, 'Company Address:'+add , 0, True, 'L')
#pdf.cell(180, -37, 'Date:'+time, 0, True, 'R')



#Start1
 # Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content 
# evenly across table and page
col_width = epw/1

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.

data = [['Company Name: '+name],
        ['Address: '+add],
        ['Name of Instrument: RTD (Pt-100) Simplex']
]

# Document title centered, 'B'old, 14 pt
pdf.set_font('Times','B',14.0) 
pdf.cell(epw, 20.0, '', align='C')
pdf.set_font('Times','',10.0) 
pdf.ln(20)

# Text height is the same as current font size
th = pdf.font_size

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2*th, str(datum), border=1)

    pdf.ln(2*th)
 
#Start2
# Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content 
# evenly across table and page
col_width = epw/2

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.

data = [['Identification No.: ','Date of Issue: '],
['Date of Calibration: ','Suggested Due Date: '],
        ['Make: ' ,'Range: '],
        ['Environment Condition: ' ,'Client Reference: ']
        
]



# Text height is the same as current font size
th = pdf.font_size

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2*th, str(datum), border=1)

    pdf.ln(2*th)

#Start3
# Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content 
# evenly across table and page
col_width = epw/1

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.

data = [['Identification No.: ']
        
]



# Text height is the same as current font size
th = pdf.font_size

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 8*th, str(datum), border=1)

    pdf.ln(8*th)


pdf.output(name+'.pdf')
