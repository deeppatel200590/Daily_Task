front=-1
rear=-1
queue=[None]*5
while True:
    print("1.Add vehicle")
    print("2.Remove vehicle")
    print("3.Display queue")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        if(rear == 4 and front == 0) or (rear + 1 == front):
            print("Queue is full")
        else:
            vehicle = input("Enter vehicle number: ")
            if front == -1:
                front=0
            if rear == 4:
                rear=0
            else:
                rear+=1
            queue[rear] = vehicle
    elif(choice == 2):
        if front == -1:
            print("Queue is empty")
        else:
            print(f"Vehicle {queue[front]} removed from the queue")
            if front == rear:
                front = -1
                rear = -1
            elif front == 4:
                front = 0
            else:
                front += 1
    elif(choice == 3):
        if front == -1:
            print("Queue is empty")
        else:
            print("Vehicles in the queue:")
            if rear >= front:
                for i in range(front, rear + 1):
                    print(queue[i])
            else:
                for i in range(front, 5):
                    print(queue[i])
                for i in range(0, rear + 1):
                    print(queue[i])
    elif(choice == 4):
        break