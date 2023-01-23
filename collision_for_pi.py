from math import pi, atan, sqrt
import time

def get_num_collisions(m1, m2):
    theta = atan(sqrt(m2) / sqrt(m1))

    N = 1
    while True:
        val = N * theta
        if val < pi:
            N += 1
        else:
            break
    
    return (N - 1)

if __name__ == "__main__":
    x = int(input("Enter the power of 100: "))
    start = time.time()

    mass2 = 1
    mass1 = 100**x

    print(f"Number of collisions with mass ratio 100^{x}:1 is {get_num_collisions(mass1, mass2)}")
    end = time.time()
    print(f"Program executed in {round(end - start, 3)} seconds.")
