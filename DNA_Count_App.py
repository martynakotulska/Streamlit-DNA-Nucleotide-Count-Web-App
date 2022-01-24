# import libraries
from asyncore import write
from msilib import sequence
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import numpy as np
import io

#config


#_______________________________Title

# display DNA count app image
img_DNA = Image.open("DNA.png")
st.image(img_DNA)

# title
st.write(""" # DNA Nucleotide Count Web App
This app count the nucleotide composition of query DNA
***
""")

#_______________________________Input Tex Box
st.header('Enter DNA sequence')

sequence_input = ">Keratyna 5, egzon 2, Homo sapiens 2\nGTGCGGTTCCTGGAGCAGCAGAACAAGGTTCTGGACACCAAGTGGACCCTGCTGCAGGAGCAGGGCACCAAGACTGTGAGGCAGAACCTGGAGCCGTTGTTCGAGCAGTACATCAACAACCTCAGGAGGCAGCTGGACAGCATCGTGGGGGAACGGGGCCGCCTGGACTCAGAGCTGAGAAACATGCAGGACCTGGTGGAAGACTTCAAGAACAA"

sequence = st.text_area("Sequence input", sequence_input, height = 200)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence)

st.write(""" 
***
""")

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

#____ 1. Print Dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    result = dict([
        ('A', seq.count('A')),
        ('C', seq.count('C')),
        ('G', seq.count('G')),
        ('T', seq.count('T'))
    ])
    return result

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

#____ 2. Print text
st.subheader('2. Print text')
st.write('There are ' + str(X['A'])+ ' adenine (A)')
st.write('There are ' + str(X['T'])+ ' thymine (T)')
st.write('There are ' + str(X['C'])+ ' guanine (C)')
st.write('There are ' + str(X['G'])+ ' cytosine (G)')

#____ 3. Display Data Frame
st.subheader('3. Display dataframe')
df = pd.DataFrame.from_dict(X,orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

#____ 4. Display Bar Chart
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)
