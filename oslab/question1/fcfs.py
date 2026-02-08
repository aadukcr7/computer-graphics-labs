# FCFS Scheduling

n = int(input("Enter number of processes: "))

arrival = []
burst = []

for i in range(n):
    print(f"\nProcess P{i+1}")
    arrival.append(int(input("Arrival Time: ")))
    burst.append(int(input("Burst Time: ")))

# Store original order
processes = [[i+1, arrival[i], burst[i]] for i in range(n)]

# Sort by arrival time
processes.sort(key=lambda x: x[1])

completion = [0] * n
waiting = [0] * n
turnaround = [0] * n

# First process completion time
completion[0] = processes[0][1] + processes[0][2]

# Completion time for others
for i in range(1, n):
    completion[i] = completion[i-1] + processes[i][2]

# Turnaround & Waiting time
for i in range(n):
    turnaround[i] = completion[i] - processes[i][1]
    waiting[i] = turnaround[i] - processes[i][2]

print("\nP\tAT\tBT\tCT\tWT\tTAT")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{completion[i]}\t{waiting[i]}\t{turnaround[i]}")

print(f"\nAverage Waiting Time: {sum(waiting)/n}")
print(f"Average Turnaround Time: {sum(turnaround)/n}")

# Gantt Chart - Execution Order
print("\nGantt Chart (Execution Order):")
gantt = " -> ".join([f"P{processes[i][0]}" for i in range(n)])
print(gantt)
