
age = input("What is your current age?\n")
life_exp = input("What is the age at which you think you will die?\n")
life_exp_new = int(life_exp)
age_new = int(age)
time_left = life_exp_new - age_new
days_in_year = 365
weeks_in_year = 52
months_in_year = 12
days_left = time_left * days_in_year
weeks_left = time_left * weeks_in_year
months_left = time_left * months_in_year
display_message = ("You have " + str(days_left) + " days, " + str(weeks_left) + " weeks, and " + str(months_left) + " months left.")
print(display_message)
print("Use your time well.")