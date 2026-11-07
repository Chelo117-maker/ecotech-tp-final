"""Vistas de la app de sustentabilidad."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .services import obtener_metricas_consumo

# Datos de ejemplo. En un sistema real vendrían de la base de datos.
HISTORIAL_CONSUMOS: list[dict] = [
    {"planta": "Planta Norte", "consumo_kwh": 1200.0},
    {"planta": "Planta Sur", "consumo_kwh": 950.5},
    {"planta": "Planta Este", "consumo_kwh": 780.0},
    {"planta": "Planta Norte", "consumo_kwh": 300.0},
]


def vista_panel_sustentabilidad(request: HttpRequest) -> HttpResponse:
    """
    Muestra el panel administrativo de sustentabilidad.

    Procesa el historial de consumos con ``obtener_metricas_consumo`` y arma
    el contexto que se renderiza en ``sustentabilidad/panel.html``.

    Args:
        request: Petición HTTP recibida.

    Returns:
        La respuesta HTTP con la plantilla renderizada.
    """
    metricas: dict = obtener_metricas_consumo(HISTORIAL_CONSUMOS)

    contexto: dict = {
        "titulo": "Panel de Sustentabilidad - EcoTech Solutions",
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "emisiones_por_planta": metricas["emisiones_por_planta"],
    }
    return render(request, "sustentabilidad/panel.html", contexto)