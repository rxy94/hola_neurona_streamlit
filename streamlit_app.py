import streamlit as st

st.image("./img/redes-neuronales.jpg")
st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.subheader("Una neurona con una entrada y un peso")
    
    w = st.slider("Peso", 0.0, 5.0)
    x = st.number_input("Introduzca el valor de la entrada")

    if st.button("Calcular la salida", key="tab1"):
        y = w * x
        st.write(f"La salida de la neurona es {y}")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        w0 = st.slider("Peso $w_0$", 0.0, 5.0, key="w0_t2")
        x0 = st.number_input("Entrada $x_0$", key="x0_t2")

    with col2:
        w1 = st.slider("Peso $w_1$", 0.0, 5.0, key="w1_t2")
        x1 = st.number_input("Entrada $x_1$", key="x1_t2")

    if st.button("Calcular la salida", key="tab2"):
            y_t2 = w0 * x0 + w1 * x1
            st.write(f"La salida de la neurona es {y_t2}")

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso $w_0$", 0.0, 5.0, key="w0_t3")
        x0 = st.number_input("Entrada $x_0$", key="x0_t3")

    with col2:
        w1 = st.slider("Peso $w_1$", 0.0, 5.0, key="w1_t3")
        x1 = st.number_input("Entrada $x_1$", key="x1_t3")
    with col3:
        w2 = st.slider("Peso $w_2$", 0.0, 5.0, key="w2_t3")
        x2 = st.number_input("Entrada $x_2$", key="x2_t3")
    
    sesgo = st.number_input("Introduzca el valor del sesgo", key="sesgo_t3")

    if st.button("Calcular la salida", key="tab3"):
        y_t3 = w0 * x0 + w1 * x1 + w2 * x2 + sesgo
        st.write(f"La salida de la neurona es {y_t3}")