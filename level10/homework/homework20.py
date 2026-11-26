# 20)რთული-----------------
students = ["Goga", "Nika", "Saba", "Ana", "Luka"]
new_students = ["Mariam", "Gio", "Dato"]

# ნაწილი 1 — მოსწავლეების დამატება
# 1. append() მეთოდით დაამატე სიაში ერთი ახალი მოსწავლე.
# 2. insert() მეთოდით დაამატე მოსწავლე მეორე ინდექსზე.
# 3. extend() მეთოდით შეუერთე new_students სია students სიას.
students.append("leo")
students.insert(2, "DATA")
students.extend(new_students)
print(students)

# ნაწილი 2 — მოსწავლეების მოძებნა
# 4. მომხმარებელს შეაყვანინე მოსწავლის სახელი.
# 5. გაიგე მისი ინდექსი index() მეთოდით.
# 6. დაითვალე რამდენჯერ გვხვდება ეს სახელი სიაში count() მეთოდით.
# 7. თუ მოსწავლე პირველ ინდექსზე დგას, დაბეჭდე "Near the beginning!".
bot = input("enter your name:")
print(students.index(bot))
print(students.count(bot))
if students.index(bot) == 1:
    print("Near the beginning!")

# ნაწილი 3 — მოსწავლეების წაშლა
# 8. მომხმარებელს შეაყვანინე მოსწავლის სახელი, რომლის წაშლაც სურს.
# 9. წაშალე ეს მოსწავლე remove() მეთოდით.
# 10. pop() მეთოდით წაშალე სიის ბოლო მოსწავლე და შეინახე ცალკე ცვლადში.
# 11. დაბეჭდე ორივე წაშლილი მოსწავლის სახელი.
bott = input("enter your names:")
students.remove(bott)
s = students.pop(-1)
print(s,bott) 





# ნაწილი 4 — საბოლოო შედეგი
# 12. შემოატრიალე მოსწავლეების სია reverse() მეთოდით.
# 13. დაბეჭდე საბოლოო სია.
# 14. თუ სიაში 3-ზე ნაკლები მოსწავლეა, გაასუფთავე სია clear() მეთოდით.
# 15. დაბეჭდე საბოლოო სია და მისი სიგრძე.

students.reverse()
print(students)
if len(students) < 3 :
    students.clear()

print(students)
print(len(students))

