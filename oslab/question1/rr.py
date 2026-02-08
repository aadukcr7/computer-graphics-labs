# Round Robin Scheduling

import collections

n = int(input("Enter number of processes: "))
quantum = int(input("Enter Time Quantum: "))

arrival = []
burst = []
remaining = []

for i in range(n):
    arrival.append(int(input(f"\nArrival Time of P{i+1}: ")))
    burst.append(int(input(f"Burst Time of P{i+1}: ")))
    remaining.append(burst[i])

completion = [0] * n
waiting = [0] * n
turnaround = [0] * n

time = 0
completed = 0
queue = collections.deque()
processed_list = [False] * n
execution_order = []

while completed < n:
    # Add newly arrived processes to queue
    for i in range(n):
        if arrival[i] <= time and not processed_list[i] and remaining[i] > 0 and i not in queue:
            queue.append(i)
    
    if not queue:
        # No process ready, jump to next arrival
        next_arrival = min([arrival[i] for i in range(n) if remaining[i] > 0])
        time = next_arrival
        for i in range(n):
            if arrival[i] == next_arrival and remaining[i] > 0:
                queue.append(i)
                break
    else:
        # Execute process from front of queue
        i = queue.popleft()
        
        if remaining[i] > quantum:
            time += quantum
            remaining[i] -= quantum
            execution_order.append(f"P{i+1}")
            queue.append(i)  # Put back in queue
        else:
            time += remaining[i]
            execution_order.append(f"P{i+1}")
            remaining[i] = 0
            completion[i] = time
            turnaround[i] = completion[i] - arrival[i]
            waiting[i] = turnaround[i] - burst[i]
            completed += 1
            processed_list[i] = True

print("\nP\tAT\tBT\tCT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{arrival[i]}\t{burst[i]}\t{completion[i]}\t{waiting[i]}\t{turnaround[i]}")

print(f"\nAverage Waiting Time: {sum(waiting)/n}")
print(f"Average Turnaround Time: {sum(turnaround)/n}")

# Gantt Chart - Execution Order
print("\nGantt Chart (Execution Order):")
print(" -> ".join(execution_order))
