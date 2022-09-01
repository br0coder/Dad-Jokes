import requests
from random import choice
from termcolor import colored
from pyfiglet import figlet_format


def jokes(term):

    url = "https://icanhazdadjoke.com/search"
    r = requests.get(
        url,
        headers={
            "Accept": "application/json"},
        params={
            "term": term,
            "limit": 30})
    # json requests received in dict data structure (format)
    data = r.json()
    joke_in_lst = [x["joke"] for x in data["results"]]
    total_jokes = data["total_jokes"]

    if total_jokes:
        joke = choice(joke_in_lst)
        if total_jokes > 1:
            print(f"\nI've got {total_jokes} jokes. Here's one: \n\n{joke}")
        # total_jokes ==1 or total_joke == 0
        else:
            print(f"\nI've got only 1 joke, here it is ! :  \n\n{joke}")
    else:
        print(f"\nSorry, I don't have jokes about {term} :(")

ascii = figlet_format("Ratio Dad Jokes")
logo = colored(ascii, "cyan")
print(logo)

while True:

    jokes(input("Want a dad joke ? Search for a topic: "))
    answer = input("Press(q) to quit or hit enter for another dad joke...")

    if answer == "q" or answer == "quit":
        print(colored("\nSee you next time!", "green"))
        break

    else:
        continue
