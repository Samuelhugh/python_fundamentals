# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         print(x)
#         x *= num
#         print(x)
#         print(num_list)
#     return num_list, x
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output: >>>[2,4,10,16]

def multiply(num_list,num):
    print(num_list, num)
    for x in range(len(num_list)):
        print(x)
        num_list[x] *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output: >>>[10,20,50,80]