import matplotlib.pyplot as plt
import itertools

def format_genotype_key(genotype):
    return ', '.join(''.join(pair) for pair in genotype)

def plot_data(ax, data, y_label, title, colors, data_type):
    for key, values in data.items():
        formatted_key = format_genotype_key(key) if isinstance(key, tuple) else key
        ax.plot(range(len(values)), values, label=formatted_key, color=colors[key])
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

def create_combined_plot(gens_genotype_counts, gens_genotype_freqs, gens_allele_counts, gens_allele_freqs):
    # Create a list of colors for standardization
    color_cycle = plt.cm.tab10.colors
    colors = {}
    
    # Gather all unique genotypes and alleles
    all_genotypes = set()
    for gen in gens_genotype_counts + gens_genotype_freqs:
        all_genotypes.update(gen.keys())
        
    all_alleles = set()
    for gens in gens_allele_counts + gens_allele_freqs:
        for locus in gens:
            all_alleles.update(locus.keys())
    
    # Assign colors to genotypes and alleles
    for i, key in enumerate(itertools.chain(all_genotypes, all_alleles)):
        colors[key] = color_cycle[i % len(color_cycle)]
    
    fig, axs = plt.subplots(2, 2, figsize=(12, 6))

    # Plot Genotype Counts
    genotype_counts_data = collect_data(gens_genotype_counts, 'count')
    plot_data(axs[0, 0], genotype_counts_data, 'Count', 'Genotype Counts Over Generations', colors, 'genotype')

    # Plot Genotype Frequencies
    genotype_freqs_data = collect_data(gens_genotype_freqs, 'frequency')
    plot_data(axs[0, 1], genotype_freqs_data, 'Frequency', 'Genotype Frequencies Over Generations', colors, 'genotype')

    # Plot Allele Counts
    allele_counts_data = collect_nested_data(gens_allele_counts, 'count')
    plot_data(axs[1, 0], allele_counts_data, 'Count', 'Allele Counts Over Generations', colors, 'allele')

    # Plot Allele Frequencies
    allele_freqs_data = collect_nested_data(gens_allele_freqs, 'frequency')
    plot_data(axs[1, 1], allele_freqs_data, 'Frequency', 'Allele Frequencies Over Generations', colors, 'allele')

    plt.tight_layout()
    return fig

