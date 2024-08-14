import matplotlib.pyplot as plt
import plotly 

from transform_genotype_data import transform_genotype_data, calc_genotype_counts_from_mf, calc_sex_counts

from adj_by_fitness import adj_by_fitness
from adj_by_drift import adj_by_drift
from adj_by_mutation import adj_by_mutation

from calc_genotype_counts import calc_genotype_counts
from calc_genotype_freqs import calc_genotype_freqs
from calc_allele_counts import calc_allele_counts
from calc_allele_freqs import calc_allele_freqs
from calc_avg_fitness import calc_avg_fitness

from calc_adj_covariance import calc_adj_covariance
from calc_sex_freq import calc_sex_freq
from calc_next_N import calc_next_N
from calc_next_genotype_freqs import calc_next_genotype_freqs

from calc_Ne import calc_Ne_over_generations

# from plot.plot import create_combined_plot
from plot.plot_plotly import create_combined_plot


"""
This function simulates the evolution of a population over multiple generations.

Args:
- generations: The number of generations to simulate.
- genotype_data: A dictionary with all possible genotypes and properties for each genotype:
    - male population size
    - female population size
    - relative fitness
- growth_rate: The growth rate of the population.
- carrying_capacity: The carrying capacity of the population.
- drift: The rate of genetic drift.
- mutations: The rate of mutations.
- bottleneck_yr: The year in which a bottleneck event occurs.
- bottleneck_pop: The population size after the bottleneck event.
- covariance: The covariance between uniting gametes.
- small_pop_inbreeding: The inbreeding coefficient in small populations. (Not sure if I want this)

TODO:
variables:
- male/female populations, mating, fitness
- linked loci/crossing over

- Change mutation implementation
"""


def pop_gen(generations,
            genotype_data,
            growth_rate=0,
            carrying_capacity=None,
            drift=None,
            mutations=None,
            bottleneck_yr=None,
            bottleneck_N=None,
            covariance=0,
            small_pop_inbreeding=0):
    
    # Transform genotype data
    genotype_m, genotype_f, genotype_fitness = transform_genotype_data(genotype_data)
    init_genotype_counts = calc_genotype_counts_from_mf(genotype_m, genotype_f)
    init_Nm, init_Nf = calc_sex_counts(genotype_m, genotype_f)
    
    # Initialize values
    init_N = sum(init_genotype_counts.values())
    init_genotype_freqs = calc_genotype_freqs(init_genotype_counts, init_N)    
    init_allele_counts = calc_allele_counts(init_genotype_counts)
    init_allele_freq = calc_allele_freqs(init_allele_counts)
    init_avg_fitness = calc_avg_fitness(init_genotype_freqs, genotype_fitness)

    # Initialize lists to track values over generations
    gens_N = [init_N]
    gens_Nm = [init_Nm]
    gens_Nf = [init_Nf]
    gens_genotype_counts = [init_genotype_counts]
    gens_genotype_freqs = [init_genotype_freqs]
    gens_allele_counts = [init_allele_counts]
    gens_allele_freqs = [init_allele_freq]
    gens_avg_fitness = [init_avg_fitness]
    gens_covariance = [covariance]

    # Repeates for each generation
    for i in range(generations):
        curr_genotype_counts = gens_genotype_counts[-1]

        # Calculate population size for the next generation, apply bottleneck
        if bottleneck_yr == i and next_N > bottleneck_N:
            curr_genotype_counts = adj_by_drift(curr_genotype_counts, 1-bottleneck_N/next_N, bottleneck_N, carrying_capacity)
            next_N = bottleneck_N
        else:
            next_N = calc_next_N(gens_N[-1], growth_rate, carrying_capacity)

        # Apply evolutionary forces to genotypes in the current generation
        if genotype_fitness:
            curr_genotype_counts = adj_by_fitness(curr_genotype_counts, genotype_fitness)
        if drift:
            curr_genotype_counts = adj_by_drift(curr_genotype_counts, drift, next_N, carrying_capacity)

        # Apply evolutionary forces to alleles in the current generation
        curr_allele_counts = calc_allele_counts(curr_genotype_counts)
        if mutations:
            curr_allele_counts = adj_by_mutation(curr_allele_counts, mutations)

        # Calculate variables for recombination and growth
        curr_allele_freqs = calc_allele_freqs(curr_allele_counts)
        adj_covariance = calc_adj_covariance(covariance, next_N, carrying_capacity, small_pop_inbreeding)

        # TODO: Calculate the male/female populations for the next generation
        next_Nm = calc_sex_freq(gens_Nm[-1], gens_Nf[-1]) * next_N
        next_Nf = calc_sex_freq(gens_Nf[-1], gens_Nm[-1]) * next_N
        
        # Calculate the next generation
        next_genotype_freqs = calc_next_genotype_freqs(curr_allele_freqs, adj_covariance)
        next_genotype_counts = calc_genotype_counts(next_genotype_freqs, next_N)
        next_allele_counts = calc_allele_counts(next_genotype_counts)
        next_allele_freqs = calc_allele_freqs(next_allele_counts)
        next_avg_fitness = calc_avg_fitness(next_genotype_freqs, genotype_fitness)

        # Append the values to the lists
        gens_N.append(next_N)
        gens_Nm.append(next_Nm)
        gens_Nf.append(next_Nf)
        gens_genotype_counts.append(next_genotype_counts)
        gens_genotype_freqs.append(next_genotype_freqs)
        gens_allele_counts.append(next_allele_counts)
        gens_allele_freqs.append(next_allele_freqs)
        gens_avg_fitness.append(next_avg_fitness)
        gens_covariance.append(adj_covariance)

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

