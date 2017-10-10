"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices

#creates empty dict
melon_dict = {}

list_of_melon_names = melon_names.values()
for item in list_of_melon_names:
    melon_dict[item] = {}

for key in melon_dict:
    melon_dict[key]["flesh_color"] = None
    melon_dict[key]["weight"] = None
    melon_dict[key]["rind_color"] = None
    if key == "Honeydew":
        melon_dict[key]["seedless"] = False
    else:
        melon_dict[key]["seedless"] = True




print melon_dict

def print_melon(name, seedless, price):
    """Print each melon."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
