# JupyterLab Code Editor Demonstration

#########################
# 1. Inline Documentation
#########################

# Click on factors and press Control to see a list of
# available pipeline factors
from zipline.pipeline.factors import AverageDollarVolume

# click on AverageDollarVolume and press Control to see 
# its docstring
avg_dollar_volume = AverageDollarVolume(window_length=30)

##################
# 2. Auto-complete
##################

# The following line uses the top() method to select the 
# top 10 stocks by dollar volume
most_actives = avg_dollar_volume.top(10)

# to demonstrate auto-complete, finish the following line 
# as shown below:

# least_actives = avg_dollar_volume.bottom(10)
least_actives = 

######################
# 3. Diagnostics Panel
######################

# The following line contains an error; right-click 
# on any text in the editor and click Show Diagnostics Panel 
# to see a list of all detected errors (Note: the Diagnostics 
# Panel is also available in notebooks)
pct_change = opens.pct_change()
