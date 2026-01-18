# FIFO Page Replacement with Table Output

ref = list(map(int, input("Enter reference string: ").split()))
frames = int(input("Enter number of frames: "))

memory = []
faults = 0
hits = 0

print("\nRef\tFrames\t\tStatus")
print("--------------------------------")

for page in ref:
    if page in memory:
        hits += 1
        status = "HIT"
    else:
        faults += 1
        status = "FAULT"
        if len(memory) < frames:
            memory.append(page)
        else:
            memory.pop(0)
            memory.append(page)

    print(f"{page}\t{memory}\t{status}")

print("\nTotal Page Faults =", faults)
print("Hit Ratio =", hits / len(ref))
