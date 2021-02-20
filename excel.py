import openpyxl
import quick
import interface
import subprocess
import os

quick.main()

# Finding the current folder path
folder = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(folder, "template.xlsx")

theFile = openpyxl.load_workbook(template_path)

theFile["Sheet1"]["B1"] = quick.summary
theFile["Sheet1"]["B2"] = quick.location
theFile["Sheet1"]["B3"] = quick.start_time
theFile["Sheet1"]["B4"] = quick.end_time

theFile.save(filename = 'New_Invoice.xlsx')

subprocess.Popen(['New_Invoice.xlsx'], shell=True)