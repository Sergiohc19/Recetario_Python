mi_archivo = open('Archivo.txt')



todas = mi_archivo.readlines()


todas = todas.pop()


print(todas)


mi_archivo.close()