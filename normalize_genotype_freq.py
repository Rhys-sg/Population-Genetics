def normalize_genotype_freq(adj):
    # Calculate the sum of adjusted frequencies
    total_adj = sum(adj.values())
    
    # Normalize frequencies so they add up to 1
    if total_adj > 0:
        return {key: value / total_adj for key, value in adj.items()}
    else:
        # Handle the case where total_adj is 0 to avoid division by zero
        return {key: 0 for key in adj}
