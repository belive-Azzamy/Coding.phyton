def friend_name(name):
    return name.len()

names = ["Agus", "Udin", "Jamal", "Budiono", "Siregar", "Samsudin", "Reza", "Fatih", "Raihan", "Dafa"]

friends_name = map(len, names)
print(list(friends_name))