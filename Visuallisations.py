import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 15, 8, 12, 20],
    'Percentage': [20, 30, 16, 24, 40]
}

df = pd.DataFrame(data)

def bar_chart(df):
    fig = px.bar(df, x='Category', y='Values', title='Bar Chart Example')
    fig.show()

def pie_chart(df):
    fig = px.pie(df, values='Percentage', names='Category', title='Pie Chart Example')
    fig.show()

def scatter_plot(df):
    fig = px.scatter(df, x='Values', y='Percentage', color='Category', size='Values', title='Scatter Plot Example')
    fig.show()

def main():
    print("Generating...")
    bar_chart(df)
    pie_chart(df)
    scatter_plot(df)
    print("Visualizations generated!")
    
pio.renderers.default = "browser"
main()