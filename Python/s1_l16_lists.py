friends = ["sai","teja"]
print(friends[1])

friends = [["sai","anand"],["teja","raju"]]
print(friends[1][0])

friends = [[["sai","anand"],["teja","raju"]]]
print(friends[0][1][1])

#count the list
friends = ["sai","teja"]
print(len(friends))

friends = [[["sai","anand"],["teja","raju","ramesh"]]]#3d
print(len(friends[0][1]))

#append()
friends = ["sai","teja"]
friends.append("sunitha")
print(friends) #['sai', 'teja', 'sunitha']

#remove()
friends = [[["sai","anand"],["teja","raju","ramesh"]]]#3d
friends[0].remove(["teja","raju","ramesh"])
print(friends) #[[['sai', 'anand']]]
