from adj_by_fitness import adj_by_fitness
from adj_by_drift import adj_by_drift
from adj_by_mutation import adj_by_mutation

from calc_genotype_freqs import calc_genotype_freqs
from calc_allele_freqs import calc_allele_freqs
from calc_allele_counts import calc_allele_counts

from calc_next_generation_genotype_count import calc_next_generation_genotype_count

from plot_genotype_freqs import plot_genotype_freqs
from plot_allele_freqs import plot_allele_freqs
from plot_freqs import create_combined_plot

import matplotlib.pyplot as plt
"""
TODO:
variables:
- genotype_freqs -> genotype_counts
- growth_rate
- bottleneck_yr
- bottleneck_pop

small pops:
- pop-based drift
- inbreeding

maybes:
- linked loci
- recombination/crossing over
- genotype_fitness vs relative genotype_fitness (currently relative)

"""


def next_genotype_frequencies(generations, init_genotype_counts, growth_rate=1, genotype_fitness=None, drift=None, mutations=None):
    
    # Initialize values
    init_pop = sum(init_genotype_counts.values())
    init_genotype_freqs = calc_genotype_freqs(init_genotype_counts, init_pop)    
    init_allele_counts = calc_allele_counts(init_genotype_counts)
    init_allele_freq = calc_allele_freqs(init_allele_counts)

    # Initialize lists for graphing
    gens_genotype_counts = [init_genotype_counts]
    gens_genotype_freqs = [init_genotype_freqs]
    gens_allele_counts = [init_allele_counts]
    gens_allele_freqs = [init_allele_freq]

    # Repeates for each generation
    for _ in range(generations):
        curr_genotype_counts = gens_genotype_counts[-1]

        # Apply evolutionary forces
        if genotype_fitness:
            curr_genotype_counts = adj_by_fitness(curr_genotype_counts, genotype_fitness)
        if drift:
            curr_genotype_counts = adj_by_drift(curr_genotype_counts, drift)

        current_allele_freqs = calc_allele_freqs(curr_genotype_counts)
        if mutations: current_allele_freqs = adj_by_mutation(current_allele_freqs, mutations)

        next_genotype_freqs = calc_next_generation_genotype_count(current_allele_freqs)

        gens_genotype_freqs.append(next_genotype_freqs)
        gens_allele_freqs.append(current_allele_freqs)

    fig = create_combined_plot(gens_allele_freqs, gens_genotype_freqs)
    plt.show()

