"""Configuración del proyecto. Es el ÚNICO archivo que deben adaptar a su dataset."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Zonas del data lake
RAW = ROOT / "data" / "raw" / "sentrybox_enaho2025.csv"            # zona raw (bronze): archivo original, nunca se edita
PROCESSED = ROOT / "data" / "processed" / "dataset.csv"  # zona processed (silver): la genera prepare_data.py
RESULTS = ROOT / "results" / "results_summary.csv"       # zona results (gold): la genera run_seeds.py

TARGET = "ganancia_neta_mes"  # nombre de la variable objetivo
TAREA = "regresion"           # "regresion" o "clasificacion"
COLS_NUM = [                  # columnas numéricas que usará el modelo
            "edad",
            "horas_semana",
            "anios_en_ocupacion",
            "personas_en_negocio"
            ]
COLS_CAT = [                  # columnas categóricas que usará el modelo
            "estado_civil",
            "nivel_educativo",
            "registro_sunat",
            "subsector_ciiu",
            "dominio",
            "estrato",
            "mes_encuesta",
            "sexo_mujer",
            "es_empleador",
            "ayuda_familiar_no_remunerado",
            "lleva_libros_contables",
            "tiene_ocupacion_secundaria"
            ]
CODIGOS_FALTANTES = [99, 9999]  # códigos que significan "sin dato" (p. ej., 99, 9999)

MODELO = "arbol"                # el algoritmo asignado: "lineal", "knn", "arbol", "rf" o "svm"

SEMILLA_PARTICION = 42          # fija: todos los integrantes usan la misma partición 80/20
SEMILLAS = [0, 1, 2, 3, 42]     # semillas de la validación cruzada
