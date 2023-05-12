# Función decorativa
def banner(seccion):
    print('*'*10+seccion+'*'*10)
    
# Mediante esta función volcaremos los datos de los archivos CSV
def dump_csv_data(file, title):
    # Abrimos el archivo
    users_file = open(file,'r', encoding = 'utf-8')
    # Leemos las líneas del archivo
    data = users_file.readlines()
    # Cerramos el archivo para liberar recursos
    users_file.close()
    # Pasamos la primera línea del CSV a una lista aparte, para manejarlo después
    fields = data[0].strip().split(';')
    # Eliminamos la primera línea,q eu contiene los nombres de campo, para dejar sólo los datos de usuario
    data.pop(0)
    # Llamamos a la función decorativa
    banner(title)
    # Mediante un bucle for, imprimimos los datos de cada usuario, concatenamos con los nombres de campo que previamente mandamos a una lista aparte
    for user in data:
        user = user.strip().split(';')
        i = 0
        for i in range(len(user)):
            print (f'{fields[i]}: {user[i]}')
            i += 1
        print('\n')

# Abrimos los archivos CSV mediante la función
dump_csv_data('users.csv','Nuestros usuarios')
dump_csv_data('admins.csv','El equipo de administradores')