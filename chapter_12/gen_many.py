vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Dont't forget to pack you towel"
# создаем генератор множеств
found = {letter for letter in vowels if letter in message}
print(found)
