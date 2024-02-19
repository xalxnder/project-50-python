import pandas

# Create a column for fur color
## Make a list out of th efur column
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_with_duplicates = squirrel_data['Primary Fur Color']
# print(fur_with_duplicates)
# Eliminate the duplicates
"""
My method was a bit much. Just know that I used set to get rid of the duplicates. Its easier to read when you are 
aware of that. 
"""
fur_no_duplicates = [x for x in [str(x) for x in list(set(fur_with_duplicates))] if x != 'nan']

# for color in fur_no_duplicates:
# 	amount = fur_with_duplicates.count(color)
# 	squirrel_dict['Fur Color'].append(color)
# 	squirrel_dict['Count'].append(amount)
#


"""
This is a much clearer/understandable method. Clear > Clever
"""
gray_count = len(squirrel_data[fur_with_duplicates == "Gray"])
cinnamon_count = len(squirrel_data[fur_with_duplicates == "Cinnamon"])
black_count = len(squirrel_data[fur_with_duplicates == "Black"])


squirrel_dict = {
	'Fur Color':["Gray", "Cinnamon","Black"],
	'Count':[gray_count, cinnamon_count, black_count]
}

squirrel_data_frame = pandas.DataFrame(squirrel_dict)
print(squirrel_data_frame)
