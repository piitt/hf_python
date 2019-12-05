def search4letters(phrase:str, letters:str='aeiou') -> set:
  """Возвращает множество указаных букв из фразы"""
  return set(letters).intersection(set(phrase))

print (search4letters('hitch-hiker'))
print (search4letters('galaxy', 'xyz'))
print (search4letters('life, the universe, and everything', 'o'))

print(search4letters(letters='iv', phrase='gvido van rossum'))
