import pandas as pd

datos = pd.read_csv('pandas/datos.csv')
print(datos)

wine_reviews = pd.read_csv("pandas/winemag-data-130k-v2.csv", index_col=0)

print('Reseñas de vinos')
print (wine_reviews.shape)
print (wine_reviews.head())