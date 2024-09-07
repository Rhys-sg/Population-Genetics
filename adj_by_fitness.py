def adj_by_fitness(curr_genotypes_data):
    """
    Adjust genotype counts by their fitness.

    """
    for data in curr_genotypes_data.values():
        data['Nm'] = round(data['Nm'] * data['fitness'])
        data['Nf'] = round(data['Nf'] * data['fitness'])
    
    return curr_genotypes_data