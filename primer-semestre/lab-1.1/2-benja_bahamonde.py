import hello
utiles_escolares = []
utiles_escolares.append("lapiz")
utiles_escolares.append("sacapuntas")
utiles_escolares.append("goma")

hello.world("-------------------------------Utiles Escolares:-------------------------------")
orden = ["Primero","Segundo","Tercero"]

for i in range (len(utiles_escolares)):
    hello.world(f"\n{orden[i]} Útil escolar: {utiles_escolares[i]}")