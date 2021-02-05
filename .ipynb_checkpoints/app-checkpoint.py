import streamlit as st
import pandas as pd
import altair as alt
from vega_datasets import data
import numpy as np


def app():
    
    st.title("Let's demo Streamlit basics")
    
    st.sidebar.markdown("**Some tools we'll use:**")
    st.sidebar.markdown("""
        * Markdown
        * Pandas
        * Altair""")
    
    
    st.markdown("""## Markdown and Pandas
I am writing Markdown but I can also show a pandas DataFrame.
  """)
    
    df_cars = data.cars()
    st.write(df_cars.head())
    
    
    st.markdown("""## Altair
And I can easily make interactive altair plots.
  """)
    
    brush = alt.selection_interval(encodings=['x', 'y'])
    repeat_chart = alt.Chart(df_cars).mark_point().encode(
    alt.X(alt.repeat('column'), type='quantitative'),
    alt.Y('Miles_per_Gallon:Q'),
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray')),
    opacity=alt.condition(brush, alt.value(0.7), alt.value(0.1))
).properties(
    width=150,
    height=150
).add_selection(
    brush           
).repeat(
    column=['Weight_in_lbs', 'Acceleration', 'Horsepower']
)

    st.write(repeat_chart)
    
    st.markdown("""## User Input
I can create a text input field to get input from the user.
  """)
    
    n = int(st.text_input("How many points do you want plotted:", '100'))
        
    x = np.random.random(n) * 10
    y = np.random.random(n) * 10
    s = np.random.random(n)
    
    df = pd.DataFrame({'x':x, 'y':y, 'size': s})
    
    chart = alt.Chart(df, width=400,
                      height=400).mark_point().encode(
                x='x',
                y='y',
                size=alt.Size('size', legend=None),
                tooltip=['size']
    ).interactive()

    st.write(chart)
    
if __name__ == '__main__':
    app()