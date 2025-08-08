h1, m1, h2, m2 = map(int, input().split())

start_minute = h1 * 60 + m1
end_minute = h2 * 60 + m2

if start_minute < end_minute:
    duration = end_minute - start_minute
elif start_minute > end_minute:
    duration = (24 * 60 - start_minute) + end_minute
else:
    duration = 24 * 60

hours = duration // 60
minutes = duration % 60

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")