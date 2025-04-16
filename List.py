# List1 = [1, 2, 3, 4]
# List2 = [
#     "ab",
#     "cd",
#     "ef",
#     "gh"
# ]
# List3 = [1, "ab"]
# List4 = []

# print (List1)
# print (List2)
# print (List3)
# print (List4)

list_1 = [5,6,7,8,9,10,11,12]

# for i in range (0, len(list_1)):
#     print("index:", i, "element", list_1[i])

for i, v in enumerate(list_1):
    print("index :", i, "element :", v)

nest_list_1 = [
    [0,1,1],
    [1,0,0]
]
nest_list_2 = [
    [0,1,1],
    [1,0,0]
]

nest_list_3 = nest_list_1 * nest_list_2