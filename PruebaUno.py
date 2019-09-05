# Muestra los bytes en texto
# 1 - Abrir el archivo
# 2 - Leer el archivo
# 3 - Imprimir en pantalla
# 4 - Cerrar el archivo 
# move, cp, tail, head, cp con argumentos(args)
NOMBRE = input('Nombre del archivo: ');
#Por defecto lo levanta en modo lectura, es decir, se puede dejar vacio el modo
try:
	var = open(NOMBRE,"r");
	parrafos = var.readlines();
	var2 = open("pepe.txt", "a+");
# Forma uno
	for x in parrafos:
		var2.write(x);

#var2.close();
	var.close();
	var2.seek(0);
	print (var2.read());
	var2.close();

	#ar3 = open("pepe.txt", "r")
	#rint(var3.read())
#ar3.close()
# Forma dos
# print(var.read())
	
except Exception as e:
	print(e)
	print('Errorrrrrr')