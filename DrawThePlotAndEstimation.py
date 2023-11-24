import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

def analyze_corpus(file_path, corpus_name, file_type='csv'):
    # Read data based on file type
    if file_type == 'csv':
        data = pd.read_csv(file_path, header=None, names=['n', 'm'])
        data = data.drop(0)  # Drop the first row
    elif file_type == 'pkl':
        data = pd.read_pickle(file_path)
    else:
        raise ValueError("Unsupported file type")

    # Fit model
    X = sm.add_constant(np.log10(data['n']))
    model = sm.OLS(np.log10(data['m']), X).fit()

    # Summary statistics
    alpha_hat = 10 ** model.params[0]
    beta_hat = model.params[1]
    rsq = model.rsquared
    print(f"{corpus_name} - alpha (est): {alpha_hat:.4f}, beta (est): {beta_hat:.4f}, R squared: {rsq:.4f}")

    # Confidence intervals
    conf_int = model.conf_int(alpha=0.1)  # 90% CI
    alpha_ci_low, alpha_ci_high = 10 ** conf_int.iloc[0, 0], 10 ** conf_int.iloc[0, 1]
    beta_ci_low, beta_ci_high = conf_int.iloc[1, 0], conf_int.iloc[1, 1]
    print(f"{corpus_name} - 90% CI for alpha: [{alpha_ci_low:.4f}, {alpha_ci_high:.4f}]")
    print(f"{corpus_name} - 90% CI for beta: [{beta_ci_low:.4f}, {beta_ci_high:.4f}]")

    return data, model.params

pubmed_data, pubmed_params = analyze_corpus('data/pubmed.pkl', 'PubMed',file_type='csv')

# Analyzing the GPT-Neo datasets (assuming they are in .pkl format)
gptneo125m_data, gptneo125m_params = analyze_corpus('data/heapLawData-gptneo125m.pkl', 'GPT-Neo-125m', file_type='pkl')
gptneo13b_data, gptneo13b_params = analyze_corpus('data/heapLawData-gptneo1.3B.pkl', 'GPT-Neo-1.3B', file_type='pkl')
gptneo27b_data, gptneo27b_params = analyze_corpus('data/heapLawData-gptneo2.7B.pkl', 'GPT-Neo-2.7B', file_type='pkl')

# Rest of the code remains the same






def plot_corpus(data, params, corpus_name, ax, log_scale=False):
    if log_scale:
        sns.lineplot(x=np.log10(data['n']), y=np.log10(data['m']), ax=ax, label=f"{corpus_name}: β={params[1]:.4f}")
    else:
        sns.lineplot(x=data['n'], y=data['m'], ax=ax, label=f"{corpus_name}: β={params[1]:.4f}")

# Natural Scale Plot
plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1, 2, 1)
plot_corpus(pubmed_data, pubmed_params, 'PubMed', ax1)
plot_corpus(gptneo125m_data, gptneo125m_params, 'GPT-Neo-125m', ax1)
plot_corpus(gptneo13b_data, gptneo13b_params, 'GPT-Neo-1.3B', ax1)
plot_corpus(gptneo27b_data, gptneo27b_params, 'GPT-Neo-2.7B', ax1)
plt.title("Heaps' Law - Natural Scale")
plt.xlabel('Total Words')
plt.ylabel('Vocabulary Size')
plt.legend()

# Log-Log Scale Plot
ax2 = plt.subplot(1, 2, 2)
plot_corpus(pubmed_data, pubmed_params, 'PubMed', ax2, log_scale=True)
plot_corpus(gptneo125m_data, gptneo125m_params, 'GPT-Neo-125m', ax2, log_scale=True)
plot_corpus(gptneo13b_data, gptneo13b_params, 'GPT-Neo-1.3B', ax2, log_scale=True)
plot_corpus(gptneo27b_data, gptneo27b_params, 'GPT-Neo-2.7B', ax2, log_scale=True)
plt.title("Heaps' Law - Log-Log Scale")
plt.xlabel('Log Total Words')
plt.ylabel('Log Vocabulary Size')
plt.legend()

plt.tight_layout()
# plt.show()



