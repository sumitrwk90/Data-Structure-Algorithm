
def countdown(n):

    # Base case...
    if n == 0:
        return
    
    # Recursive case...
    print(f"countdown({n})")
    countdown(n-1)

    # Backtracking case...return from call stack
    print(f"countdown({n})")

if __name__ == "__main__":
    countdown(5)
    