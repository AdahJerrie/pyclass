print(10 < 5)

temp = 35

if temp > 35:
    print("it is a hot weather")

else:
    print("normal weather")

score = 50

if score >= 70:
    print("A")
elif score > 60:
    print("B")
else:
    print("pass")
# --------------------------------------------------------------------------------------------------------------
age = 20
has_id = False 

if age >= 18 and not has_id:
    print("access granted")
else:
    print("access denied")

day = "tuesday"

if day == "saturday" or day == "sunday":
    print("weekend")
else:
    print("weekday")   
# --------------------------------------------------------------------------------------------------------

age >= 18
has_cv = True
qualified = age and has_cv

if qualified:
    print("access granted")
else:
    print("access denied")

good_eyes = 2
half_eyes = 1 

employeable = good_eyes and not half_eyes

if employeable:
    print(employeable)
else:
    print(not employeable)

# ---------------------------------------------------------------------------------------------

is_student = False
is_senior = True
is_staff = False

if is_student or is_senior or is_staff:
    print("Discount available")

# -----------------------------------------------------------------------------------------------------------
# Nested conditionals
age = 30
has_car = True
can_walk = True

if age <= 30:
    if has_car:
        if can_walk:
            print("can travel with us")
    else:
        print("you must have a car")
else:
    print("you are too old")
# ------------------------------------------------------------------------------------------------
name = "Jeremiah"

if name:
    print(f"welcome {name}!")

# ------------------------------------------------------------------------------------------------
for char in name:
    print(char)
