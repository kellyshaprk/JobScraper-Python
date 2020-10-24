import csv

def save_to_file(word, jobs):
  file_name = f"jobSearch_{word}.csv"
  file = open(file_name, mode="w", encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return