import streamlit as st
from scipy.stats import geom
from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt

st.title("Multi Mass Function Plot/Visualisation: ")

plotName = st.radio("Choose the plot type: ",["Geometric plot","Binomial plot","Poisson plot"])

nTrials = st.number_input("Enter the number of trials performed: ",min_value=2, max_value=1000, value=10)
x = range(1,nTrials+1)
if plotName == "Geometric plot":
    probSuc = st.number_input("Enter the probability of success: ",min_value=0.01, max_value=1.0, value=0.3)
    pmf = geom.pmf(x,probSuc)
elif plotName == "Poisson plot":
    mu = st.number_input("Enter the value of lambda: ",min_value=0.01,max_value = 100.0,value=3.0)
    pmf = poisson.pmf(x,mu)
else:
    probSuc = st.number_input("Enter the probability of success: ",min_value=0.01, max_value=1.0, value=0.3)
    pmf = binom.pmf(x,nTrials,probSuc)


fig, ax = plt.subplots()
if plotName == "Geometric plot":
    ax.stem(x, pmf)
    ax.set_title(f"Geometric PMF with p = {probSuc} for {nTrials} trials")
elif plotName == "Binomial plot":
    ax.bar(x, pmf)
    ax.set_title(f"Binomial PMF with p = {probSuc} for {nTrials} trials")
else:
    ax.stem(x,pmf)
    ax.set_title(f"Poisson PMF with lambda = {mu} for {nTrials} trials")
ax.set_xlabel("Number of trials to success")
ax.set_ylabel("Probability")
ax.grid()

st.pyplot(fig)