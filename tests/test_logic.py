from logic import Cafe

def test_buy_tea_with_50_baht_change_should_be_30_baht():
  cafe = Cafe()
  drink, change = cafe.buy("tea", 50.0)
  assert (drink, change) == ("tea", 30.0)

def test_should_return_coffee_and_the_change_of_70_baht_when_buying_coffee_with_100_baht():
  cafe = Cafe()
  drink, change = cafe.buy("coffee", 100.0)
  assert (drink, change) == ("coffee", 70.0)