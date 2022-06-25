list_nums = []
list_sum = []
list_prod = []
for i in range(1, 100):
    for j in range(i, 100):
        list_nums.append((i, j))
        list_sum.append(i + j)
        list_prod.append(i * j)


def idk_prod():
    global list_nums, list_sum, list_prod
    delete_indices = []
    for index, value in enumerate(list_prod):
        if list_prod.count(value) == 1:
            delete_indices.append(index)

    for k in sorted(delete_indices, reverse=True):
        del list_nums[k]
        del list_sum[k]
        del list_prod[k]


def idk_sum():
    global list_nums, list_sum, list_prod
    delete_indices = []
    for index, value in enumerate(list_sum):
        if list_sum.count(value) == 1:
            delete_indices.append(index)

    for k in sorted(delete_indices, reverse=True):
        del list_nums[k]
        del list_sum[k]
        del list_prod[k]


def ik_prod():
    global list_prod, list_nums
    list_answer = []
    for index, value in enumerate(list_prod):
        if list_prod.count(value) == 1:
            list_answer.append(list_nums[index])
    return list_answer


for _ in range(7):
    idk_prod()
    idk_sum()

print(ik_prod())
