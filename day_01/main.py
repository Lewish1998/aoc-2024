# Part One
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

# print(sum(new_list))


# Part Two
# Idea 1
# obj = lambda: None
# for i in range(len(left)):
#     if left[i] in right:
#         print(f"{left[i]}: {right.count(left[i])}")
#         field = left[i]
#         obj.field = right.count(left[i])

# print(obj)
        
# Idea 2
list = []
for i in range(len(left)):
    if left[i] in right:
        sub = [left[i], right.count(left[i])]
        list.append(sub)

print(list)

answer_list = []
for i in list:
    j = i[0] * i[1]
    answer_list.append(j)

print(answer_list)

answer = sum(answer_list)
print(answer)