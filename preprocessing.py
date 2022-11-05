import pandas as pd
import numpy as np

import pycountry_convert as pc


path_dataset = "Dataset.xlsx"
df1 = pd.read_excel(path_dataset, sheet_name="country_codes")
df2 = pd.read_excel(path_dataset, sheet_name="Energy_Related")

for index, row in df1.iterrows():
    df2.Exporter.replace(row["country_code"], row["iso_3digit_alpha"], inplace=True)
    df2.Importer.replace(row["country_code"], row["iso_3digit_alpha"], inplace=True)

products = {271600: "Eng", 270900: "Oil", 271111: "GNL", 271121: "GAS", 270400: "Coal"}

for code in products.keys():
    df2.Product.replace(code, products[code], inplace=True)

df2["ContinentExporter"]=df2["Exporter"]
df2["ContinentImporter"]=df2["Importer"]

for index, row in df2.iterrows():
    df2.ContinentExporter.replace(row["ContinentExporter"], pc.country_alpha2_to_continent_code(pc.country_alpha3_to_country_alpha2(str(row["ContinentExporter"]))), inplace=True)
    df2.ContinentImporter.replace(row["ContinentImporter"], pc.country_alpha2_to_continent_code(pc.country_alpha3_to_country_alpha2(str(row["ContinentImporter"]))), inplace=True)

df2.to_excel("DatasetWithCountries.xlsx", index=False)