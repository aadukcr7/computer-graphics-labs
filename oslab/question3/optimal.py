# OPT Page Replacement with Table Output

ref = list(map(int, input("Enter reference string: ").split()))
frames = int(input("Enter number of frames: "))

memory = []
faults = 0
hits = 0

print("\nRef\tFrames\t\tStatus")
print("--------------------------------")

for i in range(len(ref)):
    page = ref[i]

    if page in memory:
        hits += 1
        status = "HIT"
    else:
        faults += 1
        status = "FAULT"

        if len(memory) < frames:
            memory.append(page)
        else:
            future = []
            for m in memory:
                if m in ref[i+1:]:
                    future.append(ref[i+1:].index(m))
                else:
                    future.append(9999)

            replace_index = future.index(max(future))
            memory[replace_index] = page

    print(f"{page}\t{memory}\t{status}")

print("\nTotal Page Faults =", faults)
print("Hit Ratio =", hits / len(ref))

