
from kivy.uix.widget import Widget
from fpdf import FPDF
import datetime

class DisplayTicket(Widget):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Purchase')
    time = datetime.datetime.now()
    pdf.output(f'bill_{time}_purchase.pdf', 'F')