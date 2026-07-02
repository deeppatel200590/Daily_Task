prices = [15000, 25000, 32000, 50000, 50000, 65000, 80000]

target = int(input("Enter minimum price: "))

low = 0
high = len(prices) - 1
answer = -1

while low <= high:
    mid = (low + high)//2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

if answer != -1:
    print("First product found at index:", answer)
    print("Price:", prices[answer])
else:
    print("No product found.")