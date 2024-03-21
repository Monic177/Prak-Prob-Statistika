#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data_monic = pd.read_clipboard()
# Menampilkan data
print(data_monic)


# In[2]:


monic = data_monic[data_monic['Tinggi'] == 165]
print(monic)


# In[3]:


monic['Tinggi'] = pd.to_numeric(monic['Tinggi'])

import numpy as np
monic['Tinggi'] = monic['Tinggi'].apply(lambda x: 'tinggi' if x > 160 else 'pendek')

# Menampilkan DataFrame setelah modifikasi
print(monic)


# In[4]:


import numpy as np

monic['Jurusan'] = 'Infor20'
monic['Fakultas'] = 'FTI'

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(monic)


# In[5]:


monic = monic.drop(columns=['Fakultas'])

# Menampilkan DataFrame 'nama'
print(monic)


# In[6]:


kolom1dan2 = data_monic.iloc[:, 0:2]

# Menampilkan DataFrame kolom1dan2
print(kolom1dan2)

# Memilih kolom 1 dan 2 dari DataFrame data_nama
kolom3dan4 = data_monic.iloc[:, 2:4]

# Menampilkan DataFrame kolom3dan4
print(kolom3dan4)

# Menggabungkan dua DataFrame
kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4],axis=1)

# Menampilkan DataFrame kolom1sd4
print(kolom1sd4)


# In[7]:


kolom1dan2 = data_monic.iloc[:, 0:2]

# Menampilkan DataFrame kolom1dan2
print(kolom1dan2)


# In[8]:


# Memilih kolom 1 dan 2 dari DataFrame data_nama
kolom3dan4 = data_monic.iloc[:, 2:4]

# Menampilkan DataFrame kolom3dan4
print(kolom3dan4)


# In[9]:


# Menggabungkan dua DataFrame
kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4],axis=1)

# Menampilkan DataFrame kolom1sd4
print(kolom1sd4)


# In[10]:


# Import pandas library
import pandas as pd

# Menggabungkan baris dari dua DataFrame
baris1sd5 = data_monic.iloc[0:5, :]
baris25sd30 = data_monic.iloc[24:31, :]
baris1sd5dan25sd30 = pd.concat([baris1sd5, baris25sd30])

# Menampilkan DataFrame baris1sd6
print(baris1sd5dan25sd30)


# In[11]:


data_monic_sort = data_monic.sort_values(by='Waktu Perjalan')

print(data_monic_sort)


# In[ ]:




