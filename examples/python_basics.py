message = "Hello" #This is a string
x = 4 #This is an integer
height = 1.82 #This is a float
is_married = False #this is a boolean
is_old_enough = x > 18 #this is a boolean which we get from calculation


# print(is_old_enough)
age_str = input("Prasome ivesti savo amziu: ") #input komanda visada duoda teksta
age = int(age_str)

# conditional statement checks if a condition is true
if age >= 20:
    print("Prasome imkite alaus")
    print("Prasome imkite alaus")
    print("Prasome imkite alaus")
elif age >= 18:
    print("Prasome imkite energetinio")
else:
    print("Prasome imkite saldaini")

