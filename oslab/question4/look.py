# LOOK Disk Scheduling

disk_queue = list(map(int, input("Enter disk queue: ").split()))
head = int(input("Enter initial head position: "))
direction = input("Direction (left/right): ")

left = [i for i in disk_queue if i < head]
right = [i for i in disk_queue if i >= head]

left.sort(reverse=True)
right.sort()

order = []
total_movement = 0
current = head

if direction == "left":
    for i in left:
        total_movement += abs(current - i)
        current = i
        order.append(i)
    for i in right:
        total_movement += abs(current - i)
        current = i
        order.append(i)
else:
    for i in right:
        total_movement += abs(current - i)
        current = i
        order.append(i)
    for i in left:
        total_movement += abs(current - i)
        current = i
        order.append(i)

print("\nExecution Order:", order)
print("Total Head Movement:", total_movement)
