import ipaddress

# Abrir el archivo de entrada
with open('prueba2.txt', 'r') as archivo_entrada:

    # Abrir el archivo de salida
    with open('salida.txt', 'w') as archivo_salida:

        # Procesar cada línea del archivo de entrada
        for linea in archivo_entrada:
            
            # Eliminar el carácter de salto de línea al final de la línea
            linea = linea.rstrip('\n')
            
            # Dividir la línea en campos separados por comas
            campos = linea.split(',')
            
            # Convertir la parte de la dirección IP a decimal
            ip_decimal = str(ipaddress.IPv6Address(campos[0].split('/')[0])).replace(':', ',')
            
            # Eliminar la parte con la expresión regular
            ip_decimal = ip_decimal.split(',')[:-1]
            
            # Obtener el nombre del segundo campo
            nombre = campos[2]
            
            # Convertir la dirección IP a hexadecimal y agregarla a los campos
            ip_hexadecimal = '.'.join('{:02X}'.format(int(octeto)) for octeto in campos[5].split('.'))
            
            # Escribir los campos en el archivo de salida
            archivo_salida.write(nombre + ',' + ','.join(ip_decimal) + ',' + ip_hexadecimal + '\n')
