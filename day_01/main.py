left = []
right = []

with open('data.txt', 'r') as f:
    for n in f:
        l, r = n.strip().split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

new_list = []
for i in range(len(left)):
    new_list.append(left[i] - right[i]) if left[i] > right[i] else new_list.append(right[i] - left[i])

print(sum(new_list))