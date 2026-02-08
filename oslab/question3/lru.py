# LRU Page Replacement with Table Output

ref = list(map(int, input("Enter reference string: ").split()))
frames = int(input("Enter number of frames: "))

memory = []
recent = []
faults = 0
hits = 0

print("\nRef\tFrames\t\tStatus")
print("--------------------------------")

for page in ref:
    if page in memory:
        hits += 1
        status = "HIT"
        recent.remove(page)
        recent.append(page)
    else:
        faults += 1
        status = "FAULT"

        if len(memory) < frames:
            memory.append(page)
            recent.append(page)
        else:
            lru = recent.pop(0)
            index = memory.index(lru)
            memory[index] = page
            recent.append(page)

    print(f"{page}\t{memory}\t{status}")

print("\nTotal Page Faults =", faults)
print("Hit Ratio =", hits / len(ref))
