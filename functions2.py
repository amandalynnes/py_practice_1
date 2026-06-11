# def add(a,b):
#     result = a + b
#     return result

# sum_value = add(2,3)
# print(sum_value)

# def dollars_to_cents(a):
#     result = a * 100
#     message = f"${result:.2f}"
#     print(message)
#     return result

# sum_value = dollars_to_cents(5.00)

def apply_tax(price):
    percent = 15 / 100
    tax = price * (percent)
    total = price + tax
    dollar_amount = f"${total:.2f}"
    print(tax)
    print(dollar_amount)
    return dollar_amount

apply_tax(10.00)
apply_tax(20.30)
apply_tax(15.55)
apply_tax(36.50)

before_tip = apply_tax(27.00)
print(before_tip)