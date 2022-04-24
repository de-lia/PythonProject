house_price = 1000000
buyer_has_good_credit = False
if buyer_has_good_credit:
    down_payment = int(house_price) * 0.1
else:
    down_payment = int(house_price) * 0.2
print(f"Down_payment: ${down_payment}")