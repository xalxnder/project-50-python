print("Welcome to the Band Name Generator \n")

user_city = input("What city did you grow up in? \n")
user_pet = input("What is the name of your pet? \n")


def generator(city, pet):
	return f"The name of your band is {city} {pet}!"


print(generator(user_city, user_pet))
