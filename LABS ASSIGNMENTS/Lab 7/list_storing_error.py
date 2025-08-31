
def sort_list(data):
    integers = sorted([item for item in data if isinstance(item, int)])
    strings = sorted([item for item in data if isinstance(item, str)])
    return integers + strings  # Combine sorted integers and strings

items = [5, "vishwas", 6, "raju", 10]
print(sort_list(items))