import time
import webbrowser

again = "y"
break_limit = 3
break_count = 0
remaining = break_limit

while again == "y" and break_count < break_limit:
    time.sleep(3) # seconds
    print("You have %s remaining breaks to take advantage of!") % (remaining)
    if remaining == break_limit:
        print("Note: Don't let the client perceive you to be working too hard as their expectations will increase and your colleagues won't like it.")
    again = raw_input("Take another break? y/n >>>")
    if again != "y":
        print("Come back to a sustainable workplace with a flexible working hours  with breaks to give you a work life balance...")
    else:
        webbrowser.open("https://stackoverflow.com/users/3208553/luke-schoen")
        break_count += 1
        remaining -= 1
print("Unfortunately we'll have to let you go as you took your allocated breaks but we actually don't have the budget for that, sorry...")


