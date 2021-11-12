'''
Script para cambiar los elementos de font info
'''

# Guardar la fuente en una variable para hacerla más accesible
fuente = AllFonts()[0] # Otra manera de acceder a la fuente en edición es accediendo al índice 0 de AllFonts()
print(fuente)
# Asignar la info a una variable para hacerla más accesible y manipulable
info = fuente.info
# Revisar los elementos del font info que se pueden modificar
for elemento, valor in info.asDict().items(): # As dict transforma al objeto RInfo() en un diccionario
    print(f'info.{elemento}', '=', valor)
# Elegir 5 y asignar el valor que deseamos
info.familyName = 'Nombre de Familia'
info.styleName = 'Regular'
info.postscriptFontName = f'Nombre-de-Familia-{info.styleName}'
info.versionMajor = 1
info.versionMinor = 0
info.trademark = 'TypeNerd™'
# Reto adicional, añadir año con el módulo datetime
from datetime import datetime
fecha = datetime.now().strftime("%Y") # Tomar la fecha actual del módulo, ayuda en help(datetime)
info.year = int(fecha) # Debe ser número entero
