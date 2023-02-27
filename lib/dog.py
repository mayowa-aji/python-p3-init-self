class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

fido = Dog("Fido")
print(fido.breed)

snoopy = Dog("Snoppy", "Terrier")
print(snoopy.name)
# Any

# snoopy = Dog("Snoopy", "Tennis Ball")
# print(snoopy.favorite_toy)
# # Tennis Ball
