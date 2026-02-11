# #Part 2
#
# from easygui import *
#
#
# msgbox("Welcome to the Kingdom of Rosa, brave adventurer!")
#
# hero_name = enterbox("What is your username?")
#
# while True:
#     age = integerbox("What is your age?")
#     if age < 16:
#         msgbox("Your age is too young for this exercise.")
#     else:
#         break
#
# password = passwordbox("Create password to continue:")
#
#
# hero_class = choicebox("Pick your class:",
#                         choices=["Knight", "Archer", "Rogue"])
#
# items = multchoicebox("Select your starting items:",
#                        choices=["Sword", "Shield", "Potion", "Spellbook"])
#
# attributes = multenterbox("Enter hero characteristics:",
#                           fields=["Hair attributes", "Armor appearance", "Weapon appearance"])
#
# action = buttonbox("You reach a fork. What do you do?",
#                     choices=["Go Left", "Go Right", "Go Up", "Go Down"])
#
# while True:
#     accept_quest = ynbox("A villager asks you to slay a dragon. "
#                          "Do you accept?")
#     if not accept_quest:
#         msgbox("Don't be difficult.")
#     else:
#         break
#
# task = "Write your name inside it to claim."
# title="You found a anti-blaze spell."
# code = codebox(task, title)
# print(code)
#
#
# msgbox("Behold the dragon!", image="dragon.gif")
#
# msgbox("Completed demo.\n"
#        "Would you to save progress in a file?")
#
# save_file = filesavebox(
#     "Save your progress to file?")