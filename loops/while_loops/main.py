start_number = 5
countdown_values = []

current_number = start_number

while current_number > 0:
    countdown_values.append(current_number)
    current_number -= 1
    print (f"Discount countdown complete! {current_number}")
    print (countdown_values)