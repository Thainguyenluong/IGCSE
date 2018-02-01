name = input("Please enter your name:")
print("Well hello,", name,",what a nice name you have")

if name.find('s')or name.find("S") > 0:
    print("did you know you have an 's' in your name?")
    # It is important to use the tab key for any instructions that need to happen only if the above condition is true
    # This is how Python knows which bits of your code need to be run in which order.
else:
    print("There's no 's' in your name!")

country = input("please tell me what country you're from... ")
nexta = input("Shall I tell you the capital? Please write 'y' or 'n'.")
if nexta == "y" or nexta == "Y":
    print("the capital of", country, "is...", country.upper()[0], "! Aren't I clever ;)?")
elif nexta == "n" or nexta == "N":  # elif stands for else, if - it's shorter!
    print("oh go on.")				# to understand how this works, try to run the program and get all of these outputs.
else:
    print("I didn't understand that...")
