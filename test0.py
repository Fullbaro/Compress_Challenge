

file = open("original_file.txt", "r").read()

# Split file into words
file = file.split(" ")

# Collect words by unique key and appearence indexes list
dictionary = {}
index = 0
for word in file:
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(index)
    index += 1
print("Words length", len(dictionary))


# Remove words which only appears once
new_dictionary = {}
for key, values in dictionary.items():
    if len(values) > 1:
        new_dictionary[key] = values
print("More than 1 apperance words length:", len(new_dictionary))


print("Uj", len(new_dictionary))




# Test result
old = open('original_file.txt', 'r')
old.seek(0, 2)
old_size = old.tell()
new = open('compressed.txt', 'r')
new.seek(0, 2)
new_size = new.tell()
print(f"A tömörítés mértéke {round(((old_size - new_size) / old_size) * 100, 2)} %")