all : Servidor Cliente

# Coloca aqui el path donde te hayas descargado y compilado la mini-librería de sockets
PATH_CHSOCKET=/home/arelyvp/Escritorio/prac/Socket/libreria

CFLAGS = -g -I. -I$(PATH_CHSOCKET)

Servidor : Servidor.o
	cc Servidor.o -L$(PATH_CHSOCKET) -lChSocket -o Servidor

Cliente : Cliente.o
	cc Cliente.o -L$(PATH_CHSOCKET) -lChSocket -o Cliente

clean :
	rm *.o Cliente Servidor
