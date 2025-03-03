from pytest import raises
from logic import Cafe, DrinkNotInMenu, NotEnoughMoney

def test_buy_tea_with_50_baht_change_should_be_30_baht():
  cafe = Cafe(randomly_select = RandomlySelectMock())
  drink, change = cafe.buy("tea", 50.0)
  assert (drink, change) == ("tea", 30.0)

def test_should_return_coffee_and_the_change_of_70_baht_when_buying_coffee_with_100_baht():
  cafe = Cafe(randomly_select = RandomlySelectMock())
  drink, change = cafe.buy("coffee", 100.0)
  assert (drink, change) == ("coffee", 70.0)

def test_shoud_raise_DrinkNotInMenu_when_buying_cocoa():
  cafe = Cafe(randomly_select = RandomlySelectMock())
  with raises(DrinkNotInMenu):
    cafe.buy("cocoa", 50.0)

def test_should_raise_NotEnoughMoney_when_buying_coffee_with_1_baht():
  cafe = Cafe(randomly_select = RandomlySelectMock())
  with raises(NotEnoughMoney):
    cafe.buy("coffee", 1.0)

def test_should_return_random_drink_and_the_change_correctly_when_buying_surprise_with_40_baht():
  randomMock = RandomlySelectMock(return_value = "coffee")
  cafe = Cafe(randomly_select = randomMock)
  cafe.buy("surprise", 40.0)
  assert randomMock.is_called_with_choices == ["tea", "coffee"]

def test_should_use_randomly_selected_drink_when_buying_surprise():
  randomMock = RandomlySelectMock(return_value ="tea")
  cafe = Cafe(randomly_select=randomMock)
  drink, _ = cafe.buy("surprise", 40.0)
  assert drink == "tea"

class RandomlySelectMock:
  def __init__(self, return_value=None):
    self._return_value = return_value

  def __call__(self, choices):
    self.is_called_with_choices = choices
    return self._return_value
    