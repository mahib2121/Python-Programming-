# # write operarion  
# file = open("Std_list.txt", "w")
# text = "Hello Mahib,we area learining python "
# file.write(text)
# file.close()
# # read operation r
# file = open("Std_list.txt", "r")
# print(file.read())
# file.close()
# # append operation a
# file = open("Std_list.txt", "a")
# text = """
# I love BD
# i love Canada
# i love UAE
# i love UK
# I love USA
# """
# file.write(text)
# file.close()
# # again read operration AFTER update
# file = open("Std_list.txt", "r")
# print(file.read())
# file.close()
# # add list in text document
# file = open("bazar.text", "a")
# list = ["fualkopi", "Alu", "Potol", "tomato"]
# file.write(str(list))
# file.close()
# pdf reading

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
value = " Hello form pdf "
pdf.cell(300, 10, txt=value, align="L")
pdf.output("student.pdf")
