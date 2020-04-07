"""Simulation of Banker algorithm for predicting deadlocks in operating system"""
# Author: Mahdi Safarian
# Lang: python
# Subject: Banker Algorithm. Deadlock detector.
# Date: 14/1/99
# Lead Master: Ali Kopai



def main():
    """Start point of the program"""
    print("Enter the number of processes: ")
    p = int(input())
    print("Enter the number of resources: ")
    r = int(input())

    max_resources = [int(i) for i in input("Maximum resources: ").split()]

    print("\n Current allocated for each process~")
    current_allocated = [[int(i) for i in input(f"Process {j + 1}: ").split()] for j in range(p)]

    print("\n Maximum resources for each process~")
    max_need = [[int(i) for i in input(f"Process {j + 1}: ").split()] for j in range(p)]

    allo = [0] * r
    for i in range(p):
        for j in range(r):
            allo[j] += current_allocated[i][j]
    print(f"\nTotal allocated resources = {allo}")

    ava = [max_resources[i] - allo[i] for i in range(r)]
    print(f"Total available resources = {ava}\n")

    running = [True] * p
    count = p
    while count != 0:
        safe = False
        for i in range(p):
            if running[i]:
                exe = True
                for j in range(r):
                    if max_need[i][j] - current_allocated[i][j] > ava[j]:
                        exe = False
                        break
                if exe:
                    print(f"Process {i + 1} is executing...")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(r):
                        ava[j] += current_allocated[i][j]
                    break
        if not safe:
            print("The proccesses are in an unsafe state.")
            break

        print(f"The processes are is in a safe state. \n Available resources = {ava}\n")

if __name__ == '__main__':
    main()
    print("Thanks for your participation")
