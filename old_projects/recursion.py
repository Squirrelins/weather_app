def binary_search_loop(lst, num):
    """Binary search using a loop"""
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return None

def binary_search_recursion(list, x, high, low):
    """Binary search using recursion"""
    if high >= low:
        mid = (high + low) // 2
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return binary_search_recursion(list, x, low, mid - 1)
        elif list[mid] < x:
            return binary_search_recursion(list, x, mid + 1, high)
    else:
        return -1
    
    