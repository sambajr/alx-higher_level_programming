#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == () or tuple_b == ():
        if tuple_a == () and tuple_b == ():
            tuple_sum = (0, 0)
        elif tuple_a == () and len(tuple_b) < 2:
            tuple_sum = (
                0 + tuple_b[0],
                0 + (tuple_b[1] if len(tuple_b) == 2 else 0)
            )
        elif not tuple_a and len(tuple_b) >= 2:
            tuple_sum = (0 + tuple_b[0], 0 + tuple_b[1])
        elif not tuple_b and len(tuple_a) < 2:
            tuple_sum = ((0 + tuple_a[0]) if len(tuple_a) == 1 else 0, 0)
        elif not tuple_b and len(tuple_a) >= 2:
            tuple_sum = (0 + tuple_a[0], 0 + tuple_a[1])
        else:
            tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple_sum

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple_sum

    elif len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) < 2 and len(tuple_b) >= 2:
            tuple_sum = (tuple_a[0] + tuple_b[0], tuple_b[1] + 0)

        elif len(tuple_a) == 2 and len(tuple_b) < 2:
            tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)

        elif len(tuple_a) < 2 and len(tuple_b) < 2:
            tuple_sum = (tuple_a[0] + tuple_b[0], 0 + 0)

        return tuple_sum
