# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    # start to end distance is 'distance'.
    # Max miles per tank is 'tank'.
    # Gas stations are at distances 'stops'
    # compute station spacing
    spaces = []
    # the first segment space
    spaces.append(stops[0])
    # the in-between segments
    for i in range(1, len(stops)):
        spaces.append(stops[i] - stops[i-1])
    # the last segment
    spaces.append(distance - stops[-1])
    # check for invalid route: max distance between adjacent gas stations > tank
    # impossible segment > tank returns -1
    if sorted(spaces, reverse=True)[0] > tank:
        return -1
    # take the longest first trek by
    i = 0
    fill = 0
    while distance > 0:
        if distance > tank:
            segment = 0.
            while segment + spaces[i] <= tank:
                segment += spaces[i]
                i += 1
            # add a fuel stop
            fill += 1
            distance -= segment
        else:
            # no more stops required. Can exit the loop
            distance = 0
    return fill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
