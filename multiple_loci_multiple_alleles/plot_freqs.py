import matplotlib.pyplot as plt

def plot_allele_freqs(ax, generation_allele_freqs):
    # Create a dictionary to store allele frequencies across generations
    allele_data = {}

    # Collect all data for plotting
    for generation_index, allele_freqs in enumerate(generation_allele_freqs):
        for locus, freqs in enumerate(allele_freqs):
            for allele, freq in freqs.items():
                if allele not in allele_data:
                    allele_data[allele] = {'generations': [], 'frequencies': []}
                allele_data[allele]['generations'].append(generation_index)
                allele_data[allele]['frequencies'].append(freq)
    
    # Plot each allele's frequency over generations
    for allele, data in allele_data.items():
        ax.plot(data['generations'], data['frequencies'], label=allele)
    
    ax.set_xlabel('Generation')
    ax.set_ylabel('Frequency')
    ax.set_title('Allele Frequencies Over Generations')
    ax.legend()
    ax.grid(True)

def plot_genotype_freqs(ax, generation_genotype_freqs):
    # Get all unique genotype keys
    all_genotypes = set()
    for gen in generation_genotype_freqs:
        all_genotypes.update(gen.keys())
    
    # Create a dictionary to hold frequency lists for each genotype
    freq_data = {genotype: [] for genotype in all_genotypes}
    
    # Fill the dictionary with frequency data
    for gen in generation_genotype_freqs:
        for genotype in all_genotypes:
            freq_data[genotype].append(gen.get(genotype, 0))
    
    # Plotting
    for genotype, freqs in freq_data.items():
        genotype_formatted = ', '.join(''.join(pair) for pair in genotype)
        ax.plot(range(len(generation_genotype_freqs)), freqs, label=genotype_formatted)
    
    ax.set_xlabel('Generation')
    ax.set_ylabel('Frequency')
    ax.set_title('Genotype Frequencies Over Generations')
    ax.legend()
    ax.grid(True)

def create_combined_plot(generation_allele_freqs, generation_genotype_freqs):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    plot_genotype_freqs(ax1, generation_genotype_freqs)
    plot_allele_freqs(ax2, generation_allele_freqs)

    
    plt.tight_layout()

    # plt.show()
    
    return fig
