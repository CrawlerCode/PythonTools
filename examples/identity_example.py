from pythontools.identity import identity

person = identity.Identity()
person.generateName()
person.generateEmail("@gmail.com")
person.generatePassword()
person.generateUsername()
print(person.getIdentity())