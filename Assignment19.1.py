
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
train_set =
pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.dat
a', header = None)
test_set =
pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test'
, skiprows = 1, header = None)
col_labels = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
'occupation','relationship', 'race', 'sex', capital_gain', 'capital_loss', 'hours_per_week',
'native_country', 'wage_class']
train_set.columns = col_labels
test_set.columns = col_labels

