def calc_adj_covariance(f, N, K, F):
    """
    Calculate the adjusted covariance between uniting gametes.
    Adds a factor to the covariance based on the population size relative to carrying capacity.

    Args:
    - f (float): The covariance between uniting gametes.
    - N (int): The size of the population.
    - K (int): The carrying capacity of the population.
    - F (float): The inbreeding coefficient in small population.

    Returns:
    - float: The adjusted covariance between uniting gametes.
    """

    return f + ((1-(N/K)) * F)