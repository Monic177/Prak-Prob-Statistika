#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data_monic = pd.read_clipboard()
# Menampilkan data
print(data_monic)


# In[2]:


monic = data_monic[data_monic['Bedrooms'] == 2]

# Menampilkan nama
print(monic)


# In[3]:


monic['Bathrooms'] = pd.to_numeric(monic['Bathrooms'])

import numpy as np

monic['Bathrooms'] = monic['Bathrooms'].apply(lambda x: 'large' if x > 2 else 'small')

# Menampilkan DataFrame setelah modifikasi
print(monic)


# In[4]:


import numpy as np

monic['newvariable'] = np.where(monic['Offers'] > 2, 'large', 'small')

# Menampilkan DataFrame 'monic' setelah penambahan kolom baru
print(monic)


# In[5]:


# Menambahkan kolom baru 'newvariable' 
monic['newvariable'] = monic['Price'] / monic['SqFt']

# Menampilkan DataFrame 'monic' setelah penambahan kolom baru
print(monic)


# In[6]:


monic = monic.drop(columns=['newvariable'])

# Menampilkan DataFrame 'monic' 
print(monic)


# In[7]:


kolom1dan2 = data_monic.iloc[:, 0:2]

# Menampilkan DataFrame kolom1dan2
print(kolom1dan2)


# In[8]:


# Memilih kolom 1 dan 2 dari DataFrame data_monic
kolom3dan4 = data_monic.iloc[:, 2:4]

# Menampilkan DataFrame kolom3dan4
print(kolom3dan4)


# In[9]:


# Menggabungkan dua DataFrame 
kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4], axis=1)

# Menampilkan DataFrame kolom1sd4
print(kolom1sd4)


# In[10]:


#import pandas library
import pandas as pd

# Menggabungkan baris dari dua DataFrame
baris1sd3 = data_monic.iloc[0:3, :]
baris4sd6 = data_monic.iloc[3:6, :]
baris1sd6 = pd.concat([baris1sd3, baris4sd6])

# Menampilkan DataFrame baris1sd6
print(baris1sd6)


# In[11]:


data_monic_sort = data_monic.sort_values(by='Price')

print(data_monic_sort)


# In[12]:


data_nama = pd.read_csv("PrakStatistika\data_nama.csv")
print(data_nama)


# In[13]:


monic = data_nama['Tinggi']

# Menampilkan nama
print(monic)


# In[15]:


monic['Tinggi'] = pd.to_numeric(monic['Tinggi'])

import numpy as np

monic['Tinggi'] = monic['Tinggi'].apply(lambda x: 'tinggi' if x > 160 else 'pendek')

# Menampilkan DataFrame setelah modifikasi
print(monic)


# In[16]:


import numpy as np

monic['Jurusan'] = 'Infor20'
monic['Fakultas'] = 'FTI'

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(monic)


# In[ ]:




