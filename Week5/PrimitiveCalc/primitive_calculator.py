# Uses python3
import sys

# iterate through the numbers from 2 through n to obtain the least number of operations
# needed to compute each of the values from the given set of operations *2 *3 +1
# the ops list stores the count of operations to compute number equal to the index
# the calcs list stores the calculated factors
# the result will be a list with the number n, the next factor value obtained in the process etc
def optimal_sequence(n):
    # initialize the operations and factors list for zero index and first trivial entry
    ops = [-1, 0]

    calcs = [0, 1]
    # construct a list, ops, of the min ways to get number of the index: for example: 6 can be from (1 + 1) * 3
    for i in range(2, n + 1):
        o1 = n
        o2 = n
        o3 = n
        # if divisible by 3
        if i % 3 == 0:
            o3 = ops[int(i / 3)]
        # if divisible by 2
        if i & 1 == 0: # this is same as i mod 2, except more efficient
            o2 = ops[int(i / 2)]
        # the last operation result
        if i - 1 >= 0:
            o1 = ops[i - 1]
        # build the calcs list with the min factors
        k = min(o1, o2, o3)
        ops.append(k+1)
        if o3 <= min(o1, o2):
            calcs.append(int(i / 3))
        elif o2 <= min(o3, o1):
            calcs.append(int(i / 2))
        elif o1 <= min(o3, o2):
            calcs.append(i - 1)
    # starting with the target n
    result = [n]
    # append the calculated sub element at the nth location
    for i in range(ops[n]):
        result.append(calcs[n])
        n = calcs[n]

    return reversed(result)



def optimal_sequence_greedy(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
