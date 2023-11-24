class Animal:
    age = 1
    def set_name(self, data):
        self.name = data

pig = Animal()
pig.set_name("돼지")
pig.age = 2

panda = Animal()
Animal.set_name(panda, "푸바오")
panda.age = 3


print(f"{pig.name} : {pig.age}살")
print(f"{panda.name} : {panda.age}살")