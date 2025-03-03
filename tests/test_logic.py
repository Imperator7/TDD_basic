from logic import Cafe

def test_buy_tea_with_50_baht_change_should_be_30_baht():
  cafe = Cafe()
  drink, change = cafe.buy("tea", 50.0)
  assert (drink, change) == ("tea", 30.0)