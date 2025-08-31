# a = {} #Dictionary   (It is mutable)
# b = set() #Empty set
#
# print(a, type(a))
# print(b, type(b))

dict1 = {"good":"Something Pleasant", "bad":"not Pleasant"}
print(dict1["good"])

marks = {"Harshit" : 12, "Joker" : 10, "Rishabh" : 20, "Ayush" : 0}
print(marks["Ayush"])

marks["Rupal"] = 18
print(marks)
print(marks["Rupal"])  #If the key doesn't exist, it will give us error
# print(marks["RupalKoli"])
print(marks.get("Rupal koli")) #Get will save us from error, if key doesn't exist it will return None
print(marks.keys())
print(marks.values())
print(marks.items())