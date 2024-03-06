import dtree as d
import monkdata as m

entropy_monk1 = d.entropy(m.monk1)
entropy_monk2 = d.entropy(m.monk2)
entropy_monk3 = d.entropy(m.monk3)

print("Entropy of MONK-1 training dataset:", entropy_monk1)
print("Entropy of MONK-2 training dataset:", entropy_monk2)
print("Entropy of MONK-3 training dataset:", entropy_monk3)
