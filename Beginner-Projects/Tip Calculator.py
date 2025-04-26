# creating a program that will calculate the tip and split it among the people there and based off the total bill 

# first give the initial message
print('Welcome to the Tip Calculator!')

# ask for the total number of the bill, and then how many people are there.
total_bill = input('What was the total price of the bill?\n$')
total_people = input('How many people are splitting it?\n')
# check if this will make the input str or int
# print(type(total_bill)) # they are str

# ask them how much they want to tip
tip_percentage = input('What percentage would you like to tip for your part?\n')

# now create a new amount that is based on how it is split
new_amount = float(total_bill) / int(total_people)

# multiply this by the percent amount to now get the tip number
tip_amount = float(tip_percentage) / 100

individual_amount = round((float(new_amount) * float(tip_amount) + float(new_amount)), 2)

# tell them what their tip amount would be. 
print(f'That\'s good to know. Based off of {tip_percentage}% tip added to a bill of ${total_bill}, and split among {total_people}, your portion will come out to be ${individual_amount}')