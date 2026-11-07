"""Pruebas unitarias del algoritmo de emisiones de carbono."""

import unittest

from .services import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):
    """Valida la exactitud del cálculo y el manejo de consumos inválidos."""

    def test_calculo_con_factor_por_defecto(self):
        """100 kWh con el factor por defecto (0.4) deben dar 40."""
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_calculo_con_factor_personalizado(self):
        """250 kWh con factor 0.5 deben dar 125."""
        self.assertAlmostEqual(calcular_emisiones_carbono(250, 0.5), 125.0)

    def test_calculo_con_decimales(self):
        """Un consumo decimal se calcula correctamente."""
        self.assertAlmostEqual(calcular_emisiones_carbono(12.5), 5.0)

    def test_consumo_cero(self):
        """Un consumo de 0 es válido y produce 0 emisiones."""
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo_lanza_error(self):
        """Un consumo negativo debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)

    def test_consumo_negativo_con_factor_personalizado(self):
        """El error también debe saltar si se usa un factor distinto."""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1, factor_emision=0.8)


if __name__ == "__main__":
    unittest.main()