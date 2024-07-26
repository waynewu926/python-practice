from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon:\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = datetime.strptime(input_list[1], "%d.%m.%Y")
today = datetime.today()

output = (deadline - today).days

print(f"The remaining time for your goal '{goal}' is {output} days")
