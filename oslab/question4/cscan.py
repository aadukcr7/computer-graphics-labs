# C-SCAN Disk Scheduling

disk_queue = list(map(int, input("Enter disk queue: ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

left = [i for i in disk_queue if i < head]
right = [i for i in disk_queue if i >= head]

left.sort()
right.sort()

order = []
total_movement = 0
current = head

for i in right:
    total_movement += abs(current - i)
    current = i
    order.append(i)

total_movement += (disk_size - 1 - current)  # Move to disk_size - 1
current = disk_size - 1
total_movement += (disk_size - 1)  # Jump to 0
current = 0

for i in left:
    total_movement += abs(current - i)
    current = i
    order.append(i)

print("\nExecution Order:", order)
print("Total Head Movement:", total_movement)
