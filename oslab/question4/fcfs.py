# FCFS Disk Scheduling

disk_queue = list(map(int, input("Enter disk queue: ").split()))
head = int(input("Enter initial head position: "))

total_movement = 0
current = head
order = []

for track in disk_queue:
    total_movement += abs(track - current)
    current = track
    order.append(track)

print("\nExecution Order:", order)
print("Total Head Movement:", total_movement)
