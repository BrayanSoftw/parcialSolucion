#CONSTANTES DE BONIFICACION POR CARGO Y NIVEL DE DESEMPEÑO
BONIFICACION_DIRECTIVO_ALTO=0.20
BONIFICACION_DIRECTIVO_MEDIO=0.10
BONIFICACION_OPERATIVO_ALTO=0.15
BONIFICACION_OPERATIVO_MEDIO=0.20

#FUNCION PARA CALCULAR LA BONIFICACION SEGUN EL CARGO Y EL NIVEL DE DESEMPEÑO
def calcular_bonificacion(cargo,desempeno,salario_base):
    #DETERMINAR LA ONIFICACION SEGUN EL CARGO Y EL NIVEL DE DESEMPEÑO
    if cargo=="directivo":
        if desempeno=="alto":
            bonificacion=salario_base*BONIFICACION_DIRECTIVO_ALTO
        elif desempeno=="medio":
            bonificacion=salario_base*BONIFICACION_DIRECTIVO_MEDIO
        else:
            bonificacion=0
    elif cargo=="operativo":
        if desempeno=="alto":
            bonificacion=salario_base*BONIFICACION_OPERATIVO_ALTO
        elif desempeno=="medio":
            bonificacion=salario_base*BONIFICACION_OPERATIVO_MEDIO
        else:
            bonificacion=0
    else:
        bonificacion=0

    return bonificacion


#FUNCION PARA CALCULAR EL TOTAL A RECIBIR(SALARIO BASE + BONIFICACION)
def calcular_total(salario_base,bonificacion):
    return salario_base+bonificacion


def imprimir_resumen(cargo,desempeno,salario_base,bonificacion,total):
    print("-------Resumen de pago------")
    print(f"cargo: {cargo.capitalize()}")
    print(f"Nivel de desempeño: {desempeno.capitalize()}")
    print(f"Salario base: {salario_base}")
    print(f"Bonificacion: {bonificacion}")
    print(f"Total a recibir: ${total}")
    print(f"------------------------------")

    #ENTRADAS
salario_base=float(input("Ingrese el salario base mensual: $"))
cargo=input("Ingrese el cargo del empleado (directivo/operativo). ").lower()
desempeno=input("Ingrese el nivel de desempeño (alto/medio/bajo): ").lower()


    #CALCULAR BONIFICACION
bonificacion=calcular_bonificacion(cargo, desempeno, salario_base)

    #CALCULAR TOTAL A RECIBIR
total=calcular_total(salario_base, bonificacion)

    #INVOCAMOS LA FUNCION
imprimir_resumen(cargo, desempeno, salario_base, bonificacion, total)