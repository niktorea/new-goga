tasks = ["Homework", "Cleaning", "Shopping", "Exercise", "Reading"]
bot = int(input("pls enter an index:"))
delete = tasks.pop(bot)
print(tasks)
if delete == "Homework" :
    print("You finished your homework!")
else:
    print("Task removed:" + delete)
# print(tasks)
# # 2. წაშალე მითითებულ ინდექსზე მდგომი დავალება pop() მეთოდით. -- მოიძიე
# # 3. შეინახე წაშლილი დავალება ცალკე ცვლადში.
# # 4. თუ წაშლილი დავალება "Homework" არის, დაბეჭდე "You finished your homework!".
# # 5. სხვა შემთხვევაში დაბეჭდე "Task removed: ..." და წაშლილი დავალების სახელი.
# # 6. დაბეჭდე დარჩენილი დავალებები.
