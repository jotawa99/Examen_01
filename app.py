import streamlit as st
import pandas as pd


st.title("PROYECTO EXAMEN") # Titulo de la página

#COnfiguración de la barra lateral
st.sidebar.title("Panel de navegación") # Titulo en la barra lateral
opcion=st.sidebar.selectbox("IR A:",("HOME","EJERCICIO 1","EJERCICIO 2","EJERCICIO 3","EJERCICIO 4","RESEÑA"))

# Logica para mostrar contenido según la selección
# Ejecución de la opción "Home"
if opcion=="HOME":
    st.title("*EXAMEN DE PYTHON FUNDAMENTALS - DMC*")
    st.write("**ESTUDIANTE**"+"\u00A0"*27+":José Carlos Lazo choque")
    st.write("**MODULO**"+"\u00A0"*35+":Python Fundamentals")
    st.write("**AÑO**"+"\u00A0"*45+":2026")
    st.write("**OBJETIVO DEL TRABAJO**"+"\u00A0"*3+":El objetivo del trabajo es desarrollar el examen solicitado para la obtención\n" +"\u00A0"*55+"del certificado respectivo")
    st.write("**TECNOLOGIAS UTILIZADAS**"+"\u00A0"*00+": En este codigo se utilizaron las bibilotecas: Pandas, Streamlit.")


# Ejecución de la opción "Ejercicio 1"
if opcion=="EJERCICIO 1":
    st.title("**VARIABLES Y CONDICIONALES**")
    p=st.number_input("Ingrese el presupuesto")
    g=st.number_input("Ingrese el gasto")
    if st.button("EVALUAR"):
       if g<=p:
           st.success("El gasto esta dentro del presupuesto")

       else:
           st.warning("El presupuesto fue excedido")

           
       st.write("Direncia entre presupuesto y gasto es"+ "\u00A0"*2+ f":{p-g} soles")
    


if opcion == "EJERCICIO 2":
    st.title("📊 LISTA Y DICCIONARIOS")

    # Inicializar el estado de la sesión
    if 'actividades' not in st.session_state:
        st.session_state.actividades = []

    # --- SECCIÓN DE INGRESO DE DATOS ---
    with st.expander("➕ Agregar Nueva Actividad", expanded=True):
        nombre = st.text_input("Nombre de la actividad")
        tipo = st.text_input("Tipo de actividad")
        
        col1, col2 = st.columns(2)
        with col1:
            presupuesto = st.number_input("Presupuesto ($)", min_value=0.0, step=10.0)
        with col2:
            gasto_real = st.number_input("Gasto Real ($)", min_value=0.0, step=10.0)

        if st.button("AGREGAR ACTIVIDAD"):
            if nombre:
                actividad = {
                    "Nombre": nombre,
                    "Tipo": tipo,
                    "Presupuesto": presupuesto,
                    "Gasto Real": gasto_real
                }
                st.session_state.actividades.append(actividad)
                st.success(f"✅ '{nombre}' agregada con éxito")
            else:
                st.error("⚠️ El nombre de la actividad es obligatorio")

    # --- VISUALIZACIÓN ---
    if st.session_state.actividades:
        st.write("### 📋 Listado de Actividades")
        st.dataframe(st.session_state.actividades, use_container_width=True)

        # --- ANÁLISIS DE CUMPLIMIENTO ---
        st.write("### ⚖️ Estado de Cumplimiento")
        
        for act in st.session_state.actividades:
            # Cálculo de diferencia
            diferencia = act["Presupuesto"] - act["Gasto Real"]
            
            if act["Gasto Real"] <= act["Presupuesto"]:
                st.success(f"**{act['Nombre']}**: Cumple (Ahorro: ${diferencia:,.2f})")
            else:
                st.error(f"**{act['Nombre']}**: Excedido (Déficit: ${abs(diferencia):,.2f})")
    else:
        st.info("Aún no hay actividades registradas.")



   
if opcion == "EJERCICIO 3":
    st.title("🎯 FUNCIONES Y PROGRAMACIÓN FUNCIONAL")

    if "actividades" in st.session_state and st.session_state.actividades:
        st.write("### Datos base")
        st.dataframe(st.session_state.actividades)

        col1, col2 = st.columns(2)
        with col1:
            t = st.number_input("**Tasa anual (%)**", min_value=0.0, value=5.0)
        with col2:
            m = st.number_input("**Cantidad de meses**", min_value=1, value=12)

        # Definición de la función de cálculo
        def calcular_retorno(actividad, tasa, meses):
            # Fórmula: (Presupuesto * tasa * meses) / (12 meses * 100%)
            retorno = (actividad["Presupuesto"] * tasa * meses) / 1200
            return {
                "Nombre": actividad["Nombre"],
                "Retorno": retorno
            }

        if st.button("EJECUTAR CÁLCULO"):
            # Uso de MAP y LAMBDA para procesar la lista
            resultados = list(map(lambda x: calcular_retorno(x, t, m), st.session_state.actividades))

            st.write("### 📈 Resultados Proyectados")
            for res in resultados:
                st.info(f"**{res['Nombre']}**: Retorno proyectado de **${res['Retorno']:,.2f}**")
    else:
        st.warning("⚠️ No hay actividades registradas en el EJERCICIO 2 para realizar el cálculo.")




if opcion=="EJERCICIO 4":
    st.title("PROGRAMACIÓN ORIENTADA A OBJETOS(POO)")
    # Definicón de la calse actitividad
    class Actividad:
        def __init__(self,nombre,tipo,presupuesto,gasto_real):
            self.nombre=nombre
            self.tipo=tipo
            self.presupuesto=presupuesto
            self.gasto_real=gasto_real
    # Método para validar el presupuesto
        def esta_en_presupuesto(self):
            return self.gasto_real<=self.presupuesto
    
    # Metodo para mostrar información
        def mostrar_info(self):
            return f"Actividad {self.nombre}  | tipo {self.tipo}  | Presupuesto {self.presupuesto}  |  Gasto Real {self.gasto_real}  | "
    
    if st.session_state.actividades:
        for act_data in st.session_state.actividades:
            # Creamos el objeto 'instanciando' la clase con los datos del diccionario
            obj_act = Actividad(
                act_data["Nombre"], 
                act_data["Tipo"], 
                act_data["Presupuesto"], 
                act_data["Gasto Real"]
            )
            
            with st.container():
                st.markdown(obj_act.mostrar_info())
                if obj_act.esta_en_presupuesto():
                    st.success(f"Cumple. Ahorro: ${obj_act.presupuesto - obj_act.gasto_real}")
                else:
                    st.error(f"Excedido por: ${obj_act.gasto_real - obj_act.presupuesto}")
                st.divider()
    else:
        st.error("⚠️ No hay actividades registradas. Ve al EJERCICIO 2 para agregar datos.")
        







if opcion=="RESEÑA":
    st.title("RESEÑA")
    st.write("A continuación la reseña")
