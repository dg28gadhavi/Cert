from fpdf import FPDF

val = input("Enter your value: ")
print(val)

class PDF(FPDF):

#Header
    def header(head):
        head.image('logo.png', 10, 10, 50)

#Sidebar
        head.image('side.png', 190, 0, 20)

#Footer
    def footer(foot):
        foot.set_y(-10)
        foot.image('footer.jpg', 0, 192, 211)

pdf = PDF('P', 'mm', 'A4')

pdf.add_page()

pdf.output('test.pdf')
