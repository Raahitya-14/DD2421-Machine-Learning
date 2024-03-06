import random
import dtree as d
import monkdata as m
import matplotlib.pyplot as plt

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

num_simulations = 100
datasets = {'monk1': m.monk1, 'monk3': m.monk3}
fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

# Store the results for plotting
results = {dataset: [] for dataset in datasets}

for dataset_name, dataset in datasets.items():
    for fraction in fractions:
        avg_performance = 0

        for _ in range(num_simulations):
            train_set, val_set = partition(dataset, fraction)
            tree = d.buildTree(train_set, m.attributes)

            # Prune the tree
            best_performance = d.check(tree, val_set)
            best_tree = tree

            for pruned_tree in d.allPruned(tree):
                performance = d.check(pruned_tree, val_set)
                if performance > best_performance:
                    best_performance = performance
                    best_tree = pruned_tree

            avg_performance += d.check(best_tree, val_set)

        # Calculate the average performance over all simulations
        results[dataset_name].append(avg_performance / num_simulations)

# Plotting the results
plt.figure(figsize=(14, 5))

for dataset_name, performances in results.items():
    plt.plot(fractions, performances, marker='x', label=dataset_name)

plt.title("Pruning Performance for MONK-1 and MONK-3 (N = 100 simulations)")
plt.xlabel("Fraction of Training Set")
plt.ylabel("Average Classification Performance")
plt.legend()
plt.show()
