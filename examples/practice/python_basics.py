message = "Hello" #This is a string
x = 4 #This is an integer
height = 1.82 #This is a float
is_married = False #this is a boolean
is_old_enough = x > 18 #this is a boolean which we get from a calculation


age_str = input("Prasome ivesti savo amziu: ") # CLI input. We always get string
age = int(age_str) # converts a string to an integer

# conditional statement checks if a condition is true then decides which action to take
if age >= 20:
    print("Prasome imkite alaus")#only gets printed if age is more or equal than 20
    print("Prasome imkite alaus")
    print("Prasome imkite alaus")


elif age >= 18:
    print("Prasome imkite energetinio") #only gets printed if age is 18 or 19
else:
    print("Prasome imkite saldaini") #only gets printed if age is under 18 (all the other cases not defined in earlier if blocks)

