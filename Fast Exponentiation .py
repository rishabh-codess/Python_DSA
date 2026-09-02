def fast_power(x: float, n: int) -> float:
    # Base Cases
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / fast_power(x, -n)

    # Divide step: Compute x^(n // 2) once
    half = fast_power(x, n // 2)

    # Conquer step
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


# Verification
print(f"2^10 = {fast_power(2, 10)}")  # 1024.0 (Computed in O(log N) calls)
print(f"3^5  = {fast_power(3, 5)}")  # 243.0