import dtree as d
import monkdata as m
import drawtree_qt5 as draw  # Use drawtree_qt4 if you have PyQt4

# Choose the attribute with the highest information gain
# Replace 'your_chosen_attribute_index' with the index of that attribute
attribute_index = 5
attribute = m.attributes[attribute_index]

# Split the monk1 dataset
subsets = [d.select(m.monk1, attribute, value) for value in attribute.values]

# Compute information gains for each subset
for subset in subsets:
    gains = [d.averageGain(subset, attr) for attr in m.attributes if attr != attribute]
    print(gains)

# Manually build the tree for the first two levels (as per your analysis)
# ...

# Build the tree using the ID3 algorithm
id3_tree = d.buildTree(m.monk1, m.attributes)

# Print and draw the ID3 tree
print(id3_tree)
draw.drawTree(id3_tree)
