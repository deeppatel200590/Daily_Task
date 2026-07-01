belt = [None]*8

for i in range(8):
    product=input("Enter the product name:")
    if product == "":
        belt[i]=None
        continue
    belt[i]=product

print(belt)

slot=int(input("Enter the slot number to check (0-7):"))
if 0 <= slot < 8:
    if belt[slot] is None:
        print(f"Slot {slot} is empty.")
    else:
        print(f"Slot {slot} contains: {belt[slot]}")
else:
    print("Invalid slot number.")

find_item = input("Enter the product name to find:")
found = False
count = 0
for i in range(8):
    if belt[i] == find_item:
        found = True
        print(f"{find_item} is on the belt at slot {i}.")
        count += 1
if found:
    print(f"{find_item} appears {count} times on the belt.")
else:
    print(f"{find_item} is not on the belt.")

update_item=int(input("Enter the slot number to update (0-7):"))
new_item=input("Enter the new product name:")
if 0 <= update_item < 8:
    belt[update_item] = new_item
    print(f"Slot {update_item} updated to: {new_item}")
else:
    print("Invalid slot number.")

full = True
for i in range(8):
    if belt[i] is None:
        full = False
        break
if full:
    print("The belt is full.")
else:
    print("The belt is not full.")