
"""
EcoTech Solutions - Monitoreo térmico de sensores.

Los microcontroladores de EcoTech Solutions transmiten 
lecturas térmicas en formato heterogéneo con espacios indeseados, 
textos mezclados con unidades de medida y atributos incompletos. 
Se necesita un componente que normalice estos registros individuales 
y genere un reporte consolidado para la toma de decisiones.

"""
#Punto A: limpiar_registro_sensor  -> normaliza un registro crudo.

def limpiar_registro_sensor(registro_raw: dict[str,str]):
    """
    Normaliza un registro crudo de un sensor.

    Args:
        registro_raw: Diccionario con datos crudos, por ejemplo
            {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C",
            "ubicacion": "Planta Norte"}.

    Returns:
        Un nuevo diccionario con 'sensor_id' (str), 'temperatura' (float)
        y 'ubicacion' (str). Si no hay ubicación, usa "Desconocida".

    Raises:
        ValueError: Si falta el sensor_id o la temperatura no es válida.
    """
    # 1) ID sin espacios
    sensor_id: str = str(registro_raw.get("sensor_id", "")).strip()
    if sensor_id == "":
        raise ValueError("falta el sensor_id")

    # 2) Temperatura: me quedo solo con dígitos, punto, coma y signo menos
    texto: str = str(registro_raw.get("temperatura", ""))
    numero: str = ""
    for caracter in texto:
        if caracter in "0123456789.,-":
            numero = numero + caracter
    try:
        temperatura: float = float(numero.replace(",", "."))
    except ValueError:
        raise ValueError(f"temperatura inválida en {sensor_id}: {texto!r}")

    # 3) Ubicación con valor por defecto
    ubicacion = registro_raw.get("ubicacion")
    if ubicacion is None or str(ubicacion).strip() == "":
        ubicacion = "Desconocida"
    else:
        ubicacion = str(ubicacion).strip()

    return {"sensor_id": sensor_id, "temperatura": temperatura, "ubicacion": ubicacion}

#Punto B: generar_resumen_sensores -> detecta alertas y calcula el promedio.

def generar_resumen_sensores(
    lista_sensores_limpios: list[dict], umbral_temperatura: float
) -> tuple[list[str], float]:
    """
    Genera el resumen de monitoreo de la planta.

    Args:
        lista_sensores_limpios: Registros ya procesados con
            limpiar_registro_sensor.
        umbral_temperatura: Límite térmico. Los sensores con temperatura
            mayor a este valor entran en alerta.

    Returns:
        Tupla (lista_sensores_alerta, promedio_temperatura):
            - lista_sensores_alerta: IDs de los sensores que superan el umbral.
            - promedio_temperatura: promedio global (0.0 si no hay registros).
    """
    if len(lista_sensores_limpios) == 0:
        return [], 0.0

    lista_sensores_alerta: list[str] = []
    suma_temperaturas: float = 0.0

    for sensor in lista_sensores_limpios:
        suma_temperaturas += sensor["temperatura"]
        if sensor["temperatura"] > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura: float = suma_temperaturas / len(lista_sensores_limpios)
    return lista_sensores_alerta, promedio_temperatura


"""Flujo completo: limpieza -> resumen -> reporte impreso."""
registros_crudos: list[dict] = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": " 31.2 °C ", "ubicacion": "  Planta Sur "},
        {"sensor_id": "  SENSOR-003", "temperatura": "28,7C"},
        {"sensor_id": "SENSOR-004 ", "temperatura": "35.0C", "ubicacion": ""},
        {"sensor_id": "SENSOR-005", "temperatura": "error", "ubicacion": "Planta Este"},
        {"sensor_id": "SENSOR-006", "temperatura": "22C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-007 ", "temperatura": "0 C", "ubicacion": ""},
    ]
umbral: float = 30.0

sensores_limpios: list[dict] = []
for registro in registros_crudos:
    try:
            sensores_limpios.append(limpiar_registro_sensor(registro))
    except ValueError as error:
            print(f"[ADVERTENCIA] Registro descartado: {error}")

alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral)

print("\n=== REPORTE TÉRMICO - ECOTECH SOLUTIONS ===")
print(f"Registros válidos: {len(sensores_limpios)} de {len(registros_crudos)}")
print(f"Umbral de alerta : {umbral:.1f} °C")
print(f"Promedio global  : {promedio:.2f} °C")
print("-" * 43)
for sensor in sensores_limpios:
        estado = "ALERTA" if sensor["sensor_id"] in alertas else "OK"
        print(f"{sensor['sensor_id']:<12} {sensor['temperatura']:>5.1f} °C  "
              f"{sensor['ubicacion']:<14} {estado}")
print("-" * 43)
print(f"Sensores en alerta: {', '.join(alertas) if alertas else 'ninguno'}")
