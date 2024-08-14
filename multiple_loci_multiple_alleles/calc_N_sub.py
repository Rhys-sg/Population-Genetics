def calc_N_sub(curr_genotypes_data, sub_pop):
    """
    Counts the poopulation size for males or females
    
    """
    return sum([data[sub_pop] for data in curr_genotypes_data.values()])
