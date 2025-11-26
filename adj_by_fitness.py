def adj_by_fitness(curr_genotypes_data):
    """
    Adjust genotype counts by their fitness.

    """
    for data in curr_genotypes_data.values():
        data['Nm'] = round(data['Nm'] * data['Wm'])
        data['Nf'] = round(data['Nf'] * data['Wf'])
    
    return curr_genotypes_data