class Procesamiento:
    def __init__(self):
        self.evaluaciones = []

    def ingresar_evaluaciones(self):
        
        while True:
            try:
                puntos = int(input("Ingrese los puntos de evaluación (1-5): "))
                if puntos < 1 or puntos > 5:
                    print("Ingrese un valor de 1 a 5.")
                    continue
                comentario = input("Ingrese un comentario: ")
                self.evaluaciones.append((puntos, comentario))
                continuar = input("¿Desea ingresar más evaluaciones? (S/N): ")
                if continuar.lower() != 's':
                    break
            except ValueError:
                print("Ingrese un valor numérico válido.")

    def comprobar_resultados(self):
        if not self.evaluaciones:
            print("No hay evaluaciones ingresadas.")
        else:
            print("Evaluaciones ingresadas:")
            for i, (puntos, comentario) in enumerate(self.evaluaciones, start=1):
                print(f"Evaluación {i}: Puntos: {puntos}, Comentario: {comentario}")

    def procesar(self):
        while True:
            proceso = input("Seleccione el proceso a realizar (1-3) o '0' para terminar: ")
            if proceso == '0':
                break
            elif proceso not in ['1', '2', '3']:
                print("Por favor ingrese 1 a 3.")
                continue
            elif proceso == '1':
                self.ingresar_evaluaciones()
            elif proceso == '2':
                self.comprobar_resultados()
            elif proceso == '3':
                # Agrega aquí el código para el proceso 3
                print("Proceso 3 ejecutado.")

if __name__ == "__main__":
    procesamiento = Procesamiento()
    procesamiento.procesar()



