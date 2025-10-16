inter_wins = 0
gremio_wins = 0
draws = 0
total_grenais = 0

while True:
    inter_score, gremio_score = map(int, input().split())

    if inter_score > gremio_score:
        inter_wins += 1
    elif gremio_score > inter_score:
        gremio_wins += 1
    else:
        draws += 1
    
    total_grenais += 1

    print("Novo grenal (1-sim 2-nao)")
    option = int(input())

    if option == 2:
        break

print(f"{total_grenais} grenais")
print(f"Inter:{inter_wins}")
print(f"Gremio:{gremio_wins}")
print(f"Empates:{draws}")

if inter_wins > gremio_wins:
    print("Inter venceu mais")
elif gremio_wins > inter_wins:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")