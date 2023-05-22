from replit import clear
from art import logo

print(logo)

again = True

person_dic = {}


def find_higthest_bid(persons):
  max_value = 0
  for person in persons:
    value = persons[person]
    if value > max_value:
      max_value = value
      winner = person
  print(f"The winner is {winner} with a bid equals to ${str(max_value)}")


while again:
  entry_name = input("What's the person name?: ")
  entry_bid = int(input("What about his bid price?: $"))

  person_dic[entry_name] = entry_bid

  should_continue = input("Are there other users who want to bid? ")
  if should_continue == "no":
    again = False
    find_higthest_bid(person_dic)
  elif should_continue == "yes":
    clear()
  else:
    print("Cette instruction n'est pas prise en compte.")
