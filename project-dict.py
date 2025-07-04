Hobby = input("Enter your hobby: ")
Function_hobby = input("Enter your function hobby: ")

hobby_dict = dict(youreHobby=Hobby, function=Function_hobby)


hobby_dict["Year"] = "2021"
hobby_dict["Place"] = "Jakarta"
print(hobby_dict)

list.add = {"year" : 2021, "Place" : "Jakarta"}
hobby_dict.update(list.add)
print(hobby_dict)