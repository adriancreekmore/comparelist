path1 = input("Please enter the path of your first list: ")

first_list = open(f"{path1}", "r")
read1 = str(first_list.read())
list1 = read1.split()

path2 = input("Please enter the path of your second list: ")

second_list = open(f"{path2}", "r")
read2 = str(second_list.read())
list2 = read2.split()

shared_words = []
for word in list1:
    if word in list2:
        shared_words.append(word)

unique1 = []
for word in list1:
    if word not in list2:
        unique1.append(word)

unique2 = []
for word in list2:
    if word not in list1:
        unique2.append(word)
        


print(f"Your lists share the words: {shared_words}")
print(f"{unique1} are unique to list 1.")
print(f"{unique2} are unique to list 2.")






