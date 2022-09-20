

# message = input()
#
# message = message.lower()
#
# arr = list(message)
#
# temp = []
# for i in range(0,len(arr)):
#     if arr[i] == " ":
#         for j in range(len(temp)-1,-1,-1):
#             print(arr[j],end="")
#         print("ay",end="")
#         temp = []
#     else:
#         temp.append(arr[i])

#         # ['m', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'a', 'd', 'h', 'i', 't', 'y', 'a']

a = input()


lis = a.split()

end = ""


for i in range(0,len(lis)):
    b = list(lis[i])
    if b[0] not in ['a', 'e', 'i', 'o', 'u']:
        k = b[0]
        b.append(str(k))
        b[0] = ""
    b.append("ay")
    print(" ".join(b) , end="    ")
    end = end +"  "+ (" ".join(b))

print("\n")
print(end.strip(" "))




















