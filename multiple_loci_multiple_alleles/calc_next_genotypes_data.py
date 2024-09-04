from generate_punnett_square import generate_punnett_square
from calc_N import calc_N

def calc_next_genotypes_data(curr_genotypes_data, next_N, f):

    N = calc_N(curr_genotypes_data)

    # Initialize next generation genotype data with 0 Nm and Nf
    next_genotypes_data = {}
    for genotype, data in curr_genotypes_data.items():
        next_genotypes_data[genotype] = {'Nm': 0, 'Nf': 0, 'fitness': data['fitness']}

    # Iterate over all pairs of parent genotypes
    for genotype_A, data_A in curr_genotypes_data.items():
        for genotype_B, data_B in curr_genotypes_data.items():
            # Generate Punnett square for the parent pair
            punnett_square = generate_punnett_square(genotype_A, genotype_B)
            
            # Calculate the total number of matings between genotype_A and genotype_B
            matings_AB = data_A['Nm'] * data_B['Nf']
            matings_BA = data_B['Nm'] * data_A['Nf']
            
            # Apply the covariance factor f
            if genotype_A == genotype_B:
                total_matings = (matings_AB + matings_BA) / N * (1 + f)
            else:
                total_matings = (matings_AB + matings_BA) / N * (1 - f)

            # Distribute offspring based on Punnett square frequencies
            for genotype, frequency in punnett_square.items():
                offspring_count = total_matings * frequency
                next_genotypes_data[genotype]['Nm'] += offspring_count / 2
                next_genotypes_data[genotype]['Nf'] += offspring_count / 2

    # Normalize the frequencies to ensure they add up to 1
    total_frequency = sum([data['Nm'] + data['Nf'] for data in next_genotypes_data.values()])
    for genotype, data in next_genotypes_data.items():
        data['Nm'] /= total_frequency
        data['Nf'] /= total_frequency

    # Turn the frequencies back into counts, applying the growth rate
    for genotype, data in next_genotypes_data.items():
        data['Nm'] = round(data['Nm'] * next_N)
        data['Nf'] = round(data['Nf'] * next_N)

    return next_genotypes_data