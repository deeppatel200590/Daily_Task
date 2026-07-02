blacklist = ["free", "win", "winner", "cash", "prize","spam","virus"]
sender=input("Enter the sender's email address: ")

for i in blacklist:
    if i in sender:
        print("This email is spam.")
        break
else:
    print("This email is not spam.")