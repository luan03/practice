'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly 
swapping the adjacent elements if they are in wrong order.
'''

l = [30, 50, 10, 35, 70, 45, 80, 100, 22]
size_l = len(l)

# bubble sort
for i in range(size_l):
    change = False # optimization to not check twice 

    for j in range(1, size_l - i):
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            change = True
    if not change:
        break

print(l)