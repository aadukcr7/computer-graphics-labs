# C-LOOK Disk Scheduling

disk_queue = list(map(int, input("Enter disk queue: ").split()))
head = int(input("Enter initial head position: "))

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

if left:  # Only process left if it's not empty
    total_movement += abs(order[-1] - left[0])
    current = left[0]
    
    for i in left:
        total_movement += abs(current - i)
        current = i
        order.append(i)

print("\nExecution Order:", order)
print("Total Head Movement:", total_movement)
