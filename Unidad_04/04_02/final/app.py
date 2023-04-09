primer_nombre = 'rigoberta'
segundo_nombre = 'menchú'
nota = 'Ganadora Premio Novel de la Paz'

primer_nombre_cap = primer_nombre.capitalize()
segundo_nombre_cap = segundo_nombre.capitalize()
award_ubicacion = nota.find('award: ')
award_texto = nota[7:]

print(primer_nombre_cap)
print(segundo_nombre_cap)
print(award_ubicacion)
print(award_texto)