# SSTF Disk Scheduling

disk_queue = list(map(int, input("Enter disk queue: ").split()))
head = int(input("Enter initial head position: "))

total_movement = 0
current = head
order = []

queue = disk_queue.copy()

while queue:
    nearest = min(queue, key=lambda x: abs(x - current))
    total_movement += abs(nearest - current)
    current = nearest
    order.append(nearest)
    queue.remove(nearest)

print("\nExecution Order:", order)
print("Total Head Movement:", total_movement)
