import dtree  
import monkdata as m

# Calculate the information gain for each attribute for each MONK dataset
def calculate_information_gain(dataset, attributes):
    gains = []
    for attribute in attributes:
        gain = dtree.averageGain(dataset, attribute)
        gains.append(gain)
    return gains

# Assuming monkdata.py provides the datasets and attributes like this:
# monk1, monk2, monk3, attributes

gains_monk1 = calculate_information_gain(m.monk1, m.attributes)
gains_monk2 = calculate_information_gain(m.monk2, m.attributes)
gains_monk3 = calculate_information_gain(m.monk3, m.attributes)

print("Information Gain for MONK-1:", gains_monk1)
print("Information Gain for MONK-2:", gains_monk2)
print("Information Gain for MONK-3:", gains_monk3)
