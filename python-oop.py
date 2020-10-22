class Car():

  def __init__(self,  **kwargs):
    print(kwargs.get)
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    #컬러 설정, default = black
    self.color = kwargs.get("color", "black")
    # 가격 설정, default = $20
    self.price = kwargs.get("price", "$20")

  #method: class안에 존재함, function아님 주의
  #모든 method의 첫번째 argument는 method를 호출하는 instance 자신
  def start(self):  
    print("I starte")

  #overrive
  def __str__(self):
    return f"Car with {self.wheels} wheels" 

#extend
class Convertible(Car):
  def take_off(self):
    print("Taking off")

  #overrive
  def __str__(self):
    return f"Car with no roof"     

  #부모단에서 override한 method에 내용 추가하기
  def __init__(self, **kwargs):
    #super() 부분이 없으면 부모의 method는 완전히 잊고 새로 override 한 셈이 됨
    #여기에는 self를 안 넣음--> 넣어보니까 argument 관련 오류 나던데.. 부모 method에서 **kwargs 부분에 적용되기 때문
    super().__init__(**kwargs)
    self.time = kwargs.get("time", 10)

#dir: class 안에 있는 모든 것들을 리스트로 보여줌
#print(dir(Car))

porche = Convertible(color = "green", price="$40")
porche.take_off()
print(porche.color)

print()

mini = Car()
print(mini.color, mini.price)