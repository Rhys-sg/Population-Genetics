import plotly.graph_objects as go
import plotly.colors as pc
from plotly.subplots import make_subplots

def format_genotype_key(genotype):
    return ', '.join(''.join(pair) for pair in genotype)

def create_combined_plot(gens_Ne, gens_genotype_counts, gens_genotype_freqs, gens_allele_counts, gens_allele_freqs, gens_avg_fitness):
    color_cycle = pc.qualitative.Plotly

    # Collect all keys for color assignment
    all_Ne = gens_Ne.keys()

    all_genotypes = set()
    for gen in gens_genotype_counts + gens_genotype_freqs:
        all_genotypes.update(gen.keys())
        
    all_alleles = set()
    for gens in gens_allele_counts + gens_allele_freqs:
        for locus in gens:
            all_alleles.update(locus.keys())

    all_keys = list(all_genotypes) + list(all_alleles) + list(all_Ne)
    colors = {key: color_cycle[i % len(color_cycle)] for i, key in enumerate(all_keys)}
    
    # Set population to black
    colors['N'] = 'black'

    # Process data
    def collect_data(gens_data):
        data = {}
        for gens_index, gen_data in enumerate(gens_data):
            for key, value in gen_data.items():
                if key not in data:
                    data[key] = [0] * len(gens_data)
                data[key][gens_index] = value
        return data

    def collect_nested_data(gens_data):
        data = {}
        for gens_index, gen_data in enumerate(gens_data):
            for locus_data in gen_data:
                for key, value in locus_data.items():
                    if key not in data:
                        data[key] = [0] * len(gens_data)
                    data[key][gens_index] = value
        return data

    genotype_counts_data = collect_data(gens_genotype_counts)
    genotype_freqs_data = collect_data(gens_genotype_freqs)
    allele_counts_data = collect_nested_data(gens_allele_counts)
    allele_freqs_data = collect_nested_data(gens_allele_freqs)

    # Create traces
    def add_traces(data, mode, title, y_label):
        traces = []
        for key, values in data.items():
            trace = go.Scatter(
                x=list(range(len(values))),
                y=values,
                mode=mode,
                name=format_genotype_key(key) if isinstance(key, tuple) else key,
                line=dict(color=colors.get(key, 'black')),
                hoverinfo='text',
                text=[f'{format_genotype_key(key) if isinstance(key, tuple) else key}: {value}' for value in values],
                showlegend=False  # Hide legend
            )
            traces.append(trace)
        return traces

    # Create subplots
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=[
            'Population Size Over Generations',
            'Genotype Counts Over Generations',
            'Genotype Frequencies Over Generations',
            'Average Fitness Over Generations',
            'Allele Counts Over Generations',
            'Allele Frequencies Over Generations'
        ]
    )

    traces = add_traces(gens_Ne, 'lines', 'Population Size and Effective Size Over Generations', 'Count')
    for trace in traces:
        fig.add_trace(trace, row=1, col=1)

    traces = add_traces(genotype_counts_data, 'lines', 'Genotype Counts Over Generations', 'Count')
    for trace in traces:
        fig.add_trace(trace, row=1, col=2)

    traces = add_traces(genotype_freqs_data, 'lines', 'Genotype Frequencies Over Generations', 'Frequency')
    for trace in traces:
        fig.add_trace(trace, row=1, col=3)

    traces = add_traces({'Average Fitness': gens_avg_fitness}, 'lines', 'Average Fitness Over Generations', 'Count')
    for trace in traces:
        fig.add_trace(trace, row=2, col=1)

    traces = add_traces(allele_counts_data, 'lines', 'Allele Counts Over Generations', 'Count')
    for trace in traces:
        fig.add_trace(trace, row=2, col=2)

    traces = add_traces(allele_freqs_data, 'lines', 'Allele Frequencies Over Generations', 'Frequency')
    for trace in traces:
        fig.add_trace(trace, row=2, col=3)

    # Update layout
    fig.update_layout(
        hovermode='closest',
        height=800
    )

    # Update y-axis range for frequency plots
    fig.update_yaxes(range=[0, 1], row=1, col=3)
    fig.update_yaxes(range=[0, 1], row=2, col=3)

    return fig
