productos = ["pepsi 1L","fanta 1L", "coca 1L", "papa", "zanahoria", "tu mama"]
precios = (    1500,      1750,      2000,     150,      175,       999999)
cantidad = [5, 10, 2, 26, 15, 1]

for i in range(len(productos)):
    print(f"\n {productos[i]}: {precios[i]}$ stock: {cantidad[i]}")



