
def check_age(age):
    if age < 0:
        return "You're still a part of your parents!", age
    return "You made it through! 🙂", age

message_1, current_age = check_age(10)
message_2 = f"You are {current_age} years young!" if current_age > 0 else "You're not done yet!"
print(message_1,message_2)

message_1, current_age = check_age(2)
message_2 = f"You are {current_age} years young!" if current_age > 0 else "You're not done yet!"
print(message_1,message_2)

message_1, current_age = check_age(-2)
message_2 = f"You are {current_age} years young!" if current_age > 0 else "You're not done yet!"
print(message_1,message_2)