def print_user_profile(gender='female',first='Jane',last='Doe',pictures=[]):
    profileInfo = f'The user {first} {last} has the following pictures: '
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
# print_user_profile(**test_data2)
# print_user_profile(**test_data3)
