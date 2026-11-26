students = ["Goga", "Nika", "Saba", "Ana", "Luka", "Mariam"]
bot = input("enter your name:")
botter = students.index(bot)
if botter == 0:
    print("first student")
elif botter == 5 :
    print("last student")
else:
    print("middle student")
    





# 1. მომხმარებელს შეაყვანინე მოსწავლის სახელი.
# 2. გაიგე მისი ინდექსი , შეინახე ცვლადში.
# 3. თუ ინდექსი 0-ია, დაბეჭდე "First student!".
# 4. თუ ინდექსი სიის ბოლო ინდექსია, დაბეჭდე "Last student!".
# 5. სხვა შემთხვევაში დაბეჭდე "Middle student!".