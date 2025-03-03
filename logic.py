class Cafe:
  PRICE = {
      "tea": 20.0,
      "coffee": 30.0
  }

  def __init__(self, randomly_select):
    self._randomly_select = randomly_select

  def buy(self, drink: str, paid_money: float):
    drink = self._validate_drink(drink)
    self._validate_amount_of_money(drink, paid_money)

    change = paid_money - self.PRICE[drink]
    return drink, change
  
  def _validate_amount_of_money(self, drink, paid_money):
    if self.PRICE[drink] > paid_money:
      raise NotEnoughMoney()

  def _validate_drink(self, drink):
    if drink == "surprise":
      drink = self._randomly_select(["tea", "coffee"])

    if not drink in self.PRICE:
      raise DrinkNotInMenu()
    
    return drink
    
class DrinkNotInMenu(Exception):
  pass

class NotEnoughMoney(Exception):
  pass