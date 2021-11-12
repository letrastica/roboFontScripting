'''
Script para monoespaciar los caracteres seleccionados
'''
# Es útil tener al inicio del código las fuentes que podrá cambiar el usuario
ancho = 700 

# Guardar la fuente en una variable para hacerla más accesible
fuente = CurrentFont() # Acceder al objeto RFont en uso
# Guardar los glifos que se quieren monoespaciar en una variable (útil para números tabulares)
glifos = ['zero','one','two','three','four','five','six','seven','eight','nine']
# Revisar cada glifo guardado
for glifo in glifos:
    glifo = fuente[glifo] # Acceder al objeto RGlyph
    # Ajustar su anchura al valor deseado
    glifo.width = ancho
    # Como reto pcional serìa centrar el glifo
    # Encontrar la mitad del total del área en los márgenes
    margen = (glifo.leftMargin + glifo.rightMargin) // 2 # Divide y arroja números enteros
    # Otros métodos para hacer un número entero
    import math
    decimal = 5.3
    print(int(decimal), round(decimal), math.floor(decimal), math.ceil(decimal))
    # Asignar valor de margen a márgenes
    glifo.leftMargin, glifo.rightMargin = margen, margen
    # Asignar valor de ancho en caso de algún desfase
    glifo.width = ancho
