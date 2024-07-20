import matplotlib.pyplot as plt
from io import BytesIO
import base64
from crewai import Agent, Engine

class TextToChartAgent(Agent):
    def __init__(self):
        super().__init__()

    def respond(self, message):
        try:
            data = self.parse_message(message)
            if data:
                chart_url = self.generate_chart(data)
                return f"Here is your chart: ![chart]({chart_url})"
            else:
                return "I couldn't understand the data format. Please provide data in the format: 'label1:value1, label2:value2, ...'"
        except Exception as e:
            return f"An error occurred: {e}"

    def parse_message(self, message):
        try:
            data = {}
            pairs = message.split(',')
            for pair in pairs:
                label, value = pair.split(':')
                data[label.strip()] = float(value.strip())
            return data
        except Exception as e:
            print(f"Error parsing message: {e}")
            return None

    def generate_chart(self, data):
        labels = list(data.keys())
        values = list(data.values())

        fig, ax = plt.subplots()
        ax.bar(labels, values)

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        chart_data = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)

        chart_url = f"data:image/png;base64,{chart_data}"
        return chart_url

if __name__ == "__main__":
    engine = Engine()
    agent = TextToChartAgent()
    engine.register(agent)
    engine.run()
