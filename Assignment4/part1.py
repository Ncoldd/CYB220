# #8-3 #################################################################################################
# def make_shirt(size, message):
#     print(f"The shirt is size {size} and has the message: "
#           f"'{message}' printed on it.")
#
# make_shirt("Medium", "Sleep")
#
# make_shirt(size="Large", message="I'm tired")

# #8-4 #################################################################################################
# def make_shirt(size="Large", message="tired"):
#     print(f"The shirt is size {size} and has the message: "
#           f"'{message}' printed on it.")
#
#     make_shirt()
#
#     make_shirt(size="Medium")
#
#     make_shirt(size="Small", message="Python runs the world")

# #8-5 #################################################################################################
# def describe_city(city, country="Iceland"):
#     print(f"{city} is in {country}.")
#
# describe_city("Reykjavik")
# describe_city("Akureyri")
# describe_city("Tokyo", country="Japan")

# #8-6 #################################################################################################
#
# def city_country(city, country):
#     return f"{city}, {country}"
#
# print(city_country("Santiago", "Chile"))
# print(city_country("Tokyo", "Japan"))
# print(city_country("Paris", "France"))

# #8-7 #################################################################################################
# def make_album(artist, title, songs=None):
#     album = {
#         "artist": artist,
#         "title": title
#     }
#     if songs is not None:
#         album["songs"] = songs
#     return album
#
# print(make_album("Link", "Meteor"))
# print(make_album("Punk", "Disc"))
# print(make_album("Ad", "20"))
# print(make_album("PiFl", "The Wl", 26))

# #8-8 #################################################################################################
# def make_album(artist, title, songs=None):
#     album = {
#         "artist": artist,
#         "title": title
#     }
#     if songs is not None:
#         album["sogs"] = songs
#     return album
#
# while True:
#     print("\nEnter album information (type 'q' to quit).")
#
#     artist = input("Artist: ")
#     if artist.lower() == "q":
#         break
#
#     title = input("Title: ")
#     if title.lower() == "q":
#         break
#
#     album = make_album(artist, title)
#     print(album)
#
# #8-9 #################################################################################################
# def show_messages(messages):
#     for message in messages:
#         print(message)
#
# texts = [
#         "Hey, um.", "On my way!",
#          "Can't talk now, busy!",
#          "See you soon!"
#         ]
#
# show_messages(texts)

# #8-10 #################################################################################################
# def send_messages(messages, sent_messages):
#     while messages:
#         message = messages.pop(0)
#         print(message)
#         sent_messages.append(message)
#
# texts = ["Hello World!", "Hello!", "World!"]
# sent_texts = []
#
# send_messages(texts, sent_texts)
#
# print("\nlist before sending", texts)
# print("\nlist after sending", sent_texts)

# #8-11 #################################################################################################
# def send_messages(messages, sent_messages):
#     while messages:
#         message = messages.pop(0)
#         print(message)
#         sent_messages.append(message)
#
# texts = ["Hello World!", "Hello!", "World!"]
# send_texts = []
#
# send_messages(texts[:], send_texts)
#
# print("\nOriginal list:", texts)
# print("Sent messages:", send_texts)

# #8-12 #################################################################################################
# def make_sandwich(*items):
#     print("Your sandwich with the following items:")
#     for item in items:
#         print("-", item)
#     print()
#
# make_sandwich("Turkey", "Lettuce", "Tomato")
# make_sandwich("Peanut Butter", "Jelly")
# make_sandwich("Ham", "Cheese", "Pickles", "Mustard")

# #8-13 #################################################################################################
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#
# my_profile = build_profile('Nate', 'Cold',
#                             location='Anderson, SC',
#                             hobby='coding',
#                             favorite_game='Elden Ring')
# print(my_profile)
#
# #8-14 #################################################################################################
#
# def make_car(manufacturer, model, **car_info):
#     car_info["manufacturer"] = manufacturer
#     car_info['model'] = model
#     return car_info
#
# car = make_car('subaru',
#                'outback',
#                color='blue',
#                tow_package=True
#                )
#
# print(car)

# #8-15 #################################################################################################
# from printing_functions import *
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
#
# #8-16 #################################################################################################
#
# import greet
# greet.say_hello("Roy")
#
# from greet import say_hello
# say_hello("Roy")
#
# from greet import say_hello as sh
# sh("Roy")
#
# import greet as g
# g.say_hello("Roy")
#
# from greet import *
# say_hello("Roy")
#
# #8-17 #################################################################################################
#
# def make_car(manufacturer, model, **car_info):
#
#     car_info['manufacturer'] = manufacturer
#     car_info['model'] = model
#
#     return car_info
#
# car = make_car(
#                'subaru',
#                'outback',
#                color='blue',
#                tow_package=True
# )
#
# print(car)
#
#
# def make_sandwich(*items):
#
#     print("You ordered a sandwich with:")
#
#     for item in items:
#         print("-", item)
#
#     print()
#
#
# make_sandwich("Turkey", "Lettuce", "Tomato")
# make_sandwich("Peanut Butter", "Jelly")
# make_sandwich("Ham", "Cheese", "Pickles", "Mustard")
#
#
# def say_hello(name):
#
#     print("Hello,", name)
#
# say_hello("Rob")
#
#
