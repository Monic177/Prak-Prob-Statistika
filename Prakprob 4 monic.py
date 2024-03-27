#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

# Fungsi untuk menghitung kombinasi (n choose k)
def n_choose_k(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

# Fungsi untuk menghitung probabilitas P(X=k) dalam distribusi binomial
def binomial_probability(n, k, p):
    return n_choose_k(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Parameter distribusi binomial
n = 10 # jumlah percobaan
p = 0.5 # probabilitas keberhasilan dalam satu percobaan
k = 3 # jumlah keberhasilan yang diinginkan

# Menghitung probabilitas P(X=k) untuk distribusi binomial
prob_binomial = binomial_probability(n, k, p)
print("Probabilitas P(X=k) untuk distribusi binomial:", prob_binomial)


# In[4]:


from scipy.stats import binom

# Distribusi Binomial
n = 10 # jumlah percobaan
p = 0.5 # probabilitas keberhasilan dalam satu percobaan
k = 3 # jumlah keberhasilan yang diinginkan

prob_binomial = binom.pmf(k, n, p)
print("Probabilitas P(X=k) untuk distribusi binomial:", prob_binomial)


# In[5]:


import math

# Fungsi untuk menghitung probabilitas P(X=k) dalam distribusi Poisson
def poisson_probability(lambd, k):
    return (lambd ** k) * math.exp(-lambd) / math.factorial(k)

# Parameter distribusi Poisson
lambd = 3 # rata-rata jumlah peristiwa dalam interval waktu/titik
k = 2 # jumlah peristiwa yang diinginkan

# Menghitung probabilitas P(X=k) untuk distribusi Poisson
prob_poisson = poisson_probability(lambd, k)
print("Probabilitas P(X=k) untuk distribusi Poisson:", prob_poisson)


# In[6]:


from scipy.stats import poisson

# Distribusi Poisson
lambd = 3 # rata-rata jumlah peristiwa dalam interval waktu/titik
k = 2 # jumlah peristiwa yang diinginkan 

prob_poisson = poisson.pmf(k, lambd)
print("Probabilitas P(X=k) untuk distribusi Poisson:", prob_poisson)


# In[7]:


from scipy import stats
X = stats.binom(15, 0.1)
print(X.pmf(3))           # P(X = 3)


# In[8]:


print(X.cdf(2))          # P(X <= 2)


# In[9]:


print(X.pmf(6)+X.pmf(7))


# In[10]:


from scipy import stats
Y = stats.poisson(5)
print(Y.pmf(4))       # P(Y = 4)


# In[11]:


from scipy import stats

# Mendefinisikan variabel X sebagai distribusi binomial dengan 15 percobaan dan probabilitas sukses 0.1
X = stats.binom(20, 0.7)

# Menghitung probabilitas massa X sama dengan 3
pmf_15 = X.pmf(15)

# Mencetak nilai probabilitas
print(pmf_15)


# In[12]:


from scipy import stats
Y = stats.poisson(2)

print(Y.pmf(3))       # \(P(Y=3)\)


# In[13]:


from scipy import stats

X = stats.binom(15, 0.3)
print(X.pmf(5))      # P(X = 5)


# In[ ]:




