import matplotlib.pyplot as plt
import plotly 

from calc_N import calc_N
from calc_next_N import calc_next_N
from calc_N_sub import calc_N_sub


from adj_by_fitness import adj_by_fitness
from adj_by_drift import adj_by_drift
from adj_by_mutation import adj_by_mutation

from calc_next_genotypes_data import calc_next_genotypes_data

from calc_genotype_counts import calc_genotype_counts
from calc_genotype_freqs import calc_genotype_freqs
from calc_allele_counts import calc_allele_counts
from calc_allele_freqs import calc_allele_freqs
from calc_avg_fitness import calc_avg_fitness

from calc_Ne import calc_Ne_over_generations

# from plot.plot import create_combined_plot
from plot.plot_plotly import create_combined_plot


"""
This function simulates the evolution of a population over multiple generations.

TODO:
- Change mutation implementation
- implement bottleneck
- implement muation

Design decisions/questions:
- Make drift only decrease population?

TODO (future):
- male/female fitness
- male/female covariance
- genotype covariance
"""


def pop_gen(generations,
            genotype_data,
            growth_rate=0,
            carrying_capacity=None,
            drift=None,
            mutation_rate=None,
            bottleneck_yr=None,
            bottleneck_N=None,
            covariance=0):
    
    # Transform genotype data
    gens_genotype_data = []

    # Repeates for each generation
    for i in range(generations):

        # Append the next generation to the list of generations
        gens_genotype_data.append(genotype_data)

        curr_genotypes_data = gens_genotype_data[-1]
        next_N = calc_next_N(calc_N(curr_genotypes_data), growth_rate, carrying_capacity)

        # Apply evolutionary forces to genotypes in the current generation
        curr_genotypes_data = adj_by_fitness(curr_genotypes_data)
        curr_genotypes_data = adj_by_drift(curr_genotypes_data, drift, calc_N(curr_genotypes_data), carrying_capacity)

        # If bottleneck, adjust population size, apply drift
        if bottleneck_yr == i and next_N > bottleneck_N:
            curr_genotypes_data = adj_by_drift(curr_genotypes_data, 1-bottleneck_N/next_N, bottleneck_N, carrying_capacity)
            next_N = bottleneck_N

        # Calculate the next generation
        genotype_data = calc_next_genotypes_data(curr_genotypes_data, next_N, covariance)
        genotype_data = adj_by_mutation(genotype_data, mutation_rate)


    # Initialize lists for each type of calculation
    gens_Nm, gens_Nf, gens_genotype_counts, gens_genotype_freqs, gens_allele_counts, gens_allele_freqs, gens_avg_fitness = ([] for _ in range(7))

    # Perform all calculations in a single loop
    for genotype_data in gens_genotype_data:
        gens_Nm.append(calc_N_sub(genotype_data, 'Nm'))
        gens_Nf.append(calc_N_sub(genotype_data, 'Nf'))
        gens_genotype_counts.append(calc_genotype_counts(genotype_data))
        gens_genotype_freqs.append(calc_genotype_freqs(genotype_data))
        allele_counts = calc_allele_counts(genotype_data)
        gens_allele_counts.append(allele_counts)
        gens_allele_freqs.append(calc_allele_freqs(allele_counts))
        gens_avg_fitness.append(calc_avg_fitness(genotype_data))

    # Calculate effective population sizes over generations
    gens_Ne = calc_Ne_over_generations(gens_Nm, gens_Nf, gens_allele_freqs)

    # Generate graphs
    fig = create_combined_plot(gens_Ne,
                               gens_genotype_counts,
                               gens_genotype_freqs,
                               gens_allele_counts,
                               gens_allele_freqs,
                               gens_avg_fitness)
    
    # Graph
    fig.show()
    plt.show()

