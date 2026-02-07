to_do_list = ["Buy Groceries", "Clean the house", "Pay Bills"]
to_do_list.append("Schedule Meeting")
to_do_list.append("Go for a run")
to_do_list.remove("Pay Bills")

#Checking if a task is in list
if "Pay Bills" in to_do_list:
    print("Pay Bills is still pending")
else:
    print("Pay Bills is completed")

print("TO do list remaining : -> ")
for item in to_do_list:
    print(f" - {item}")
