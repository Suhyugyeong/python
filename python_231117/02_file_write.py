f = open("hello10.txt", "w")
for i in range(10):
    f.write(f"hej{i+1}!\n")
    f.close()
    
