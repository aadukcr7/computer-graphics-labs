# SCAN Disk Scheduling

disk_queue = list(map(int, input("Enter disk queue: ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))
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
    total_movement += current
    current = 0
    for i in right:
        total_movement += abs(current - i)
        current = i
        order.append(i)
else:
    for i in right:
        total_movement += abs(current - i)
        current = i
        order.append(i)
    total_movement += (disk_size - 1 - current)
    current = disk_size - 1
    for i in left:
        total_movement += abs(current - i)
        current = i
        order.append(i)

print("\nExecution Order:", order)
print("Total Head Movement:", total_movement)
