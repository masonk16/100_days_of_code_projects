#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Prompt user input
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give?\n"))
number_of_people = int(input("How many people are splitting the bill?\n")) 

#Convert strings
# total_as_float = float(total_bill)
# percentage_as_int = int(tip_percentage)
# people_as_int = int(number_of_people)

#Calculate bill including tip
tip = (total_bill / 100) * tip_percentage
final_bill = total_bill + tip

#Claculate each persons share
individual_share = "{:.2f}".format(final_bill / number_of_people)

#Print results
print (f"Total tip: ${tip}")
print (f"Total bill including tip: ${final_bill}")
print(f"Each person should pay: ${individual_share}")

