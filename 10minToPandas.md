#Apprendre Pandas en 10 minutes
Basé sur  [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
##Importations

    import numpy as np
    import pandas as pd
    
##Création d'objets
###Objet  *Series* 

    In[1]: s = pd.Series([1, 3, 5, np.nan, 6, 8])
    
    In[2]: s
    
    Out[2]:
    0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64


###Objet Dataframe

- **En passant un NumPy Array**

    - Création du Array

            In[3]: dates = pd.date_range('20130101', periods=6)
            
            In[4]: dates
            
            Out[4]: 
            DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
    - Création du DataFrame ***.DataFrame()***

            In[5]: df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
            
            Out[5]: 
                               A         B         C         D
            2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
            2013-01-02  1.212112 -0.173215  0.119209 -1.044236
            2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
            2013-01-04  0.721555 -0.706771 -1.039575  0.271860
            2013-01-05 -0.424972  0.567020  0.276232 -1.087401
            2013-01-06 -0.673690  0.113648 -1.478427  0.524988

- **En passant un dictionnaire**
    - Création du DataFrame ***.DataFrame()***
    
            In[6]: df2 = pd.DataFrame({'A': 1.,
               ...:                     'B': pd.Timestamp('20130102'),
               ...:                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
               ...:                     'D': np.array([3] * 4, dtype='int32'),
               ...:                     'E': pd.Categorical(["test", "train", "test", "train"]),
               ...:                     'F': 'foo'})
               ...: 
             
            In[7]: df2 
            
            Out[7]:
                 A          B    C  D      E    F
            0  1.0 2013-01-02  1.0  3   test  foo
            1  1.0 2013-01-02  1.0  3  train  foo
            2  1.0 2013-01-02  1.0  3   test  foo
            3  1.0 2013-01-02  1.0  3  train  foo 

- **Visualisation des types des colonnes ***.dtype*****
        
            In[8]: df2.dtypes
            
            Out[8]:
            A           float64
            B    datetime64[ns]
            C           float32
            D             int32
            E          category
            F            object
            dtype: object 

##Visualisation des données

- **Afficher le haut ou le bas du DataFrame**
    - Top ***.head()***

            In[9]: df.head()
            
            Out[9]: 
                               A         B         C         D
            2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
            2013-01-02  1.212112 -0.173215  0.119209 -1.044236
            2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
            2013-01-04  0.721555 -0.706771 -1.039575  0.271860
            2013-01-05 -0.424972  0.567020  0.276232 -1.087401
    - Bottom ***.tail()***
            
            In[10]: df.tail(3)
            
            Out[10]: 
                               A         B         C         D
            2013-01-04  0.721555 -0.706771 -1.039575  0.271860
            2013-01-05 -0.424972  0.567020  0.276232 -1.087401
            2013-01-06 -0.673690  0.113648 -1.478427  0.524988
- **Afficher les indices et les colonnes**
    - Indices ***.index***
    
            In[11]: df.index
            
            Out[11]: 
            DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                           '2013-01-05', '2013-01-06'],
                          dtype='datetime64[ns]', freq='D')
    - Colonnes ***.columns***
        
            In [12]: df.columns
            
            Out[12]: Index(['A', 'B', 'C', 'D'], dtype='object')
- **Afficher des informations statistiques sur les colonnes ***describe()*****

        In[13]: df.describe()
        
        Out[13]: 
                      A         B         C         D
        count  6.000000  6.000000  6.000000  6.000000 # nombre d'éléments
        mean   0.073711 -0.431125 -0.687758 -0.233103 # moyenne
        std    0.843157  0.922818  0.779887  0.973118 # écart-type
        min   -0.861849 -2.104569 -1.509059 -1.135632 # minimum
        25%   -0.611510 -0.600794 -1.368714 -1.076610 # 1er quartile
        50%    0.022070 -0.228039 -0.767252 -0.386188 # médiane
        75%    0.658444  0.041933 -0.034326  0.461706 # 3eme quartile
        max    1.212112  0.567020  0.276232  1.071804 # maximum
        
- **Transposer les données ***.T*****
        
        In [14]: df.T
        
        Out[14]: 
           2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
        A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
        B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
        C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
        D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
      
- **Organiser par axe ***.sort_index()*****

        In[15]: df.sort_index(axis=1, ascending=False)
        
        Out[15]: 
                           D         C         B         A
        2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
        2013-01-02 -1.044236  0.119209 -0.173215  1.212112
        2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
        2013-01-04  0.271860 -1.039575 -0.706771  0.721555
        2013-01-05 -1.087401  0.276232  0.567020 -0.424972
        2013-01-06  0.524988 -1.478427  0.113648 -0.673690
        
- **Organiser par valeur ***.sort_values()*****

        In[16]: df.sort_values(by='B')
        
        Out[16]: 
                           A         B         C         D
        2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
        2013-01-04  0.721555 -0.706771 -1.039575  0.271860
        2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
        2013-01-02  1.212112 -0.173215  0.119209 -1.044236
        2013-01-06 -0.673690  0.113648 -1.478427  0.524988
        2013-01-05 -0.424972  0.567020  0.276232 -1.087401
        
##Sélection

- **Sélection par colonne**

    - Récuperation d'une colonne complète ***[]*** 
    
            In[17]: df['A']
            
            Out[17]: 
            2013-01-01    0.469112
            2013-01-02    1.212112
            2013-01-03   -0.861849
            2013-01-04    0.721555
            2013-01-05   -0.424972
            2013-01-06   -0.673690
            Freq: D, Name: A, dtype: float64
            
    - Récuperation d'un DataFrame tronqué ***[:]*** 
    
            In[18]: df[0:3] #par l'indice des lignes
            
            Out[18]: 
                               A         B         C         D
            2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
            2013-01-02  1.212112 -0.173215  0.119209 -1.044236
            2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
            
            In[18]: df['20130102':'20130104'] #par le nom des lignes
            
            Out[18]: 
                               A         B         C         D
            2013-01-02  1.212112 -0.173215  0.119209 -1.044236
            2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
            2013-01-04  0.721555 -0.706771 -1.039575  0.271860
- **Sélection par label**

    - Label simple ***.loc[[]]***
    
            In[19]: df.loc[dates[0]] #par l'indice des colonnes
            
            Out[19]: 
            A    0.469112
            B   -0.282863
            C   -1.509059
            D   -1.135632
            Name: 2013-01-01 00:00:00, dtype: float64
    - Multi-axes par label ***.loc[:,[,]]***
        
            In[20]: df.loc[:, ['A', 'B']]
            
            Out[20]: 
                               A         B
            2013-01-01  0.469112 -0.282863
            2013-01-02  1.212112 -0.173215
            2013-01-03 -0.861849 -2.104569
            2013-01-04  0.721555 -0.706771
            2013-01-05 -0.424972  0.567020
            2013-01-06 -0.673690  0.113648
            
    - Multi-axes par label avec points extrêmes définis***.loc[:,[,]]***
    
            In[21]: df.loc['20130102':'20130104', ['A', 'B']]
            
            Out[21]: 
                               A         B
            2013-01-02  1.212112 -0.173215
            2013-01-03 -0.861849 -2.104569
            2013-01-04  0.721555 -0.706771
           
    