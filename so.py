import requests
from bs4 import BeautifulSoup


url = f"https://stackoverflow.com/jobs?d=20&l=us&q=python&u=Km"


def get_last_page():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  title = html.find("a", {"class":"s-link"})["title"]
  
  company = html.find("h3", {"class":"fc-black-700"}).find("span").string
  if company is not None:
    company = company.strip()
  else:
    company = None

  location = html.find("h3", {"class":"fc-black-700"}).find("span", {"class", "fc-black-500"}).string
  if location is not None:
    location = location.strip()
  else:
    location = None

  job_id = html['data-jobid']
  
  #print(company, location)
  return {
    'title':title, 
    'company':company, 
    'location':location, 
    'link':f"https://stackoverflow.com/jobs/{job_id}"
  }


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{url}&pg={page+1}")
    #print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs