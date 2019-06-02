import json

cat_food_dict = {}

user_input_date = input("What is todays date? ")
user_input_flavor = input("Which flavor are we serving today? ")
user_input_style = input("And which consistency is this flavor? ")
user_input_cat_color = input("Which color cat is on the can? ")
user_input_overall = input("On a scale of 0-5, how would Sophie rate her meal today? ")

cat_food_dict["Date"] = user_input_date
cat_food_dict["Flavor"] = user_input_flavor
cat_food_dict["Consistency"] = user_input_style
cat_food_dict["Cat_Color"] = user_input_cat_color
cat_food_dict["Overall_Rating"] = user_input_overall

converted = json.dumps(cat_food_dict, indent = 4, sort_keys=True)

date = str(user_input_date)
date_f = "{}".format(date)

flavor = str(user_input_flavor)
flavor_f = "{} ".format(flavor)

style = str(user_input_style)
style_f = "{}".format(style)

color = str(user_input_cat_color)
color_f = "{} ".format(color)

overall = str(user_input_overall)
overall_f = "{} ".format(overall)

all_4_f = f"\n-------------------------------------------------\nDate: {date_f}\nFlavor: {flavor_f}\nStyle: {style_f}\nCat Color: {color_f}\nOverall Rating: {overall_f}"

with open('cat_food.json', 'a') as out_file:
	out_file.write('{}\n'.format(converted))

print(all_4_f)
print("Saved!")

out_file.close()
