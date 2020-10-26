import requests
from bs4 import BeautifulSoup


limit = 50


def get_jobs(word):
  url = f"https://ca.indeed.com/jobs?q={word}&l=alberta&limit={limit}"
  last_page = extract_indeed_pages(url)
  jobs = extract_indeed_jobs(last_page, url)
  return jobs

def extract_indeed_pages(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
 
  pagination = soup.find("ul", {"class":"pagination-list"})
  if pagination is None:
    return 1
  else :
    links = pagination.find_all("a")
    pages = []
    for link in links[0:-1]:
      pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page, url):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping indeed page {page}")
    result = requests.get(f"{url}&start={page*limit}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

    for result in results:
      job = extract_jobs(result)
      jobs.append(job)
  return jobs
  
def extract_jobs(html):
    title = html.find("h2", {"class", "title"}).find("a")["title"]
    company = html.find("span", {"class":"company"})
    
    if company:
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = str(company_anchor.string)
      else:
        company = str(company.string)
      company = company.strip()
    else:
      company = None
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
      'title':title, 
      'company':company, 
      'location' : location, 
      'link':f"https://ca.indeed.com/viewjob?jk={job_id}"
    }

