import dtree as d
import monkdata as m

# Compute information gain for each attribute
gains = [(i, d.averageGain(m.monk1, attribute)) for i, attribute in enumerate(m.attributes)]
# Find the attribute with the highest gain
best_attribute_index, best_gain = max(gains, key=lambda x: x[1])
best_attribute = m.attributes[best_attribute_index]
subsets = {value: d.select(m.monk1, best_attribute, value) for value in best_attribute.values}

second_level_splits = {}
for value, subset in subsets.items():
    if not subset:
        continue
    gains = [(i, d.averageGain(subset, attribute)) for i, attribute in enumerate(m.attributes) if i != best_attribute_index]
    best_attr_index_subset, _ = max(gains, key=lambda x: x[1])
    second_level_splits[value] = m.attributes[best_attr_index_subset]


leaf_classes = {}
for subset_value, subset_attribute in second_level_splits.items():
    subset = subsets[subset_value]
    split_subsets = {value: d.select(subset, subset_attribute, value) for value in subset_attribute.values}
    for value, split_subset in split_subsets.items():
        # Key is now just subset_value
        leaf_classes[subset_value] = d.mostCommon(split_subset)


print(f"Root: {best_attribute.name}")
for subset_value, subset_attribute in second_level_splits.items():
    print(f"  When {best_attribute.name} = {subset_value}:")
    print(f"    Split by: {subset_attribute.name}")
    # Retrieve leaf class using the updated key structure
    leaf_class = leaf_classes[subset_value]
    class_label = "True" if leaf_class else "False"
    print(f"      Class = {class_label}")
