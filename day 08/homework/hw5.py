# 5. შექმენით პატარა თამაში, სადაც თქვენ შექმნით რაიმე რიცხვების თანმიმდევრობას,
# და მომხმარებელმა კი უნდა გამოიცნოს ეს თანმიმდევრობა (გამოიყენეთ While loop)


numbers = 5678
user_numbers = int(input("შეიყვანე 4 რიცხვი რომელსაც ფიქრობ (მიმდევრობა): "))

while user_numbers != numbers:
    if len(str(user_numbers)) != len(str(numbers)):
        print("თანმიმდევრობა შედგება 4 რიცხვისგან და არ უნდა აღემატებოდეს მას")

    user_numbers = int(input("თანმიმდევრობა არასწორია თავიდან შეიყვანე: "))

print("გილოცავ! შენ სწორად გამოიცანი თანმიმდევრობა <3")