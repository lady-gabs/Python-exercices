seg_str = input ("Por favor, insira o número de segundos que deseja converter: ")
total_seg = int (seg_str)

a = total_seg // 86400
seg_rest = total_seg % 86400
b = seg_rest // 3600
segs_rest = seg_rest % 3600
c = segs_rest // 60
d = segs_rest % 60

print (a, "dias,",b,"horas,",c,"minutos e",d,"segundos")
