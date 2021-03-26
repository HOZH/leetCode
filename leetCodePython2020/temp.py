

def session_simulator(clients, regular):
    result = 0
    for i in clients:
        if regular >= i:
            regular -= i
            result += i
        else:
            result += regular
            remaining_time = i-regular
            result += remaining_time//2
            regular = 0
    return result


# Test cases
print(session_simulator([1, 2, 3, 1], 10))
print(session_simulator([4, 3, 4, 6, 2], 25))
print(session_simulator([7, 2, 1, 5, 3, 2], 30))
print(session_simulator([5, 5], 10))
print(session_simulator([1, 5, 4, 8, 7], 28))
print(session_simulator([5, 7, 5, 6], 20))
print(session_simulator([8, 6, 7, 5, 3, 9], 20))
print(session_simulator([8, 6, 7, 5, 3, 9], 30))
print(session_simulator([8, 6, 7, 5, 3, 9], 50))
print(session_simulator([20, 12, 6, 8, 14, 15, 9, 2], 75))
