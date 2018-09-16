def prefix(word):
  return 'I think ' + word


def postfix(word):
  return word + ' is great!'


animal = 'rabit'

print(prefix(animal))
print(postfix(animal))
print(prefix(postfix(animal)))
