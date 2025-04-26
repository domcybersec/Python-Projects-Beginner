import pprint

# this is just a quick program to count the number of individual characters in a message and add them to a dictionary 

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# have a dictionary where the key is the character in 'message' and the value is the number of times that key has occured 
count = {}
# try creating a for loop that will iterate through message and and add all of the characters to 'count' via .setdefault
for i in message.upper():
    if count.get(i, 'N/A') == 'N/A':
        count.setdefault(i, 1)
    else:
        count[i] += 1
# this worked and now I have all the characters
# I now need to create an 'if' statement to allow me to adjust the value if it is repeated more than once
pprint.pprint(count)
# pprint (pretty print) will allows you to more cleanly print out the info