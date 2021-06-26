list_1 = [1, 1, 5, 5, 6, 7, 7, 7]

def remove_dubles(list_):
    result = []
    for i in list_1:
        if list_1.count(i) == 1:
            result.append(i)

    return result

# print(remove_dubles(list_1))
print("asides")

# list_2 = [1, 1, 7, 1, 1]

# for i in list_2:
#     print(list_2)
#     print(i)
#     if list_2.count(i) > 1:
#         list_2.remove(i)

# print(list_2)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



# final_list = []

# for element in a:
#     if element in b and not element in final_list:
#         final_list.append(element)


# print(final_list)


# text = input("Tell smth:\n")

# text = text.split(" ")
# print(text)
# text.reverse()
# result = ""
# for word in text:
#     result += f"{word} "
# print(result)



# a = [1, 1, 5, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# # a.reverse()

# print(sorted(a, reverse=True))
# print(a)

dict_1 = {"key1": 14, "key2": 15, "key3": [1, 2]}
dict_2 = {"key1": 28, "key5": 15, "key6": [1, 2]}

dict_3 = {}
# print(dict_1["key3"])


# for key in dict_1:
#     print(key, dict_1[key])


# print(dict_1.keys(), type(dict_1.keys()))
# for key in dict_1.keys():
#     print(key, dict_1[key])



# print(dict_1.keys(), type(dict_1.keys()))
# for key in dict_1.keys():
#     print(key, dict_1[key])

# print(dict_1.values(), type(dict_1.values()))
# for value in dict_1.values():
#     if not type(value) is list and value > 5:
#         print(value)

# print(dict_1.items(), type(dict_1.items()))

# for key, value in dict_1.items():
#     print(key, value)



# key, value = ("key1", 14)

# dict_1["key4"] = 17
# dict_1["key4"] = 10

# print(dict_1)


dict_1 = {"key1": 14, "key2": 15, "key3": [1, 2]}
dict_2 = {"key1": 28, "key5": 15, "key6": [1, 2]}

# dict_3 = {}

dict_3.update(dict_1)
# dict_3.update(dict_2)

# for key in dict_1:
#     dict_3[key] = dict_1[key]


# for key in dict_2:
#     dict_3[key] = dict_2[key]

# print(dict_3.get("key7", "ajhd"))

# dict_1['key2'] += 2
# print(dict_3.pop("key3"))

# print(dict_2.popitem())

# del dict_1["key2"]

print(help(dict_3.update))

def foo(a:int, b:list):
    """

    :param a:
    :param b:
    :return:
    """

    pass









