times = ("Botafogo", "Palmeiras", "Fortaleza", "Internacional", "Flamengo", "São Paulo",
          "Cruzeiro", "Bahia", "Corinthians", "Vitória", "Vasco", "Juventude", "Grêmio", "Fluminense",
            "Atlético-MG", "RB Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá")

primeiros = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional")

ultimos = ("Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá")



print(f"Lista de times no brasileirão: {times}\n")
print(f"Os 5 primeiros times são: {primeiros}\n")
print(f"Os 4 ultimos são: {ultimos}\n")
print(f"Os times em ordem alfabetica: {sorted(times)}\n")
print(f"Chapecoense esta na posição : {times.index("Vitória") + 1} \n")
