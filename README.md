# TP Final · EcoTech Solutions

Trabajo práctico final de Python con tres ejercicios sobre el monitoreo y la gestión de equipamiento sustentable de **EcoTech Solutions**: normalización de datos de sensores, un catálogo de dispositivos con programación orientada a objetos, y un panel web con Django y tests unitarios.

## Contenido

| Ejercicio | Tema | Tecnologías |
|---|---|---|
| **1** | Normalización de lecturas de sensores térmicos y reporte consolidado | Python |
| **2** | Catálogo de dispositivos ecológicos con validación de stock y persistencia en JSON | Python, POO, JSON |
| **3** | Auditoría del cálculo de huella de carbono y panel web de sustentabilidad | Python, `unittest`, Django |

## Estructura del repositorio

```
TP Final/
├── Ejercicio 1/
│   └── Sanitización y Análisis Estadístico de Sensores.py
├── Ejercicio 2/
│   └── Modelo de Productos, Excepciones y Persistencia.py
├── Ejercicio 3/
│   ├── manage.py
│   ├── ecotech_project/          # configuración del proyecto Django
│   └── sustentabilidad/          # app del panel
│       ├── services.py           # lógica de cálculo de emisiones
│       ├── views.py              # vista del panel
│       ├── urls.py
│       ├── tests.py              # pruebas unitarias
│       └── templates/sustentabilidad/panel.html
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.12 o superior (requerido por Django 6)
- Git

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Chelo117-maker/ecotech-tp-final.git
cd ecotech-tp-final

# 2. Crear y activar el entorno virtual
python -m venv tpfinal
tpfinal\Scripts\activate          # Windows
# source tpfinal/bin/activate     # Linux / macOS

# 3. Instalar las dependencias
pip install -r requirements.txt
```

## Ejecución

### Ejercicio 1 · Sensores térmicos

```bash
python "Ejercicio 1/Sanitización y Análisis Estadístico de Sensores.py"
```

Normaliza registros crudos de sensores (ID sin espacios, temperatura numérica, ubicación por defecto), descarta los registros inválidos y muestra un reporte con el promedio térmico y los sensores que superan el umbral de alerta.

### Ejercicio 2 · Catálogo de dispositivos

```bash
python "Ejercicio 2/Modelo de Productos, Excepciones y Persistencia.py"
```

Crea productos ecológicos (incluido un `PanelSolar`), valida que el stock no sea negativo mediante `StockInvalidoError`, imprime las fichas técnicas y exporta el catálogo al archivo `catalogo_ecotech.json`.

### Ejercicio 3 · Panel de sustentabilidad (Django)

```bash
cd "Ejercicio 3"
python manage.py runserver
```

Abrir en el navegador: <http://127.0.0.1:8000/sustentabilidad/panel/>

El panel muestra el total global de emisiones de carbono, la planta de mayor consumo y el detalle de emisiones por planta.

**Tests unitarios** (desde la carpeta `Ejercicio 3`):

```bash
python manage.py test sustentabilidad
```

## Documentación

La descripción detallada de módulos, clases y funciones está en [`docs/documentacion_tecnica.md`](docs/documentacion_tecnica.md).

## Autor

Marcelo E. Guevara · TP Final