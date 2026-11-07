def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4) -> float:
    """
    Calcula las emisiones de carbono asociadas a un consumo eléctrico.

    Args:
        consumo_kwh: Consumo de energía en kWh. No puede ser negativo.
        factor_emision: Kg de CO2 emitidos por cada kWh (por defecto 0.4).

    Returns:
        Las emisiones de carbono (consumo_kwh * factor_emision).

    Raises:
        ValueError: Si el consumo es negativo.
    """
    if consumo_kwh < 0:
        raise ValueError(f"El consumo no puede ser negativo: {consumo_kwh}")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros: list[dict]) -> dict:
    """
    Procesa el historial de consumos de las plantas industriales.

    Cada registro tiene la forma ``{"planta": "Planta Norte", "consumo_kwh": 1200.0}``.
    Una misma planta puede aparecer varias veces; sus consumos se suman.

    Args:
        registros: Lista de registros de consumo.

    Returns:
        Diccionario con:
            - ``total_emisiones``: emisiones globales de todas las plantas.
            - ``planta_mayor_consumo``: nombre de la planta con más consumo
              (``None`` si no hay registros).
            - ``emisiones_por_planta``: emisiones acumuladas de cada planta.

    Raises:
        ValueError: Si algún registro tiene un consumo negativo.
    """
    consumo_por_planta: dict[str, float] = {}
    emisiones_por_planta: dict[str, float] = {}

    for registro in registros:
        planta: str = registro["planta"]
        consumo: float = registro["consumo_kwh"]
        emisiones: float = calcular_emisiones_carbono(consumo)

        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0.0) + consumo
        emisiones_por_planta[planta] = emisiones_por_planta.get(planta, 0.0) + emisiones

    planta_mayor_consumo = None
    if consumo_por_planta:
        planta_mayor_consumo = max(consumo_por_planta, key=consumo_por_planta.get)

    return {
        "total_emisiones": sum(emisiones_por_planta.values()),
        "planta_mayor_consumo": planta_mayor_consumo,
        "emisiones_por_planta": emisiones_por_planta,
    }