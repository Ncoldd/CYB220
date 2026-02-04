# Person = {
#     "f_name": "Eric",
#     "l_name": "Grando",
#     "age": 14,
#     "hometown": "Province",
#     "current_city": "Kingdom City",
#     "username": "Grand_Child"
# }
# print(Person)
#
# print()
#
# print(
#     f"This person's first name is {Person["f_name"]},\n"
#     f"last name is {Person["l_name"]},\n"
#     f"and their username is {Person['username']}."
# )
#
# print(
#     f"For security purposes, we might \nrequest their"
#     f"hometown, which is {Person['hometown']}"
# )
#
# print()
#
# Definitions = {
#     "python":"a language",
#     "variable":"a named container",
#     "list":"a collection",
#     "method":"object function",
#     "if_statement":"Conditional function",
#     "dictionary":"a collection of key-values",
#     "function":"A reusable block of code"
# }
#
# for key, value in Definitions.items():
#     print(f"{key}: {value}\n")

# counties = {
#     "Anderson County": "Anderson",
#     "Spartanburg County": "Spartanburg",
#     "Abbeville County": "Abbeville",
#     "Aiken County": "Aiken",
#     "Beaufort County": "Beaufort",
#     "Charleston County": "Charleston"
# }
#
# county_list = [
#     "Abbeville County",
#     "Aiken County",
#     "Anderson County",
#     "Beaufort County",
#     "Charleston County",
#     "Spartanburg County",
#     "Greenville County",
#     "Richland County",
#     "Horry County",
#     "Lexington County"
# ]
# for county in county_list:
#     if county in counties:
#         print(f"{county} is in our dictionary, "
#               f"and the capital/seat is "
#               f"{counties[county]}.")
#     else:
#         print(f"{county} is not in our dictionary. "
#               f"We will add this county shortly. "
#               f"Thanks!")
#
# abbeville = {
#     "Abbeville": 12400,
#     "Calhoun Falls": 3000,
#     "Due West": 2600,
#     "Donaldson": 1200,
#     "Lowndesville": 500
# }
#
# aiken = {
#     "Aiken": 32000,
#     "North Augusta": 21000,
#     "Graniteville": 3000,
#     "Burnettown": 2000,
#     "Gloverville": 1200
# }
#
# anderson = {
#     "Anderson": 28000,
#     "Belton": 4000,
#     "Clemson": 16000,
#     "Pendleton": 3500,
#     "Williamston": 5500
# }
#
# beaufort = {
#     "Beaufort": 13000,
#     "Hilton Head": 42000,
#     "Bluffton": 22000,
#     "Port Royal": 13000,
#     "Okatie": 8000
# }
#
# charleston = {
#     "Charleston": 150000,
#     "Mount Pleasant": 93000,
#     "North Charleston": 125000,
#     "Summerville": 52000,
#     "Goose Creek": 45000
# }
#
# county_list = [abbeville, aiken, anderson, beaufort, charleston]
#
# for county in county_list:
#     print()
#     for city, population in county.items():
#         print(f"In {city.title()}, the current population is {population}.")

# sc_counties = {
#     "Abbeville County": ["Abbeville", "Calhoun Falls", "Due West"],
#     "Aiken County": ["Aiken", "North Augusta", "Graniteville"],
#     "Anderson County": ["Anderson", "Clemson", "Belton"],
#     "Beaufort County": ["Hilton Head", "Beaufort", "Bluffton"],
#     "Charleston County": ["Charleston", "North Charleston", "Mount Pleasant"]
# }
#
# for county, cities in sc_counties.items():
#     print(f"In {county}, the largest cities are {cities[0]}, {cities[1]}, and {cities[2]}.")
#
#
# name = input("Please enter your name: ")
#
# print(f"Welcome to Anderson University, {name}!")
#
# money = float(input("How much money do you have to spend on a processor? $"))
#
# i3_price = 120
# i5_price = 200
# i7_price = 320
# i9_price = 500
#
# if money >= i9_price:
#     print("You can afford an i9 processor!")
# elif money >= i7_price:
#     print("You can afford an i7 processor!")
# elif money >= i5_price:
#     print("You can afford an i5 processor!")
# elif money >= i3_price:
#     print("You can afford an i3 processor!")
# else:
#     print("Sorry, you cannot afford any of these processors right now.")
#
# while True:
#     user_input = input("Enter an integer (or type 'quit' to exit): ")
#
#     if user_input.lower() == "quit":
#         print("Goodbye!")
#         break  # exits the loop
#
#     if user_input.isdigit():
#         number = int(user_input)
#         if number % 2 == 0:
#             print(f"{number} is even.")
#         else:
#             print(f"{number} is odd.")
#
# active = True
#
# while active:
#     response = input("Type something (or 'quit' to exit): ")
#     if response.lower() == "quit":
#         break
#     print(f"You typed: {response}")

# valid_flavours = ["Ubuntu", "Kubuntu", "Xubuntu", "Lubuntu", "Ubuntu MATE"]
# 
# while True:
#     username = input("Enter username (or type 'quit' to stop): ")
#     print()
#     if username.lower() == "quit":
#         break
#     print(f"Flavors: {valid_flavours}")
#     flavour = input("Enter your favorite Ubuntu flavour: ").title()
# 
#     if flavour in valid_flavours:
#         print(f"Thanks {username}, your favorite flavour is '{flavour}'.\n")
#     else:
#         print(f"'{flavour}' is not a valid Ubuntu flavour. Valid options are:\n"
#               f"{valid_flavours}")
