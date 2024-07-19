import matplotlib.pyplot as plt

def plot_genotype_freqs(generation_genotype_freqs):
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
    plt.figure(figsize=(10, 6))
    for genotype, freqs in freq_data.items():
        plt.plot(range(len(generation_genotype_freqs)), freqs, label=str(genotype))
    
    plt.xlabel('Generation')
    plt.ylabel('Frequency')
    plt.title('Genotype Frequencies Over Generations')
    plt.legend()
    plt.show()
