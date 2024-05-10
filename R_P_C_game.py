import random

c_in = random.randint(0,2)
u_in=int(input("0. for (Rock)🪨 .\n1. for (Paper)📃.\n2. for (Scissor)✂️ .\n__________________\n"))
print(c_in)
if u_in == 0 and c_in == 0: 
    print("🪨  = 🪨\nMatch draw.")

elif u_in == 0 and c_in == 1:
    print("🪨  = 📃\nYou loose.")

elif u_in == 0 and c_in == 2:
    print("🪨  =  ✂️\nYou win.")

elif u_in == 1 and c_in == 0:
    print("📃 =  🪨\nYou win.")
    
elif u_in == 1 and c_in == 1:
    print("📃 = 📃\nMatch draw.")

elif u_in == 1 and c_in == 2:
    print("📃 =  ✂️\nYou loose.")
    
elif u_in == 2 and c_in == 0:
    print("✂️  =  🪨\nYou loose.")
    
elif u_in == 2 and c_in ==1:
    print("✂️  = 📃\nYou win.")

elif u_in == 2 and c_in == 2:
    print("✂️  = ✂️\nMatch draw.")
    
else:
    print("Enter 0,1,2 one of these only")