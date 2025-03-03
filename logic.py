class Cafe:
  PRICE = {
      "tea": 20.0,
      "coffee": 30.0
  }

  def buy(self, drink: str, paid_money: float):
    change = paid_money - self.PRICE[drink]
    return drink, change