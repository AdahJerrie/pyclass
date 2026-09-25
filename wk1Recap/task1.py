# Exercise 1 — ListsCreate a list containing five programming languages.Then:Print the first language.Print the last language.Add another language using append().Remove one language using remove().Print the length of the list.Loop through the list and print every language.RequirementsUse:a listindexingappend()remove()len()a for loopDon't worry about tuples, sets, or dictionaries yet.

def ListsCreate(language):
    return language

ListsCreates = ListsCreate(["java", "Go", "python", "Rust", "JS"])
print(ListsCreates[0])
print(ListsCreates[-1])
ListsCreates.append("Express")
print(ListsCreates)
ListsCreates.remove("java")
print(ListsCreates)
print(len(ListsCreates))
for lang in ListsCreates:
    print(f"programming language: ", lang)
