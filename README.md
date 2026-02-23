# 📊 PROYECTO EXAMEN – Python Fundamentals

Aplicación web desarrollada con **Python** y **Streamlit** como evaluación final del módulo *Python Fundamentals*.

El proyecto integra conceptos fundamentales del lenguaje organizados en ejercicios prácticos dentro de una sola aplicación interactiva.

---

## 👨‍🎓 Información del Proyecto

- **Estudiante:** José Carlos Lazo Choque  
- **Módulo:** Python Fundamentals  
- **Año:** 2026  
- **Tipo:** Proyecto de evaluación  

---

## 🚀 Tecnologías Utilizadas

- Python 3
- Streamlit
- Pandas

---

## 🧩 Estructura del Proyecto

La aplicación está dividida en 6 secciones accesibles desde el panel lateral:

```
HOME
EJERCICIO 1
EJERCICIO 2
EJERCICIO 3
EJERCICIO 4
RESEÑA
```

---

# 📌 Descripción de los Ejercicios

## 🏠 HOME
Muestra información general del examen:
- Datos del estudiante
- Objetivo del trabajo
- Tecnologías utilizadas

---

## 📊 EJERCICIO 1 – Variables y Condicionales

Se ingresan:
- Presupuesto
- Gasto

El sistema evalúa si:
- ✅ El gasto está dentro del presupuesto
- ⚠️ El presupuesto fue excedido

También calcula la diferencia entre ambos valores.

Conceptos aplicados:
- Variables
- Condicionales (`if - else`)
- Operaciones matemáticas

---

## 📊 EJERCICIO 2 – Listas y Diccionarios

Permite:
- Registrar actividades
- Guardarlas en `st.session_state`
- Mostrar los datos en un `dataframe`
- Evaluar cumplimiento de presupuesto

Estructura de datos utilizada:

```python
actividad = {
    "Nombre": nombre,
    "Tipo": tipo,
    "Presupuesto": presupuesto,
    "Gasto Real": gasto_real
}
```

Conceptos aplicados:
- Listas
- Diccionarios
- Session State
- Bucles `for`

---

## 📊 EJERCICIO 3 – Funciones y Programación Funcional

Se define una función:

```python
def calcular_retorno(actividad, tasa, meses):
```

Se utilizan:
- Funciones personalizadas
- `map()`
- `lambda`
- Cálculo financiero simple

Se proyecta el retorno en función de:
- Tasa anual (%)
- Cantidad de meses

Conceptos aplicados:
- Funciones
- Programación funcional
- Expresiones lambda

---

## 📊 EJERCICIO 4 – Programación Orientada a Objetos (POO)

Se define la clase:

```python
class Actividad:
```

### 🔹 Atributos
- nombre
- tipo
- presupuesto
- gasto_real

### 🔹 Métodos
- `esta_en_presupuesto()`
- `mostrar_info()`

Se instancian objetos a partir de los diccionarios guardados en el ejercicio 2.

Conceptos aplicados:
- Clases
- Objetos
- Métodos
- Encapsulamiento

---

## 🎯 RESEÑA

Breve reflexión personal sobre el aprendizaje de Python y la experiencia desarrollando el proyecto.

---

# ▶️ Cómo Ejecutar el Proyecto

1. Instalar dependencias:

```bash
pip install streamlit pandas
```

2. Ejecutar la aplicación:

```bash
streamlit run app.py
```

3. Se abrirá automáticamente en el navegador.

---

# 📚 Objetivo Académico

Este proyecto demuestra la aplicación práctica de:

- Variables
- Condicionales
- Listas
- Diccionarios
- Funciones
- Programación funcional
- Programación Orientada a Objetos
- Desarrollo de aplicaciones web con Streamlit

---

# 🏁 Conclusión

El proyecto integra los fundamentos de Python en una aplicación interactiva, demostrando comprensión de los principales paradigmas de programación vistos en el módulo.

---

© 2026 – Proyecto académico
