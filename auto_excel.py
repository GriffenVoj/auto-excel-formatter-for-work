import fitz
import xlsxwriter
import os


def convert_to_text():
    folder=os.getcwd()
    files = os.listdir()
    files = [x for x in files if x.endswith(".pdf")]
    for item in files:
        with fitz.open(item) as doc:
            print("he")
            text = ""
            for page in doc:
                text += page.get_text()
            doc_name="text{}".format(item)
            with open(f"{doc_name}.txt", "w") as f:
                f.write(text)
    return

def ckf_convert():
    files = os.listdir()
    files = [x for x in files if x.endswith(".pdf")]
    for item in files:
        page=open(item).read().splitlines()
        for line in page:
            
    pass

def dsc_convert():

    pass

def main():
    type=input("CKF or DSC?")
    type.lower()
    
    if type!="ckf" and type!="dsc":
        type=input("learn how to spell")
        type.lower()
    if type=="dsc":
        workbook=xlsxwriter.Workbook("__.xlsx")
        worksheet=workbook.add_worksheet()
        worksheet.write("A1","Sample Name" )
        worksheet.write("A2","Storage Conditions")
        worksheet.write("A3","Time Point" )
        worksheet.write("A4","Peak Onset" )
        worksheet.write("A5","Peak Temp" )
    #add name based 
    

    

    #after finish writing
    workbook.close()
    return


main()








