# import random
# import dtree as d
# import monkdata as m
# import matplotlib.pyplot as plt

# def partition(data, fraction):
#     ldata = list(data)
#     random.shuffle(ldata)
#     breakPoint = int(len(ldata) * fraction)
#     return ldata[:breakPoint], ldata[breakPoint:]

# num_simulations = 100
# datasets = {'monk1': m.monk1, 'monk3': m.monk3}
# fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

# results = {dataset: [] for dataset in datasets}


# for dataset_name, dataset in datasets.items():
#     for fraction in fractions:
#         avg = 0                                                                                                   

#         for _ in range(num_simulations):
#             train_set, val_set = partition(dataset, fraction)

#             tree = d.buildTree(train_set, m.attributes)

#             best_accuracy = d.check(tree, val_set)
#             best_tree = tree

#             for pruning in d.allPruned(tree):
#                 accuracy = d.check(pruning, val_set)
#                         # print(accuracy)
#                 if accuracy >= best_accuracy:
#                     best_accuracy = accuracy
#                     best_tree = pruning

#             avg += d.check(best_tree, val_set)

#         results[dataset_name].append(avg / num_simulations)

# plt.figure(figsize=(14, 5))
# for dataset_name, accuracy in results.items():
#     plt.plot(fractions, accuracy, marker='o', label=dataset_name)

# plt.title("MONK-1 (N = 100 simulations")
# plt.xlabel("Partition value")
# plt.ylabel("Classification performance")
# plt.legend()
# plt.show()
import monkdata as m
import dtree
import random
import matplotlib.pyplot as plt

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)

    return ldata[:breakPoint], ldata[breakPoint:]

def refine_tree(train, val):
    t = dtree.buildTree(train, m.attributes)
    p1 = performance = dtree.check(t, val)
    better_found = True
    while better_found:
        prunes = dtree.allPruned(t)
        better_found = False
        for prune in prunes:
            tmp_performance = dtree.check(prune, val)
            if tmp_performance > performance:
                t = prune
                performance = tmp_performance
                better_found = True
    return p1, dtree.check(t, val)

runs = 1000
fractions = [i/10 for i in range(3,9)]
classification_performance = []
for fraction in fractions:
    i = runs
    performance = [0,0]
    while i > 0:
        monktrain, monkval = partition(m.monk3, fraction)
        performance_run = refine_tree(monktrain, monkval)
        performance = [performance[i] + performance_run[i] for i in range(0,2)]
        i -= 1
    performance = [performance[i]/runs for i in range(0,2)]
    classification_performance.append(performance)

before_pruning = [c[0] for c in classification_performance]
after_pruning = [c[1] for c in classification_performance]

plt.figure(figsize=(14, 5))
plt.scatter(fractions, before_pruning, marker='x', label='Before pruning')
plt.scatter(fractions, after_pruning, marker='o', label='After pruning')
plt.title("MONK-3 (N = 1000 simulations)")
plt.xlabel("fraction value")
plt.ylabel("Classification error")
plt.legend()
plt.show()