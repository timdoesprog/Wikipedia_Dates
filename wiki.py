# 06.03.2017
# let the user input a date and
# return the link to a wikipedia page about that date

import datetime

answer_format = "%m/%d"  # 12/24 -> December 24th
link_format = "%b_%d"    # 12/24 -> Dec_24
link = "https://en.wikipedia.com/wiki/{}"

while True:
    answer = input("""What date would you like to look up?
Use the format: MM/DD
Enter 'quit' to quit.\n""")
    if answer == "quit":
        break
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("That's not a valid date. Please try again.")
