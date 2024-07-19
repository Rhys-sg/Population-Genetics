from adj_by_fitness import adj_by_fitness
from adj_by_drift import adj_by_drift
from adj_by_mutation import adj_by_mutation

from calc_genotype_freqs import calc_genotype_freqs
from calc_allele_freqs import calc_allele_freqs

from plot_genotype_freqs import plot_genotype_freqs
from plot_allele_freqs import plot_allele_freqs
from plot_freqs import create_combined_plot

import matplotlib.pyplot as plt

def next_genotype_frequencies(generations, genotype_freqs, genotype_fitness=None, drift=None, mutations=None):
    generational_genotype_freqs = [genotype_freqs]
    generational_allele_freqs = [calc_allele_freqs(genotype_freqs)]

    for _ in range(generations):
        current_genotype_freqs = generational_genotype_freqs[-1]
        if genotype_fitness: current_genotype_freqs = adj_by_fitness(current_genotype_freqs, genotype_fitness)
        if drift: current_genotype_freqs = adj_by_drift(current_genotype_freqs, drift)

        current_allele_freqs = calc_allele_freqs(current_genotype_freqs)
        if mutations: current_allele_freqs = adj_by_mutation(current_allele_freqs, mutations)

        next_genotype_freqs = calc_genotype_freqs(current_allele_freqs)

        generational_genotype_freqs.append(next_genotype_freqs)
        generational_allele_freqs.append(current_allele_freqs)

    fig = create_combined_plot(generational_allele_freqs, generational_genotype_freqs)
    plt.show()

