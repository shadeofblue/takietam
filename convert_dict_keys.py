
input_dict = { "TEST_INPUT": 1, "A_B_C": { "A_B_D": 'TEST' }, "A_B_D": "DD", "MAX": '1' }
# input_dict = { "TEST_INPUT": 1, "A_B_C": { "A_B_D": 'TEST' }, "A_B_D": "DD", "A_B": "dupa", "MAX": '1' }
expected = {"TEST":{"INPUT":1},"A":{"B":{"C":{"A":{"B":{"D":"TEST"}}},"D":"DD"}},"MAX":"1"}


def merge_dicts(d1, d2):
    items = list(d1.items())
    items.extend(list(d2.items()))

    new_dict = dict()
    for k, v in items:
        if k not in new_dict:
            new_dict[k] = v
        else:
            new_dict[k] = merge_dicts(new_dict[k], v)
    return new_dict

def unroll_dict(d):
    if not isinstance(d, dict):
        return d

    new_dict = dict()

    for k, v in d.items():
        new_keys = k.split("_", maxsplit=1)
        if len(new_keys) > 1:
            update = {new_keys[0]: unroll_dict({new_keys[1]: v})}
        else:
            update = {k: unroll_dict(v)}
        new_dict = merge_dicts(new_dict, update)

    return new_dict

print(unroll_dict(input_dict))
