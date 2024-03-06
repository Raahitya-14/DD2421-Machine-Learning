import dtree as d
import monkdata as m
import drawtree_qt5 as draw

def attributeCalc(attribute, dataset):
    print(f"Results for dataset: {dataset}")
    for i in range(0, 5):
        print(f"for attribute {i + 1} we have {d.averageGain(dataset, attribute)}")

def calculate_information_gain(dataset, attributes):
    gains = []
    for attribute in attributes:
        gain = d.averageGain(dataset, attribute)
        gains.append(gain)
    return gains


split = d.select(m.monk1, m.attributes[1], 5)

test = m.monk1[0]

print(f"test: {test.attribute[m.attributes[4]]}")

main = d.buildTree(m.monk1, m.attributes)

tree1 = d.select(m.monk1, m.attributes[4], 1)
tree2 = d.select(m.monk1, m.attributes[4], 2)
tree3 = d.select(m.monk1, m.attributes[4], 3)
tree4 = d.select(m.monk1, m.attributes[4], 4)

built_tree1 = d.buildTree(tree1, m.attributes)
built_tree2 = d.buildTree(tree2, m.attributes)
built_tree3 = d.buildTree(tree3, m.attributes)
built_tree4 = d.buildTree(tree4, m.attributes)

print(main)
print(built_tree1)
print(built_tree2)
print(built_tree3)
print(built_tree4)


draw.drawTree(built_tree1)