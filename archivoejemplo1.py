archivo = open("archivo.txt")
for i, linea in enumerate(archivo):     
    linea = linea.rstrip("\\n")     
    print " %4d: %s" % (i, linea) 
archivo.close()  
saludo = open("[*saludo.py*](http://saludo.py)", "w") 
saludo.write(""" 
print "Hola Mundo" 
""")
