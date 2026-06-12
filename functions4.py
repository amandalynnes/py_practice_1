# def morning_register(till, num):
#     total = till
#     return total, num

# def evening_register(till, num):
#     total = till
#     return total, num

# morning_total, morning_count = morning_register(5000.00, 1)
# evening_total, evening_count = evening_register(7000.00, 1)
# count = morning_count + evening_count
# print(count)

# while count:
#     if count > 1:
#         money_usd = f"${morning_total:.2f}" 
#         count -= 1
#         print(money_usd)

#     else:
#         money_usd = f"${evening_total:.2f}"
#         count -= 1
#         print(money_usd)
 


def apply_discount(price, rate):
    discount = price * rate
    discounted_price = price - discount
    print(discounted_price)
    return discounted_price



final_total = apply_discount(150, 0.2)
print(final_total)

def print_usd(final_total):
    usd_money = f"${final_total:.2f}"
    print(usd_money)
    return usd_money

print_usd(final_total)

final_total = apply_discount(300, 0.24)
print_usd(final_total)


