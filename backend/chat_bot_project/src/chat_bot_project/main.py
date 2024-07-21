from crewai import CrewAI
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def generate_chart(data, chart_type):
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 6))

    if chart_type == 'bar':
        sns.barplot(x=df.columns[0], y=df.columns[1], data=df)
    elif chart_type == 'line':
        sns.lineplot(x=df.columns[0], y=df.columns[1], data=df)
    # Add more chart types as needed

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    return img_base64

def handle_user_input(user_input):
    # Process the user input and convert it to a database query
    # Example: "Show me the sales data for the last month as a bar chart"
    chart_type = 'bar'  # Extract the chart type from the user input
    data = { 'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [100, 150, 200] }  # Sample data
    
    chart = generate_chart(data, chart_type)
    return chart

if __name__ == "__main__":
    crew_ai = CrewAI()
    user_input = "Show me the sales data for the last month as a bar chart"
    result = handle_user_input(user_input)
    print(result)
