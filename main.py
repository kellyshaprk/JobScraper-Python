#request를 통해서 home.html에서 사용자가 입력한 단어를 추출하고 사용할 수 있음
from flask import Flask, render_template, request, redirect

from scraper import get_jobs as get_indeed_jobs
#from so import get_jobs as get_so_jobs
#from save import save_to_file

#indeed_jobs = get_indeed_jobs()
#so_jobs = get_so_jobs()
#save_to_file(indeed_jobs)

app = Flask("SuperScraper")
db = {}

# @<- decorator
# 데코레이터는 바로 밑에 명시된 함수를 실행시킴. 때문에 route의 페이지 이름과 함수명이 같을 필요는 없음 
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()

    #job 정보를 db에 저장해놓고, 동일한 요청이 들어오면 db에서 읽어서 보여주고 아니면 새로 검색하기
    fromDb = db.get(word)
    if fromDb:
      jobs = fromDb
    else:
      jobs = get_indeed_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html"
  , searchingby=word
  , resultNumber=len(jobs)
  )

# <> means placeholder
@app.route("/<username>") 
def potato(username):
  return f"Hey, {username}"

#repl에서 사용하기 위한 host주소임, local에선 안먹힘
app.run(host="0.0.0.0")