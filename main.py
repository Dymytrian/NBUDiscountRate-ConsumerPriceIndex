import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load data from KursPrice.xlsx file
data = pd.read_excel('KursPrice.xlsx')

# Calculate Pearson's correlation coefficient
r, p_value = stats.pearsonr(data['NBU interest rate'], data['Consumer price indices'])

# Test the significance of the relationship
if p_value < 0.05:
    print(f'The correlation between the interest rate and the consumer price index is significant (r = {r:.2f}, p-value = {p_value:.4f})')
else:
    print(f'The correlation between the interest rate and the consumer price index is not significant (r = {r:.2f}, p-value = {p_value:.4f})')

# Calculate the coefficients of the linear regression equation
slope, intercept, r_value, p_value, std_err = stats.linregress(data['NBU interest rate'], data['Consumer price indices'])
print(f'Linear regression equation: y = {intercept:.2f} + {slope:.2f}x')
# Plot the linear regression
plt.scatter(data['NBU interest rate'], data['Consumer price indices'])
plt.plot(data['NBU interest rate'], intercept + slope * data['NBU interest rate'], 'r')
plt.xlabel('Interest Rate')
plt.ylabel('Consumer Price Index')
plt.show()