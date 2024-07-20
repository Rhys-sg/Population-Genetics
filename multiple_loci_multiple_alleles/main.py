import matplotlib.pyplot as plt
import plotly 

from adj_by_fitness import adj_by_fitness
from adj_by_drift import adj_by_drift
from adj_by_mutation import adj_by_mutation

from calc_genotype_counts import calc_genotype_counts
from calc_genotype_freqs import calc_genotype_freqs
from calc_allele_counts import calc_allele_counts
from calc_allele_freqs import calc_allele_freqs
from calc_avg_fitness import calc_avg_fitness

from calc_next_pop import calc_next_pop
from calc_next_genotype_freqs import calc_next_genotype_freqs

# from plot.plot import create_combined_plot
from plot.plot_plotly import create_combined_plot

"""
Priority:
- avg_fitness (function, appending, graphing)
- fix carrying capacity
"""

"""
TODO:
variables:
- genotype_freqs -> genotype_counts
x growth_rate
- carrying_capacity
- bottleneck_yr
- bottleneck_pop
- non-random mating

small pops:
- pop-based drift (Make drift inversely proportional to the size of the population)
- inbreeding

maybes:
- linked loci
- recombination/crossing over
- genotype_fitness vs relative genotype_fitness (currently relative)

"""


def next_genotype_frequencies(generations, init_genotype_counts, genotype_fitness=None, growth_rate=1, carrying_capacity=None, drift=None, mutations=None):
    
    # Initialize values
    init_pop = sum(init_genotype_counts.values())
    init_genotype_freqs = calc_genotype_freqs(init_genotype_counts, init_pop)    
    init_allele_counts = calc_allele_counts(init_genotype_counts)
    init_allele_freq = calc_allele_freqs(init_allele_counts)
    init_avg_fitness = calc_avg_fitness(init_genotype_freqs, genotype_fitness)

    # Initialize lists for graphing
    gens_pop = [init_pop]
    gens_genotype_counts = [init_genotype_counts]
    gens_genotype_freqs = [init_genotype_freqs]
    gens_allele_counts = [init_allele_counts]
    gens_allele_freqs = [init_allele_freq]
    gens_avg_fitness = [init_avg_fitness]

    # Repeates for each generation
    for _ in range(generations):
        curr_genotype_counts = gens_genotype_counts[-1]

        # Apply evolutionary forces to genotypes in the current generation
        if genotype_fitness:
            curr_genotype_counts = adj_by_fitness(curr_genotype_counts, genotype_fitness)
        if drift:
            curr_genotype_counts = adj_by_drift(curr_genotype_counts, drift)

        # Apply evolutionary forces to alleles in the current generation
        curr_allele_counts = calc_allele_counts(curr_genotype_counts)
        if mutations:
            curr_allele_counts = adj_by_mutation(curr_allele_counts, mutations)
        
        # Calculate variables for recombination and growth
        curr_allele_freqs = calc_allele_freqs(curr_allele_counts)
        next_pop = calc_next_pop(gens_pop[-1], growth_rate, carrying_capacity)
        
        # Calculate the next generation
        next_genotype_freqs = calc_next_genotype_freqs(curr_allele_freqs)
        next_genotype_counts = calc_genotype_counts(next_genotype_freqs, next_pop)
        next_allele_counts = calc_allele_counts(next_genotype_counts)
        next_allele_freqs = calc_allele_freqs(next_allele_counts)
        next_avg_fitness = calc_avg_fitness(next_genotype_freqs, genotype_fitness)

        # Append the values to the lists
        gens_pop.append(next_pop)
        gens_genotype_counts.append(next_genotype_counts)
        gens_genotype_freqs.append(next_genotype_freqs)
        gens_allele_counts.append(next_allele_counts)
        gens_allele_freqs.append(next_allele_freqs)
        gens_avg_fitness.append(next_avg_fitness)

    fig = create_combined_plot(gens_pop,
                               gens_genotype_counts,
                               gens_genotype_freqs,
                               gens_allele_counts,
                               gens_allele_freqs,
                               gens_avg_fitness)
    fig.show()
    plt.show()

