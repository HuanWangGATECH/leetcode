
# a child is running up staircase with n steps and can hop 1 step 2 step or 3 steps at a time. Implement a method to count how many possible ways the child can run up stairs

def triple_hop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)


if __name__ == "__main__":
    print(triple_hop(1))
    print(triple_hop(2))
    print(triple_hop(3))
    print(triple_hop(4))
    print(triple_hop(5))
    print(triple_hop(6))

    print(method_2(1))
    print(method_2(2))
    print(method_2(3))
    print(method_2(4))
    print(method_2(5))
    print(method_2(6))
