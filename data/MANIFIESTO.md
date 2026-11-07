# Manifiesto de datos

| Campo | Valor |
| :--- | :--- |
| Nombre del archivo en `data/raw/` | `sentrybox_enaho2025.csv` |
| Fuente (institución) | INEI (ENAHO 2025 Módulo 500) |
| URL exacta de descarga | https://proyectos.inei.gob.pe/microdatos/ |
| Fecha de descarga | 2026-10-31 |
| Licencia o condiciones de uso | Datos abiertos del Estado peruano para uso académico y estadístico |
| ¿Se permite redistribuir? | Sí |
| Filas × columnas (raw) | 4765 filas × 18 columnas |
| MD5 del archivo raw | 79cb9c9fcccd760795c3a28fdc8b35e3 |
| MD5 del archivo processed | f2a07a276a13ca7f0272aa8d8004b2df |

## Diccionario de las variables usadas

| Variable | Tipo | Descripción | Unidad / categorías |
| :--- | :--- | :--- | :--- |
| `ganancia_neta_mes` | Objetivo | Ganancia neta mensual de la ocupación principal | Soles (P530A) |
| `edad` | Numérica | Años cumplidos del encuestado | Años (P208A) |
| `horas_semana` | Numérica | Horas trabajadas la semana pasada | Horas (P513T) |
| `anios_en_ocupacion` | Numérica | Tiempo en la ocupación principal | Años (P513A1 + P513A2/12) |
| `personas_en_negocio` | Numérica | Personas que trabajan en el negocio | Conteo personas (P512B) |
| `sexo_mujer` | Categórica | Indicador de sexo femenino | 0: Hombre, 1: Mujer (P207) |
| `estado_civil` | Categórica | Estado civil del encuestado | Categorías ENAHO (P209) |
| `nivel_educativo` | Categórica | Último nivel educativo aprobado | Categorías ENAHO (P301A) |
| `es_empleador` | Categórica | Indicador de condición de empleador | Categorías ENAHO (P507) |
| `ayuda_familiar_no_remunerado` | Categórica | Ayuda de familiares sin pago fijo | Categorías ENAHO (P508) |
| `registro_sunat` | Categórica | Condición de registro en SUNAT | Jurídica / Natural RUC / Sin RUC |
| `lleva_libros_contables` | Categórica | Indicador de libros/sistema contable | Categorías ENAHO (P510B) |
| `tiene_ocupacion_secundaria` | Categórica | Indicador de ocupación secundaria | Categorías ENAHO (P514) |
| `subsector_ciiu` | Categórica | Actividad económica CIIU Rev. 4 | Códigos 4700-4799 |
| `dominio` | Categórica | Dominio geográfico | Definido por INEI |
| `estrato` | Categórica | Estrato geográfico | Definido por INEI |
| `mes_encuesta` | Categórica | Mes de realización de la encuesta | Meses del año |

## Transformaciones de raw a processed
1. Se quitaron espacios al inicio y final en los nombres de columnas.
2. Se verificó la ausencia de filas duplicadas exactas.
3. Se conservaron las 4 765 observaciones correspondientes a microcomerciantes con ganancia reportada.
4. Se excluyó la variable `tiene_trabajadores_pagados` por colinealidad exacta con `es_empleador`.
5. Se mantuvo el valor nulo de `nivel_educativo` para ser imputado dentro del Pipeline de Scikit-learn.