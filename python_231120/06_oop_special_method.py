class Car:
    def __init__(self, id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return "차 번호 : " + self.id

def main():
    c = Car('123가5678')
    print(len(c))
    print(str(c))
    
main()