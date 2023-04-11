def calculate_discount(price, discount_percent):
    discount_amount = price * discount_percent / 100
    discountprice = price - discount_amount
    return discountprice
print(calculate_discount(1000,20))