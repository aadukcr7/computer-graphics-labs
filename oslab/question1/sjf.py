# SJF Non-Preemptive Scheduling

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    at = int(input(f"\nArrival Time of P{i+1}: "))
    bt = int(input(f"Burst Time of P{i+1}: "))
    processes.append([i+1, at, bt])

# Store original process data
original_processes = [p[:] for p in processes]

ct = [0] * n
wt = [0] * n
tat = [0] * n

processed = []
current_time = 0
execution_order = []  # Track execution order

for _ in range(n):
    # Find the process with minimum burst time that has arrived
    best = -1
    min_bt = float('inf')
    
    for i in range(n):
        if i not in processed and original_processes[i][1] <= current_time and original_processes[i][2] < min_bt:
            min_bt = original_processes[i][2]
            best = i
    
    # If no process has arrived, jump to the next arrival time
    if best == -1:
        best = min([i for i in range(n) if i not in processed], key=lambda x: original_processes[x][1])
        current_time = original_processes[best][1]
    
    # Execute the process
    current_time += original_processes[best][2]
    ct[best] = current_time
    tat[best] = ct[best] - original_processes[best][1]
    wt[best] = tat[best] - original_processes[best][2]
    processed.append(best)
    execution_order.append(f"P{original_processes[best][0]}")

print("\nP\tAT\tBT\tCT\tWT\tTAT")
for i in range(n):
    print(f"P{original_processes[i][0]}\t{original_processes[i][1]}\t{original_processes[i][2]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")

print(f"\nAverage Waiting Time: {sum(wt)/n}")
print(f"Average Turnaround Time: {sum(tat)/n}")

# Gantt Chart - Execution Order
print("\nGantt Chart (Execution Order):")
print(" -> ".join(execution_order))
