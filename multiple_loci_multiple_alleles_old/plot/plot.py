import matplotlib.pyplot as plt
import itertools

def format_genotype_key(genotype):
    return ', '.join(''.join(pair) for pair in genotype)

def plot_data(ax, data, y_label, title, colors, data_type):
    for key, values in data.items():
        if data_type == 'population':
            ax.plot(range(len(values)), values, label=key)
        else:
            formatted_key = format_genotype_key(key) if isinstance(key, tuple) else key
            ax.plot(range(len(values)), values, label=formatted_key, color=colors.get(key, 'black'))
    ax.set_xlabel('Generation')
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)

def collect_data(gens_data, data_type):
    data = {}
    for gens_index, gen_data in enumerate(gens_data):
        for key, value in gen_data.items():
            if key not in data:
                data[key] = [0] * len(gens_data)
            data[key][gens_index] = value
    return data

def collect_nested_data(gens_data, data_type):
    data = {}
    for gens_index, gen_data in enumerate(gens_data):
        for locus_data in gen_data:
            for key, value in locus_data.items():
                if key not in data:
                    data[key] = [0] * len(gens_data)
                data[key][gens_index] = value
    return data

def assign_colors(all_keys, color_cycle):
    colors = {}
    for i, key in enumerate(all_keys):
        colors[key] = color_cycle[i % len(color_cycle)]
    return colors

def create_combined_plot(gens_pop, gens_genotype_counts, gens_genotype_freqs, gens_allele_counts, gens_allele_freqs, gens_avg_fitness):
    color_cycle = plt.cm.tab10.colors
    
    # Collect all keys for color assignment
    all_genotypes = set()
    for gen in gens_genotype_counts + gens_genotype_freqs:
        all_genotypes.update(gen.keys())
        
    all_alleles = set()
    for gens in gens_allele_counts + gens_allele_freqs:
        for locus in gens:
            all_alleles.update(locus.keys())

    all_keys = list(all_genotypes) + list(all_alleles)
    colors = assign_colors(all_keys, color_cycle)
    
    # Process data
    genotype_counts_data = collect_data(gens_genotype_counts, 'count')
    genotype_freqs_data = collect_data(gens_genotype_freqs, 'frequency')
    allele_counts_data = collect_nested_data(gens_allele_counts, 'count')
    allele_freqs_data = collect_nested_data(gens_allele_freqs, 'frequency')

    # Plot data
    fig, axs = plt.subplots(2, 3, figsize=(18, 10))

    plot_data(axs[0, 0], {'Population Size': gens_pop}, 'Count', 'Population Size Over Generations', colors, 'population')
    plot_data(axs[0, 1], genotype_counts_data, 'Count', 'Genotype Counts Over Generations', colors, 'genotype')
    plot_data(axs[1, 0], {'Average Fitness': gens_avg_fitness}, 'Count', 'Average Fitness Over Generations', colors, 'population')
    plot_data(axs[0, 2], genotype_freqs_data, 'Frequency', 'Genotype Frequencies Over Generations', colors, 'genotype')
    plot_data(axs[1, 1], allele_counts_data, 'Count', 'Allele Counts Over Generations', colors, 'allele')
    plot_data(axs[1, 2], allele_freqs_data, 'Frequency', 'Allele Frequencies Over Generations', colors, 'allele')

    plt.tight_layout()
    return fig
