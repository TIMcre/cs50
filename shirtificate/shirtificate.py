from fpdf import FPDF

name = str(input("Name: ")) + " took CS50"
pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 30)

pdf.cell(0, 60, "CS50 Shirtificate", align="C")

#pdf.image("shirtificate.png", x="C")


pdf.cell(0, 120, name, align="C", center=True)


pdf.output("shirtificate.pdf")
