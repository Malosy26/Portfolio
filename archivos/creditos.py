import streamlit as st
from funciones.funciones import *
import pandas as pd
from funciones.funcionesCreditos import *

df = pd.read_csv(r'D:\bootcamp\dsb06rt\mod5-machine-learning-y-deep-learning\29_11_2023\credit_risk.csv')





def mostrar_creditos():
    escribeTitulo("Ejercicio de Machine Learning Créditos",'center')
    escribeTexto("En este caso le expondremos un caso de un modelo supervisado utilizando clasificación ,los diferentes problemas a los que nos enfrentamos y la resolucion elegida.")
    espacio(3)
    col1,col2 = st.columns(2)
    with col1:
        escribeSubTitulo("DataFrame",'center')
        st.dataframe(df, height= 550)
    with col2:
        escribeSubTitulo("Contexto",'center')
        texto = """
<div style='text-align: justify;font-size:18px;'>
    <p><strong>BAD:</strong> 1 = candidato con préstamo incumplido o con mora; 0 = candidato que paga su deuda y no tiene registro negativo</p>
    <p><strong>LOAN:</strong> Cantidad de solicitud de préstamo</p>
    <p><strong>MORTDUE:</strong> Cantidad adeudada de la hipoteca existente</p>
    <p><strong>VALUE:</strong> Valor actual del bien o propiedad</p>
    <p><strong>REASON:</strong> DebtCon = consolidación de la deuda; HomeImp = mejoras para el hogar</p>
    <p><strong>JOB:</strong> Categorías ocupacionales o profesionales</p>
    <p><strong>YOJ:</strong> Años en su trabajo actual</p>
    <p><strong>DEROG:</strong> Número de informes derogados o cancelados importantes</p>
    <p><strong>DELINQ:</strong> Número de líneas de crédito morosas</p>
    <p><strong>CLAGE:</strong> Antigüedad de la línea de crédito más antigua en meses</p>
    <p><strong>NINQ:</strong> Número de consultas crediticias recientes</p>
    <p><strong>CLNO:</strong> Número de líneas de crédito</p>
    <p><strong>DEBTINC:</strong> Cantidad de los ingresos que se dedica a pagar créditos en porcentaje</p>
</div>
"""

        st.markdown(texto, unsafe_allow_html=True)
    espacio(3)
    escribeSubTitulo("EDA",'center')
    espacio(2)
    escribeTexto2("Este ejercicio lo vamos a intentar resolver en 2 ramas :",'center')
    espacio(2)
    col3,col4 = st.columns(2)

    with col3:
        escribeSubTitulo("Evaluación del modelo sin los nan",'center')
        escribeTexto2("Para este caso evaluaremos el obviar todos los nan de los datos.",'center')
        escribeTexto2('El df con los nan tiene 5960 filas mientras que sin nan tiene 3364','center')
        escribeTexto2('Observamos una pérdida importante de información. Debido a ello evaluaremos los dos modelos','center')
    with col4:
        escribeSubTitulo("Evaluación del modelo tratando los nan", 'center')
        escribeTexto2("En la mayoría de modelos este sería el paso a seguir tratar los nan.",'center')
        escribeTexto2("Pero en este caso concreto los nan se tratan con una estimación la cual puede ser más o menos acertada.",'center')
        escribeTexto2("En su apartado correspondiente explicaremos a que se debe que esta estimación lleve un riesgo.",'center')
    espacio(3)
    escribeSubTitulo("Resultados 1 parte Evaluación de modelo sin los nan",'center')
    escribeTexto2("En primer lugar haremos un resumén de EDA realizado para información mas tecnica en mis redes gitlab o github tienen el notebook con todas la operaciones.",'center')
    espacio(2)
    col5,col6 = st.columns(2)
    with col5:
        escribeTexto("1- Se limpian todos los nan eliminandolos de los datos.")
        escribeTexto("3- Se observa la correlación entre los datos.")
    with col6:
        escribeTexto("2- Se realiza mapeado las columnas REASON y JOB.")
        escribeTexto("4- Se elige la variable objetivo en este caso BAD.")
    espacio(5)
    escribeTexto2("Mostramos resultados de la correlación: ",'center')
    espacio(1)
    getCorrelacionSinNan2()
    espacio(1)
    escribeTexto("Cabe destacar que entre VALUE y MORTDUE hay una correlación alta.")

    espacio(5)
    escribeTexto("A continuación se realizo una prueba con todos los modelos de clasificación siendo el ganador RandomForest.")
    escribeTexto("Se realizan varias pruebas y se observan sus métricas las cuales expongo :")
    espacio(2)
    col7,col8 = st.columns(2)
    with col7:
        texto = """
    <div style='text-align: justify; font-size:18px'>
    ------------------------------------------------------------------<br>
    MODELO NORMALIZADO CON STRATIFY EN Y<br>
    Jaccard Index: 0.7448257930317213<br>
    Exactitud: 0.9583952451708767<br>
    Precisión: 0.9781591263650546<br>
    Sensibilidad: 0.7666666666666666<br>
    F1-score: 0.8366618126343527<br>
    ROC AUC: 0.7666666666666666<br>
    ------------------------------------------------------------------<br>
    MODELO NORMALIZADO SIN STRATIFY EN Y<br>
    Jaccard Index: 0.7476394134636748<br>
    Exactitud: 0.9613670133729569<br>
    Precisión: 0.9644005627575118<br>
    Sensibilidad: 0.7719182112385996<br>
    F1-score: 0.8385197489848653<br>
    ROC AUC: 0.7719182112385996<br>
     ------------------------------------------------------------------<br>
    </div>
   
    """

        st.markdown(texto, unsafe_allow_html=True)
    with col8:
            
            texto = """
    <div style='text-align: justify; font-size:18px'>
    ------------------------------------------------------------------<br>
    MODELO SIN NORMALIZADO CON STRATIFY EN Y<br>
    Jaccard Index: 0.735747663551402<br>
    Exactitud: 0.9569093610698366<br>
    Precisión: 0.9774143302180686<br>
    Sensibilidad: 0.7583333333333333<br>
    F1-score: 0.8440645676183611<br>
    ROC AUC: 0.7583333333333333<br>
    ------------------------------------------------------------------<br>
    MODELO SIN NORMALIZADO CON STRATIFY EN Y<br>
    Jaccard Index: 0.7379658385093169<br>
    Exactitud: 0.9598811292719168<br>
    Precisión: 0.9631156039398652<br>
    Sensibilidad: 0.7628273021476905<br>
    F1-score: 0.8304706815319307<br>
    ROC AUC: 0.7628273021476906<br>
    ------------------------------------------------------------------<br>
    </div>
    """

            st.markdown(texto, unsafe_allow_html=True)
    espacio(3)
    escribeTexto("El modelo ganador  basandonos en la métrica F1-score es el modelo sin normalizar con stratify en Y, ahora primer paso que damos es el visualizar que el modelo no memoriza al completo el conjunto de datos de entrenamiento:")
    espacio(2)
    texto = """
    <div style='text-align: justify; font-size:18px'>
    F1-score en Conjunto de Entrenamiento: 1.0<br>
    F1-score en Conjunto de Prueba: 0.8366618126343527
    </div>
   
    """
    st.markdown(texto, unsafe_allow_html=True)
    espacio(1)
    escribeTexto("Se observa que si, se ha memorizado al completo el conjunto de entrenamiento por lo que probaremos a disminuir el parámetro de profundidad del modelo.")
    espacio(2)
    texto = """
    <div style='text-align: justify; font-size:18px'>
    F1-score en Conjunto de Entrenamiento con el parámetro max_depth = 11:  0.8826906699460741<br>
    F1-score en Conjunto de Prueba con el parámetro max_depth=11: 0.7777295371684618
    </div>
   
    """
    st.markdown(texto, unsafe_allow_html=True)
    espacio(1)
    escribeTexto("Estas métricas fueron obtenidas tras pruebas realizando un bucle y guardando los datos quedándonos con la que tenia menor diferencia entre los conjuntos pero mayor presición.")
    espacio(3)
    escribeSubTitulo("Feature importances","center")
    escribeTexto2("Ahora comprobaremos la importancia de las columnas evaluadas para saber cuáles aportan más información al modelo:",'center')
    espacio(1)
    features_importances_sin_nan()
    espacio(1)
    escribeTexto('Comprobamos que el modelo le da a DEBTINC la mayor importancia con diferencia.')
    espacio(2)
    escribeSubTitulo("Matriz de confusión:", 'center')
    escribeTexto2("Vamos a comprobar con la matriz de confusión como predice el modelo los datos:",'center')
    espacio(1)
    plot_confusion_matrix()
    espacio(2)
    escribeTexto("En resumen, el modelo tiene una alta precisión y un recall decente. La mayoría de los clientes que pagan la deuda fueron identificados correctamente, pero hubo algunos casos donde el modelo predijo incorrectamente que no pagarían la deuda. La exactitud general del modelo y el F1-score son bastante altos, lo que sugiere un buen rendimiento en la predicción de la clase 0 un BAD = 0 es que el cliente paga la deuda.")
    espacio(2)
    escribeSubTitulo("Curva ROC",'center')
    espacio(1)
    plot_roc_curve()
    espacio(3)
    escribeSubTitulo("Resultado 2 Modelo con tratamiento a los nan","center")
    espacio(2)
    escribeTexto2("Ahora para no alargar tanto el contenido vamos a comentar como se tratan los nan y expondré los resultados.",'center')
    espacio(2)
    escribeTexto("El primer paso diferente que en el caso anterior es ordenar los datos primero por la columna BAD(objetivo) y después por DEBTINC.")
    escribeTexto("Este paso se da gracias al conocimiento de la features importances del modelo sin los nan y por que nos conviene tenerlos ordenados para el tratamiento que vamos a realizar de los nan.")
    espacio(1)
    escribeTexto("Una vez ordenados procederemos ha realizar las medias de los vecinos con KNNimputer cuyos parámetros son:")
    escribeTexto("metric='nan_euclidean',weights='distance',n_neighbors=5")
    espacio(1)
    escribeTexto("Ahora entrenamos el modelo que tiene todo el conjunto de datos al completo y obtenemos este resultado:")
    escribeTexto("F1-score en Conjunto de Entrenamiento con (max_depth = 9) = 0.8252834557487514")
    escribeTexto("F1-score en Conjunto de Prueba con (max_depth=9) = 0.7599596113156386")
    espacio(4)
    escribeSubTitulo("Conclusiones",'center')
    espacio(3)
    

   
    # Define el texto con el tamaño de fuente de 18px para cada línea
    texto = """
    <div style='font-size: 18px;'>
    Conclusión del ejercicio: Desde que comencé este ejercicio, siempre tuve la duda y el objetivo de determinar si para este caso sería mejor estimar los datos y trabajar con más información o si sería preferible omitir los datos desconocidos y construir un modelo basado únicamente en datos reales.
    </div><br>
    <div style='font-size: 18px;'>
    Modelo con datos reales:
    </div><br>
    <div style='font-size: 18px;'>
    Ventajas: No hay ninguna estimación en el punto de corte, ya que utilizamos datos reales con toda la información disponible. La información obtenida de las predicciones trata de  un acierto real sin necesidad de estimaciones.
    </div><br>
    <div style='font-size: 18px;'>
    Desventajas: No creo que haya manera de mejorar significativamente los resultados, ya que estas métricas son aproximadamente las mejores que podemos obtener.
    </div><br>
    <div style='font-size: 18px;'>
    Modelo con datos estimados (transformación de los NaN):
    </div><br>
    <div style='font-size: 18px;'>
    Ventajas: El modelo tiene más información para identificar patrones, lo que puede resultar en una mayor precisión en la obtención de datos. La distancia entre la precisión en el grupo de Train y el de Test es menor.
    </div><br>
    <div style='font-size: 18px;'>
    Desventajas: La ESTIMACIÓN; el 100% de la precisión de este modelo depende de dicha estimación. Tras evaluar varias estimaciones, he considerado la mejor aquella que he usado con el orden de DEBTINC y las medias de los nulos del vecino superior e inferior. Aunque el modelo mostraba solo correlación entre MORDUE y VALUE, la fórmula del DEBTINC lleva implícitos MORDUE y LOAN, además de los INCOMES, pero no podemos obtener este último.
    </div><br>
    <div style='font-size: 18px;'>
    Además también he tenido en cuenta que en el modelo anterior al sacar las features importances DEBTINC era la que tenía un mayor peso.
    </div><br>
    <div style='font-size: 18px;'>
    Conclusión final: Para trabajar con modelos de clasificación, la importancia de si vas a tratar los NaN o no depende de tu capacidad para realizar la estimación. En este ejercicio, opté por presentar ambos modelos y sugerir la prueba con nuevos datos para evaluar la precisión de las predicciones. Aunque el segundo modelo pueda tener un rendimiento superior, los patrones que identifica se basan en estimaciones del usuario. Aunque el mundo ideal donde conocemos todos los datos no exista en la realidad, mi objetivo en el aprendizaje automático es lograr que mi modelo se asemeje lo más posible a ese mundo ideal y tenga el menor margen de error posible.
    </div>
    """

    # Imprime el texto con el tamaño de fuente de 18px para cada línea
    st.markdown(texto, unsafe_allow_html=True)




