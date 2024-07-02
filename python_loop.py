

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "grapes", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x,'\t',y, '\n')


# for i in range(1, 5):       # 1 first ma 1 hunxa
#     for j in range(i):      # 1 chalxa
#         print(i, end=' ')   # 1 print  1 times
#     print()                 # to new line
    
i = 1
while i < 10:
    j = i
    while j < 10:
        print(f"{j}", end=" ")
        j = j + 1
    print("")
    i = i + 1
print("Complete!")

# i = 1: Inner loop runs 9 times, printing 1 2 3 4 5 6 7 8 9
# i = 2: Inner loop runs 8 times, printing 2 3 4 5 6 7 8 9
# i = 3: Inner loop runs 7 times, printing 3 4 5 6 7 8 9
# i = 4: Inner loop runs 6 times, printing 4 5 6 7 8 9
# i = 5: Inner loop runs 5 times, printing 5 6 7 8 9
# i = 6: Inner loop runs 4 times, printing 6 7 8 9
# i = 7: Inner loop runs 3 times, printing 7 8 9
# i = 8: Inner loop runs 2 times, printing 8 9
# i = 9: Inner loop runs 1 time, printing  9