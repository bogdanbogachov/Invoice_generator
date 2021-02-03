import openpyxl
import quick
import interface
import subprocess

quick.main()

theFile = openpyxl.load_workbook('template.xlsx')

theFile["Sheet1"]["B1"] = quick.summary
theFile["Sheet1"]["B2"] = quick.location
theFile["Sheet1"]["B3"] = quick.start_time
theFile["Sheet1"]["B4"] = quick.end_time

theFile.save(filename = 'New_Invoice.xlsx')

subprocess.Popen(['New_Invoice.xlsx'], shell=True)