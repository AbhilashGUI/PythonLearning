#Menu Lunch/Dinner#

Biryani_order=input("Enter the order: Full/Family/Jumbo:")
Bill=0
if Biryani_order=='Full':
    Bill+=350
    print("Full Biryani price is 350rs")
elif Biryani_order=='Family':
    Bill+=750
    print("Family Biryani price is 750rs")

else:
    Bill+=1100
    print("Jumbo Biryani price is 1100")

Add_salad=input("Would you like to add salad (Y/N):")
if Add_salad=='Y':
  if Biryani_order=='Full':
    Bill+=10
else:
    Bill+=20

Add_coke=input("Would you like to add coke (Y/N):")
if Add_coke=='Y':
    Bill=Bill+40


print(f"Final bill for the order:{Bill}")









