class Car():

  def __init__(self,  **kwargs):
    print(kwargs.get)
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    #�÷� ����, default = black
    self.color = kwargs.get("color", "black")
    # ���� ����, default = $20
    self.price = kwargs.get("price", "$20")

  #method: class�ȿ� ������, function�ƴ� ����
  #��� method�� ù��° argument�� method�� ȣ���ϴ� instance �ڽ�
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

  #�θ�ܿ��� override�� method�� ���� �߰��ϱ�
  def __init__(self, **kwargs):
    #super() �κ��� ������ �θ��� method�� ������ �ذ� ���� override �� ���� ��
    #���⿡�� self�� �� ����--> �־�ϱ� argument ���� ���� ������.. �θ� method���� **kwargs �κп� ����Ǳ� ����
    super().__init__(**kwargs)
    self.time = kwargs.get("time", 10)

#dir: class �ȿ� �ִ� ��� �͵��� ����Ʈ�� ������
#print(dir(Car))

porche = Convertible(color = "green", price="$40")
porche.take_off()
print(porche.color)

print()

mini = Car()
print(mini.color, mini.price)