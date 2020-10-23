from flask import Flask, render_template

app = Flask("SuperScraper")

# @<- decorator
# 데코레이터는 바로 밑에 명시된 함수를 실행시킴. 때문에 route의 페이지 이름과 함수명이 같을 필요는 없음 
@app.route("/")
def home():
  return render_template("home.html")




#repl에서 사용하기 위한 host주소임, local에선 안먹힘
app.run(host="0.0.0.0")