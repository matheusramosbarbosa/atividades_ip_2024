#dia no mine tem 24000 ticks, 20 min da vida real
#tantan só tem 3h por dia pra construir casas
#tantan tem medo de construir a noite
#tantan então só vai construir nos primeiros 12 mil ticks do dia
#ele tem "ao todo" 216.000 ticks pra construir, mas já que ele tem medo de construir à noite, então ele só tem 108.000 ticks pra construir por dia
#tantan quer saber quantos ticks demoraria pra construir cada casa

dia_ticks_mine = 24000 #esse dia dura 20 minutos da vida real
tempo_livre = 3 * 60 #3 horas transformadas em minutos
dia_mine_real = 20 #quanto dura um dia no mine na vida real
qtd_dias_mine = tempo_livre // dia_mine_real #quantos dias do mine ele tem por dia
ticks_por_dia =  dia_ticks_mine * qtd_dias_mine #quatidade de ticks presentes em um dia no mine vezes quantidade de dias de mine que ele tem disponível por dia, resultando na quantidade de ticks que ele tem disponível no dia
dia_ticks_produtivo = ticks_por_dia // 2 #quantos ticks ele tem disponível por dia, pois ele só constrói de dia

d = int(input())
c = int(input())

total_ticks = dia_ticks_produtivo * d #ticks por dia vezes a quantidade de dias
t = total_ticks // c #total de ticks por casa

print(f'{t}')

#eu quis complicar mais a situação, mas se eu quisesse eu já poderia dizer qual a quantidade de ticks por dia sem ter que fazer todas essas contas
