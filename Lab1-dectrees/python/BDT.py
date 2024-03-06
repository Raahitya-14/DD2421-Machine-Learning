import monkdata as m
import dtree as d


t_monk1 = d.buildTree(m.monk1, m.attributes)
t_monk2 = d.buildTree(m.monk2, m.attributes)
t_monk3 = d.buildTree(m.monk3, m.attributes)

performance_monk1_train = d.check(t_monk1, m.monk1)
performance_monk2_train = d.check(t_monk2, m.monk2)
performance_monk3_train = d.check(t_monk3, m.monk3)

performance_monk1_test = d.check(t_monk1, m.monk1test)
performance_monk2_test = d.check(t_monk2, m.monk2test)
performance_monk3_test = d.check(t_monk3, m.monk3test)

error_monk1_train = 1 - performance_monk1_train
error_monk2_train = 1 - performance_monk2_train
error_monk3_train = 1 - performance_monk3_train

error_monk1_test = 1 - performance_monk1_test
error_monk2_test = 1 - performance_monk2_test
error_monk3_test = 1 - performance_monk3_test


print("MONK-1 Train Error:", error_monk1_train)
print("MONK-1 Test Error:", error_monk1_test)

print("MONK-2 Training Error:", error_monk2_train)
print("MONK-2 Test Error:", error_monk2_test)

print("MONK-3 Training Error:", error_monk3_train)
print("MONK-3 Test Error:", error_monk3_test)
