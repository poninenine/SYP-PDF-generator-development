from fpdf import FPDF
import os
from datetime import date

# Base directory used to retrieve images for template
b_dir = os.getcwd()

# Date of appraisal
today = date.today()
today_pretty = today.strftime("%B %d, %Y")

# Example listing
listing = {
    "Owner":"Owen Houseguy",
    "Address":"123 Road St",
    "Price":400,
    "Image path":b_dir + '/PDF generator/house1.webp',
}

#example comp
comp = {
    "Owner":"Owen Otherhouseguy",
    "Address":"124 Road St",
    "Price":401,
    "Image path":b_dir + '/PDF generator/house2.webp',
}

class PDF(FPDF):
    def header(self):
        # House
        self.image(b_dir + '/PDF generator/house.png', 0, 0, 50)
        # Printing REALM        
        self.set_font('arial', 'B', 16)
        self.cell(29,65,'REALM.',align='C')
        # Line break
        self.ln()
    
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("arial", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="R")

# Creating pdf object
pdf = PDF('P', 'mm', 'A4')

# Setting auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Page 1
pdf.add_page()

# Setting font
pdf.set_font('arial', 'B', 20)

# Text
#pdf.cell(0,30)

# Creating space from top
# num_lines = 10
# for i  in range(0,num_lines):
#     pdf.cell(txt=' ', new_x="LMARGIN", new_y="NEXT")


pdf.set_y(60)

pdf.cell(0,0,'HOME APPRAISAL REPORT', align='C', new_x="LMARGIN", new_y="NEXT")
# pdf.cell(0,0,'This is a test ' + listing['Address'])
pdf.ln()
pdf.ln()
pdf.image(listing['Image path'],w=pdf.epw/1.5,x=pdf.epw/4-6)

pdf.write_html("""
    <br>
    <br>
    <center><h3>Owner's name:   """ + listing["Owner"] + """</h3>
    <center><h3>Address:   """ + listing["Address"] + """</h3>
    <center><b><h3><u>Estimated price:   $""" + str(listing["Price"]) + """</u></h3></b>
    <center><h3>Date of appraisal:</h3>
    <center><h3>""" + today_pretty + """</h3>
""")

pdf.add_page()
pdf.set_font('arial', 'B', 16)
pdf.set_y(60)

pdf.cell(0,0,'Example comparable property 1', align='C', new_x="LMARGIN", new_y="NEXT")

pdf.ln()
pdf.ln()
pdf.image(comp['Image path'],w=pdf.epw/1.5,x=pdf.epw/4-6)

pdf.write_html("""
    <br>
    <br>
    <center><h3>Address:   """ + comp["Address"] + """</h3>
    <center><h3>Proximity to Subject:   0.12 km</h3>
    <center><h3>Price:   $""" + str(comp["Price"]) + """</h3>
    <center><h3>Age, features, etc...</h3>
""")

pdf.output('./Report.pdf')