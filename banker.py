# Author: Mahdi Safarian
# Lang: python
# Subject: Banker Algorithm. Deadlock detector.
# Date: 14/1/99
# Lead Master: Ali Kopai



def main():
    print("Enter number of processes: ")
    P = int(input())
    print("Enter number of resources: ")
    R = int(input())

    MaxResources = [int(i) for i in input("maximum resources : ").split()]

    print("\n Crrrent allocated for each process~")
    CurrentAllocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(P)]

    print("\n Max resources for each process~")
    MaxNeed = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(P)]

    Allo = [0] * R
    for i in range(P):
        for j in range(R):
            Allo[j] +=CurrentAllocated[i][j]
    print(f"\ntotal allocated resources : {Allo}")

    Ava = [MaxResources[i] - Allo[i] for i in range(R)]
    print(f"total available resources : {Ava}\n")

    Running = [True] * P
    Count = P
    while Count != 0:
        safe = False
        for i in range(P):
            if Running[i]:
                exe = True
                for j in range(R):
                    if MaxNeed[i][j] - CurrentAllocated[i][j] > Ava[j]:
                        exe = False
                        break
                if exe:
                    print(f"process {i + 1} is executing")
                    Running[i] = False
                    Count -=1
                    safe = True
                    for j in range(R):
                        Ava[j] += CurrentAllocated[i][j]
                    break
        if not safe:
            print("the proccess are in an unsafe state.")
            break

        print(f"the process is in a safe state. \n Available resources: {Ava}\n")

if __name__ == '__main__':
    main()

    print("thanks for your participation")
