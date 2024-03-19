#----------------------Liberias de utilidad y necesarias--------------------------#
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go

#----------------------------------------------------------------------------------#
#-----------------------------Utiles-----------------------------------------------#
from sklearn.model_selection import train_test_split #division del train test
from sklearn.preprocessing import MinMaxScaler # escalador para normalizar os datos
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV # para realizar validacion cruzada
from sklearn.impute import KNNImputer
#----------------------------------------------------------------------------------#
#-------------------------Metricas de Clasificadores-------------------------------#
from sklearn.metrics import jaccard_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score
#----------------------------------------------------------------------------------#
#--------------------------Modelos de clasificacion--------------------------------#
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestCentroid
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
#----------------------------------------------------------------------------------#
#-------------------------------Post-Modelo----------------------------------------#
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
#-----------------------------------------------------------------------------------#


df = pd.read_csv(r'D:\bootcamp\dsb06rt\mod5-machine-learning-y-deep-learning\29_11_2023\credit_risk.csv')



#--------------------------Trabajo de modelo sin los nan-----------------------------#

#Diccionarios para mapear las columnas categoricas
dic_re={'DebtCon':1,'HomeImp':2}
dic_job={'Other':1,'ProfExe':2,'Office':3,'Mgr':4,'Self':5,'Sales':6}
#Hácer un Dammies para las categorias le dara mas precision al modelo oal menos lo entendera mejor
df_no_nan=df.dropna().copy()
df_no_nan['JobEnum']=df_no_nan['JOB'].map(dic_job)
df_no_nan['ReasonEnum']=df_no_nan['REASON'].map(dic_re)
df_no_nan.drop(['REASON','JOB'],axis=1,inplace=True)
model_regularized = RandomForestClassifier(max_depth=12)
X=df_no_nan.drop('BAD',axis=1)
y=df_no_nan['BAD']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42, stratify=y)
model_regularized = RandomForestClassifier(max_depth=12)
model_regularized.fit(X_train, y_train)
yhat = model_regularized.predict(X_test)
y_train_pred_regularized = model_regularized.predict(X_train)
y_test_pred_regularized = model_regularized.predict(X_test)
f1_train_regularized = f1_score(y_train, y_train_pred_regularized, average='macro')
f1_test_regularized = f1_score(y_test, y_test_pred_regularized, average='macro')

def getCorrelacionSinNan():
    corr = df_no_nan._get_numeric_data().corr()  # matriz de correlación

    fig, ax = plt.subplots(figsize=(5, 5))

    mask = np.triu(np.ones_like(corr, dtype=bool))  # máscara para la matriz triangular superior

    # mapa de color coolwarm
    color_map = "coolwarm"

    # mapa de calor de correlación
    sns.heatmap(corr,                      # datos
                mask=mask,                 # máscara blanca
                cmap=color_map,            # color
                vmax=1,                    # borde vertical
                center=0,                  # centro del gráfico
                square=True,               # representación cuadrada de los datos
                linewidth=.5,              # ancho de línea
                cbar_kws={'shrink': .5},   # barra lateral de la leyenda
                annot=True,                # valor de correlación
                fmt=".2f", 
                ax=ax                      # ejes para el tamaño del gráfico
            )

    st.pyplot(fig,use_container_width=False)

def getCorrelacionSinNan2():
    corr = df_no_nan._get_numeric_data().corr()  # matriz de correlación

    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=corr.columns.tolist(),
        y=corr.index.tolist(),
        colorscale=[(0, 'blue'), (0.5, 'lightgray'), (1, 'red')],
        annotation_text=corr.round(2).values,
        showscale=True
    )

    fig.update_layout(
        title="Matriz de correlación",
        xaxis=dict(title="Features"),
        yaxis=dict(title="Features"),
        height=700, width=700
    )

    st.plotly_chart(fig,use_container_width=True)

def features_importances_sin_nan():
    # Calcular la importancia de las características
    feature_importances = model_regularized.feature_importances_
    feature_names = X_train.columns  
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)

    # Crear el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(x=importance_df['Feature'], y=importance_df['Importance'])])
    fig.update_layout(
        title='Importancia de las Características en Random Forest',
        xaxis=dict(title='Características'),
        yaxis=dict(title='Importancia'),
        xaxis_tickangle=-45,
        height=500,
        width=900
    )

    st.plotly_chart(fig,use_container_width=True)



def plot_confusion_matrix():
    cm = confusion_matrix(y_test, yhat, labels=[0, 1])

    # Crear la matriz de confusión con Plotly
    fig = ff.create_annotated_heatmap(
        z=cm,
        x=["Predicted 0", "Predicted 1"],
        y=["Actual 0", "Actual 1"],
        colorscale="Viridis",
        showscale=True
    )

    fig.update_layout(
        title="Matriz de Confusión",
        xaxis=dict(title="Predicted label"),
        yaxis=dict(title="True label"),
        height=500,
        width=500
    )

    st.plotly_chart(fig,use_container_width=True)

def plot_roc_curve():
    # Obtener las probabilidades predichas para la clase positiva
    y_prob = model_regularized.predict_proba(X_test)[:, 1]

    # Calcular la curva ROC
    fpr, tpr, umbrales = roc_curve(y_test, y_prob)

    # Calcular el área bajo la curva ROC (AUC)
    roc_auc = auc(fpr, tpr)

    # Crear un DataFrame para la curva ROC
    roc_df = pd.DataFrame({'FPR': fpr, 'TPR': tpr})

    # Graficar la curva ROC con Plotly Express
    fig = px.line(roc_df, x='FPR', y='TPR', labels={'FPR': 'Tasa de Falsos Positivos', 'TPR': 'Tasa de Verdaderos Positivos'},
                  title=f'Curva ROC (AUC = {roc_auc:.2f})')
    fig.add_scatter(x=[0, 1], y=[0, 1], mode='lines', line=dict(color='navy', width=2, dash='dash'), name='Aleatorio')
    fig.update_layout(showlegend=True, legend=dict(x=0, y=1))
    
    st.plotly_chart(fig,use_container_width=True)

#---------------------------Fin de modelo sin los nan---------------------------------#
#---------------------------Modelo tratando los nan-----------------------------------#
# df2=df.copy()
# df2['JobEnum']=df2['JOB'].map(dic_job)
# df2['ReasonEnum']=df2['REASON'].map(dic_re)
# df2.drop(['REASON','JOB'],axis=1,inplace=True)
# df2 = df2.sort_values(by=['BAD','DEBTINC'])
# df2 = df2.reset_index(drop=True)
# knn_imputer = KNNImputer(metric='nan_euclidean',weights='distance',n_neighbors=5)
# df_imputed = pd.DataFrame(knn_imputer.fit_transform(df2), columns=df2.columns)
# X=df_imputed.drop('BAD', axis=1)
# y=df_imputed.BAD
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42, stratify=y)
# model_regularized = RandomForestClassifier(max_depth=9)
# model_regularized.fit(X_train, y_train)
# yhat = model_regularized.predict(X_test)
# y_train_pred_regularized = model_regularized.predict(X_train)
# y_test_pred_regularized = model_regularized.predict(X_test)
# f1_train_regularized = f1_score(y_train, y_train_pred_regularized, average='macro')
# f1_test_regularized = f1_score(y_test, y_test_pred_regularized, average='macro')


