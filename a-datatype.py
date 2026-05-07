"""
dictionary : {}
{
    key: value,
    key1: valu1
}

"""

d = {
  "id" : 1234,
  "name" : "Ck",
  "l" : [12,13,"Four",15],
  "nd" : { 1: "One", "Two" : 2 }
}

print("Value of nd[Two]:", d["nd"]["Two"])

print(type(d), d)
print(d["name"])
name_of_key = "id"
print(d[name_of_key])


for k in d:
    print(k,":",d[k], type(d[k]))


# #   0, 1, 2    ,3
# l=[12,13,"Four",15]
# print(type(l))

# print("First value:", l[0])
# print("Last value:", l[-1])
# print("Last value:", l[3])

# print("Slice arrays:", l[2:-1])
# print("Slice arrays:", l[2:])
# print("Slice arrays:", l[0:2])
