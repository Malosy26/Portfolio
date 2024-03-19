import streamlit as st



################################################
def espacio(num):
    if num<0 or num == 1:
        num=2
    for i in range(1,num):
        st.markdown(" ")
################################################
############ DEFINICIONES PARA TITULO SUBTITULO Y TEXTO######################################
def escribeTitulo(titulo,alineacion):
    
    st.write("<span style='display: block; text-align: " +alineacion+"; font-size: 50px; font-weight: bold;'>" + titulo + "</span>", unsafe_allow_html=True)
   

def escribeSubTitulo(subTitulo,alineacion):
    estilo = f"color:cyan; text-align:{alineacion}; font-size:30px; font-weight:bold"
    st.markdown(f"<p style='{estilo}'>{subTitulo}</p>", unsafe_allow_html=True)

def escribeSubSubTitulo(subTitulo,alineacion):
    estilo = f"color:cyan; text-align:{alineacion}; font-size:20px; font-weight:bold"
    st.markdown(f"<p style='{estilo}'>{subTitulo}</p>", unsafe_allow_html=True)



def escribeTexto(texto):
     st.write("<div style='text-align: justify; font-size: 18px;'>" +texto+ "</div>",unsafe_allow_html= True)
    

def escribeTexto2(texto,alineacion):
    estilo = f"text-align:{alineacion}; font-size:18px;"
    st.write(f"<div style='{estilo}'>{texto}</div>", unsafe_allow_html=True)
    
# def escribeTextoTripleComilla(texto):
#         res = """
#                             <div style='text-align: justify;font-size:18px '>
#                             """ + texto 
#         st.markdown(res,unsafe_allow_html=True)
                            

                          

     
################################################################################################
            
