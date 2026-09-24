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
# for char in name:
#     print(char)
# -------------------------------------------------------------------------------------------------
# assessment solvings
# 1a. 
def ticket_total(price, quantity):
    total = price * quantity
    return total
amount = ticket_total(7, 3)
print(amount)
# amount printed none because nothing was actually returned from the function, it was just printed inside the function.
# -------------------------------------------------------------------------------------------------------------------

# 2.
def passing_scores(scores):
    passed = []
    for score in scores:
        if score >= 50:
            passed.append(score)
    return passed
print(passing_scores([49, 50, 80, 65]))
# current output is [80] because len(scores)-1 excludes the last element in the list, which is 65. second defect is that the condition should be >= 50.
assert passing_scores([30, 56, 80]) == ([56, 80])
assert passing_scores([70]) == ([70])
assert passing_scores([]) == ([])
# -------------------------------------------------------------------------------------------------------------------------
# 3.
def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = profile["tags"].copy() + [tag]
    # updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])
print(changed["tags"])

assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]
# ----------------------------------------------------------------------------------------------------------------------------
# 4. 

# ----------------------------------------------------------------------------------------------------------------------------
def is_palindrome(word):
    return word == word[::-1]

