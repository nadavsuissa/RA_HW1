# Sort Function
def sort_dict(item: dict):
    return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(item.items())}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Q2")
    tr = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print(sort_dict(tr))

   
