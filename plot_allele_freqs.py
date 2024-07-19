import matplotlib.pyplot as plt

def plot_allele_freqs(generational_genotype_freqs):
    plt.figure(figsize=(10, 6))
    
    # Create a dictionary to store allele frequencies across generations
    allele_data = {}

    # Collect all data for plotting
    for generation_index, allele_freqs in enumerate(generational_genotype_freqs):
        for locus, freqs in enumerate(allele_freqs):
            for allele, freq in freqs.items():
                if allele not in allele_data:
                    allele_data[allele] = {'generations': [], 'frequencies': []}
                allele_data[allele]['generations'].append(generation_index)
                allele_data[allele]['frequencies'].append(freq)
    
    # Plot each allele's frequency over generations
    for allele, data in allele_data.items():
        plt.plot(data['generations'], data['frequencies'], label=allele)
    
    plt.xlabel('Generation')
    plt.ylabel('Frequency')
    plt.title('Allele Frequencies Over Generations')
    plt.legend()
    plt.grid(True)
    plt.show()
