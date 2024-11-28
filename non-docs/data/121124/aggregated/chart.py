import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# Set the backend to 'Agg' which doesn't require Qt
import matplotlib
matplotlib.use('Agg')

# Data
data = '''Service Name,Input Cost Per Million Tokens,Output Cost Per Million Tokens
Claude 3.5 Sonnet,3,15
Claude 3.5 Haiku,10,50
Claude 3 Opus,15,75
GPT4o,2.50,10.00
gpt-4o-mini,0.150,0.600
o1-preview,15.00,60.00
o1-mini,3.00,12.00
chatgpt-4o-latest,5.00,15.00
gpt-4-turbo,10.00,30.00
gpt-4,30.00,60.00
gpt-4-32k,60.00,120.00'''

# Convert string data to DataFrame
df = pd.read_csv(StringIO(data))

# Reshape data for seaborn
df_melted = df.melt(id_vars=['Service Name'], 
                    var_name='Cost Type', 
                    value_name='Cost (USD)')

# Create the plot
plt.figure(figsize=(15, 8))
sns.barplot(data=df_melted, 
            x='Service Name', 
            y='Cost (USD)', 
            hue='Cost Type',
            palette='Set2')

# Customize the plot
plt.xticks(rotation=45, ha='right')
plt.title('API Costs Comparison: Input vs Output Costs per Million Tokens', 
          pad=20, 
          fontsize=14)
plt.xlabel('Service Name', fontsize=12)
plt.ylabel('Cost in USD per Million Tokens', fontsize=12)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot to chart.png
plt.savefig('chart.png', dpi=300, bbox_inches='tight')
plt.close()