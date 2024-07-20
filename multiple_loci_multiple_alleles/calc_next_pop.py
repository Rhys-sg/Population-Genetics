def calc_next_pop(N, r, K):
    """
    Calculates the size of the next population based on Verhulst's model:
    - dN/dt = rate of population change
    -     r = maximum population growth rate
    -     N = population size
    -     K = population carrying capacity
    """

    if not K:
        dN = N * r
    else:
        dN = r * N * (1 - (N / K))
    
    next_N = N + dN

    # Ensure the population size never goes negative
    next_N = max(1, next_N)

    return next_N
