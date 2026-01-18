# SJF Preemptive (SRTF)

n = int(input("Enter number of processes: "))

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
execution_order = []

while completed < n:
    idx = -1
    min_bt = 9999

    for i in range(n):
        if arrival[i] <= time and remaining[i] > 0 and remaining[i] < min_bt:
            min_bt = remaining[i]
            idx = i

    if idx == -1:
        time += 1
        continue

    remaining[idx] -= 1
    time += 1
    
    # Track only when process completes or first executes
    if remaining[idx] == 0:
        completed += 1
        completion[idx] = time
        turnaround[idx] = completion[idx] - arrival[idx]
        waiting[idx] = turnaround[idx] - burst[idx]
    
    if not execution_order or execution_order[-1] != f"P{idx+1}":
        execution_order.append(f"P{idx+1}")

print("\nP\tAT\tBT\tCT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{arrival[i]}\t{burst[i]}\t{completion[i]}\t{waiting[i]}\t{turnaround[i]}")

print(f"\nAverage Waiting Time: {sum(waiting)/n}")
print(f"Average Turnaround Time: {sum(turnaround)/n}")

# Gantt Chart - Execution Order
print("\nGantt Chart (Execution Order):")
print(" -> ".join(execution_order))
