import random 

seed = int(input())
random.seed(seed)

list_randint = [random.randint(0, 200) for _ in range(100)]

list_sample = random.sample(range(201), 100)

sum_ran = 0
for i in range(100):
    if (list_randint[i] in list_sample):
        sum_ran += 1

sum_sam = 0
for i in range(100):
    if (list_sample[i] in list_randint):
        sum_sam += 1

print(max(sum_ran, sum_sam))