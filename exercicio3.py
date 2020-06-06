segundos_str = input("informe o numero de segundos que voce queira converter")
total_segs = int(segundos_str)

dias = total_segs // 86400
hora = total_segs // 3600
horas_total = hora % 24
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print("resto horas ")
print(dias,"dias,",horas_total,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")
