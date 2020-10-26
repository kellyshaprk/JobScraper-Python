'''
import csv

def save_to_file(word, jobs):
  file_name = f"jobSearch_{word}.csv"
  file = open(file_name, mode="w", encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(["Title", "Company", "Location", "Link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return
'''

import xlsxwriter

def save_to_file(word, jobs):
  file_name = f"jobSearch_{word}.xlsx"
  wb = xlsxwriter.Workbook(file_name)
  sheet = wb.add_worksheet()
  title_format = wb.add_format({"bold" : True})
  title_format.set_align("center")
  title_format.set_font_size(12)
  cell_format = wb.add_format()
  cell_format.set_pattern(1)
  cell_format.set_bg_color("yellow")

  sheet.set_column("A:A", 30)
  sheet.set_column("B:B", 30)
  sheet.set_column("C:C", 15)
  sheet.set_column("D:D", 40)
  sheet.write("A1", "Title", title_format)
  sheet.write("B1", "Company", title_format)
  sheet.write("C1", "Location", title_format)
  sheet.write("D1", "Link", title_format)

  sheet.freeze_panes(1, 0)

  for i in range (0, len(jobs), 1):
    
    sheet.write(i+1, 0, jobs[i].get('title'))
    sheet.write(i+1, 1, jobs[i].get('company'))
    sheet.write(i+1, 2, jobs[i].get('location'))
    sheet.write(i+1, 3, jobs[i].get('link'))


  wb.close()


  return