from claseViajeroFrecuente2 import ViajeroFrecuente

if __name__== '__main__':
 viajero1 = ViajeroFrecuente(123, '12345678', 'Juan', 'Perez', 10000)
 viajero2 = ViajeroFrecuente(456, '87654321', 'Maria', 'Garcia', 15000)
 viajero3 = ViajeroFrecuente(789, '11111111', 'Pedro', 'Lopez', 5000)
 lista_viajeros = [viajero1, viajero2, viajero3]
 viajero_con_mas_millas = max(lista_viajeros)
 print(f"El/los viajero/s con mayor cantidad de millas acumuladas es/son: {viajero_con_mas_millas.nombre} {viajero_con_mas_millas.apellido}")
 viajero = ViajeroFrecuente(123, '12345678', 'Juan', 'Perez', 10000)
 viajero = viajero + 500
 print(f"Las nuevas millas acumuladas son: {viajero.millas}")
 viajero = ViajeroFrecuente(123, '12345678', 'Juan', 'Perez', 10000)
 viajero = viajero - 500
 print(f"Las nuevas millas acumuladas son: {viajero.millas}")