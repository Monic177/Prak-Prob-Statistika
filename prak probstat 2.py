#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = [1, 2, -5, 0.3, 6, -2, 4]  # numeric vector
b = ["one", "two", "three"]     # character vector
c = [True, True, True, False, True]  # logical vector
print(a)
print(b)
print(c)


# In[4]:


#MATRIKS
import numpy as np
cells = [3, 15, -27, 38]
r_nama = ["R1", "R2"]
c_nama = ["C1", "C2"]
monic_matrix = np.matrix(cells).reshape(2, 2)
print(monic_matrix)


# In[5]:


import pandas as pd
import numpy as np

monic1 = [1, 2, 3, 4]
monic2 = ["red", "white", "red", np.nan]  # Menggunakan np.nan untuk merepresentasikan NA
monic3 = [True, True, True, False]

data_monic = pd.DataFrame({'ID': monic1, 'Color': monic2, 'Passed': monic3})
print(data_monic)


# In[6]:


import pandas as pd

data_monic = pd.DataFrame({'id': list('abcdefghij'), 'x': list(range(1, 11)), 'y': list(range(11, 21))})
print(data_monic)


# In[8]:


pip install mysql-connector-python


# In[11]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="houseprices1"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM monic_houseprices;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[12]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['Brick'] == 'No']

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[13]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kondisi yang kompleks
df_filtered = df[(df['Brick'] == 'No') | (df['Neighborhood'] == 'East')]

# Menampilkan hasil filter
print(df_filtered)


# In[15]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ps2[monic]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM data_nama_csv;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()


# In[20]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[(df['Gender'] == 'L')]

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[ ]:




