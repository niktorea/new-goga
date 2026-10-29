# 13)შერეული სია
items = [15, "apple", 28, "banana", 9]
if items[0] > 10:
    print("the num is more then 10")
else:
    print("the num is more or eaqvel to ten")
if items[1] == "apple":
    print("xilia")
else:
    print("else element")
items[3] = "orange"
if items[-1] < 10:
    print("small numbers")
else:
    print("big numbers")

# 1. თუ პირველი ელემენტი მეტია 10-ზე, დაბეჭდე "რიცხვი 10-ზე მეტია", სხვა შემთხვევაში — "რიცხვი 10-ზე ნაკლები ან ტოლია".
# 2. თუ მეორე ელემენტი უდრის "apple"-ს, დაბეჭდე "ხილია", სხვა შემთხვევაში — "სხვა ელემენტია".
# 3. მეოთხე ელემენტი შეცვალე "orange"-ით.
# 4. თუ ბოლო ელემენტი ნაკლებია 10-ზე, დაბეჭდე "პატარა რიცხვია", სხვა შემთხვევაში — "დიდი რიცხვია".