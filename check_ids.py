from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

datos_1 = pd.read_csv(DATA_DIR / "fichero1.tsv",
                      sep="\t",
                      usecols=["cid", "asin"])
datos_2 = pd.read_csv(DATA_DIR / "fichero2.tsv",
                      sep="\t",
                      usecols=["cid", "asin"])

pairs_1 = {(c, a) for (c, a) in zip(datos_1["cid"], datos_1["asin"])}
pairs_2 = {(c, a) for (c, a) in zip(datos_2["cid"], datos_2["asin"])}
# -------------------------------------------------------------------------------
# Pairs that are not in the two tsv files:
# this is called the symmetric difference of two sets
# ------------------------------------------------------------------------------
print("Pairs that are not in the two tsv files: ")
print("This is called the symmetric difference")
print(pairs_1 ^ pairs_2)  # if these are many, you many not want to print them all

print(
    f"These are {len(pairs_1 ^ pairs_2)} of these out of a total of {len(pairs_1) + len(pairs_2)}, i.e {100 * len(pairs_1 ^ pairs_2)/(len(pairs_1) + len(pairs_2)):.2f}%"
)

clients_1 = {c for c in datos_1["cid"]}
clients_2 = {c for c in datos_2["cid"]}
# -------------------------------------------------------------------------------
# clients that are not in the two tsv files:
# this is called the symmetric difference of two sets
# ------------------------------------------------------------------------------

print("\nClients that are not in the two tsv files: ")
print("This is called the symmetric difference")
print(clients_1
      ^ clients_2)  # if these are many, you many not want to print them all

print(
    f"These are {len(clients_1 ^ clients_2)} of these out of a total of {len(clients_1) + len(clients_2)}, i.e {100 * len(clients_1 ^ clients_2)/(len(clients_1) + len(clients_2)):.2f}%"
)

asin_1 = {c for c in datos_1["asin"]}
asin_2 = {c for c in datos_2["asin"]}
# -------------------------------------------------------------------------------
# asin that are not in the two tsv files:
# this is called the symmetric difference of two sets
# ------------------------------------------------------------------------------

print("\nAsin that are not in the two tsv files: ")
print("This is called the symmetric difference")
print(asin_1
      ^ asin_2)  # if these are many, you many not want to print them all

print(
    f"These are {len(asin_1 ^ asin_2)} of these out of a total of {len(asin_1) + len(asin_2)}, i.e {100 * len(asin_1 ^ asin_2)/(len(asin_1) + len(asin_2)):.2f}%"
)
