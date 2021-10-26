from fpdf import FPDF
from datetime import datetime
#import random
import time
import os


name = input("Enter the Company Name: ")
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

pdf.output(name+'.pdf')
