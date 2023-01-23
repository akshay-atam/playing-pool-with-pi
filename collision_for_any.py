from math import pi, atan, sqrt

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
    # initialize m1 and m2 to zero
    m1 = int(input("Enter m1: "))
    m2 = int(input("Enter m2: "))

    collisions = get_num_collisions(m1, m2)

    print(f"Total number of collsions: {collisions}")