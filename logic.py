class Cafe:
  def __init__(self):
    self.drinks = ["tea", "milktea"]

  def buy(self, drink: str, paid_money: float):
    if drink == "tea":
      change = paid_money - 20.0
    
    return drink, change