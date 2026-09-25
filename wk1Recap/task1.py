# Exercise 1 — ListsCreate a list containing five programming languages.Then:Print the first language.Print the last language.Add another language using append().Remove one language using remove().Print the length of the list.Loop through the list and print every language.RequirementsUse:a listindexingappend()remove()len()a for loopDon't worry about tuples, sets, or dictionaries yet.

def ListsCreate(language):
    return language

ListsCreates = ListsCreate(["java", "Go", "python", "Rust", "JS"])
# print(ListsCreates[0])
# print(ListsCreates[-1])
# ListsCreates.append("Express")
# print(ListsCreates)
# ListsCreates.remove("java")
# print(ListsCreates)
# print(len(ListsCreates))
# for lang in ListsCreates:
#     print(f"programming language: ", lang)

# -----------------------------------------------------------------------------------------------------------------------------------
set()
# Now let's see whether you understand why we'd choose something other than a list.Part A — TupleCreate a tuple representing a coordinate:x = 10y = 20Then:Print the first coordinate.Print the second coordinate.Try changing the first coordinate to 50.Before you run it, predict what will happen when you try to change it.Part B — SetCreate this list:numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]Then:Convert it to a set.Print the set.Explain why the duplicate numbers disappeared.Check whether 3 exists in the set.

coordinate = (10, 20)
# print(coordinate[0])
# print(coordinate[1])
# # try:
#     coordinate[0] = 50
# except TypeError as e:
#     # print(e)

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# convert the list to a set
unique_numbers = set(numbers)
# print(unique_numbers)

three_check = 3 in unique_numbers
# print(three_check)
# when you pass a list to set(), python automatically filters out any repeating values, keeping only one instance of each.
# ---------------------------------------------------------------------------------------------------------------------------------
# dictionaries
# Dictionaries 🗂️Create a dictionary representing a developer profile:developer = { "name": "Jerrie", "age": 25, "language": "Go", "is_learning_python": True}Your tasksPrint the developer's name.Print their age.Print their programming language.Change "language" from "Go" to "Python".Add a new key:"experience": 2Check whether "age" exists in the dictionary.Loop through the dictionary and print each key and value.ChallengeWithout running the code first, predict what this will produce:print(developer["country"])
developer = {
    "name": "Jerrie", 
    "age": "25", 
    "language": "Go", 
    "is_learning_python": True
}
# print(developer["name"])
# print(developer["age"])
# print(developer["language"])
# developer["language"] = "python"
# print(developer["language"])
# developer["experience"] = 2
# print(developer["experience"])
# print(developer)


two_check = "age" in developer
# print(two_check)

# for key, value in developer.items():
    # print(f"{key}: {value}")
# -----------------------------------------------------------------------------------------------------------
# Collections Challenge 🧠Now we're going to combine list + tuple + set + dictionary.Imagine you're building a small developer skills tracker.Starting datalanguages = ["Python", "Go", "Python", "JavaScript", "Go"]developer = { "name": "Jerrie", "experience": 2}coordinates = (6.5244, 3.3792)Your tasks1. ListPrint the languages.Then add "Rust" to the list.2. SetConvert languages into a set called unique_languages.Print it.Your goal is to remove the duplicate "Python" and "Go".3. TuplePrint the latitude and longitude separately using indexes.Remember:coordinates[0] → ?coordinates[1] → ?4. DictionaryAdd this information to developer:"languages": unique_languagesThen print the entire dictionary.
languages = ["Python", "Go", "Python", "JavaScript", "Go"]
developer = {
     "name": "Jerrie", 
     "experience": 2
}
coordinates = (6.5244, 3.3792)
# print(languages)
languages.append("Rust")
print(languages)

# convert to set
unique_languages = set(languages)
print(unique_languages)
# tuple
print(coordinates[0])
print(coordinates[1])

developer["languages"] = unique_languages
print(developer)
