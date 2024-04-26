# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("Proyecto de Ciencias")
st.write('Hola *Enrique* **como** estás! :sunglasses:')
st.write('Gastos:')
st.write(pd.DataFrame({
    'casa':['Alimentos'],
    'monto':[350],
    }))