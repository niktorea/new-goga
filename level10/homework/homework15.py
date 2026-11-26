# 15)შექმენი სამი სია:
morning = ["Breakfast", "Exercise"]
afternoon = ["Study", "Lunch"]
evening = ["Reading", "Sleep"]
morning.extend(afternoon)
morning.extend(evening)
print(morning)

print(len(morning))
# 1. სამივე სია გააერთიანე ერთ სიაში.
# 2. დაბეჭდე საბოლოო სია.
# 3. დაითვალე რამდენი აქტივობა გაქვს მთლიანობაში. გამოიყენე len()