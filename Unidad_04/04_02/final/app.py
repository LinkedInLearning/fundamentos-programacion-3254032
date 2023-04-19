primer_nombre = 'rigoberta'
segundo_nombre = 'menchú'
nota = 'Ganadora Premio Novel de la Paz'

primer_nombre_cap = primer_nombre.capitalize()
segundo_nombre_cap = segundo_nombre.capitalize()
premio_ubicacion = nota.find('Premio')
premio_texto = nota[16:]

print(primer_nombre_cap)
print(segundo_nombre_cap)
print(premio_ubicacion)
print(premio_texto)