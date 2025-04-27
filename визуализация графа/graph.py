#%%
import pandas as pd
import dash
from dash import dcc, html
import dash_cytoscape as cyto


df = pd.read_excel("graph_connections.xlsx")

# Проверка структуры данных
print(df.head())  # Это поможет увидеть, как выглядят ваши данные
# Преобразование данных в формат для Cytoscape
elements = []
for index, row in df.iterrows():
    vertex1 = str(row['vertex 1'])  # Приведение к строке
    vertex2 = str(row['vertex 2'])  # Приведение к строке

    # Добавляем узлы, если они еще не добавлены
    if {'data': {'id': vertex1}} not in elements:
        elements.append({'data': {'id': vertex1, 'label': vertex1}})  # Добавляем label
    if {'data': {'id': vertex2}} not in elements:
        elements.append({'data': {'id': vertex2, 'label': vertex2}})  # Добавляем label

    # Добавляем ребро
    elements.append({'data': {'source': vertex1, 'target': vertex2}})
# Инициализация Dash приложения
app = dash.Dash(__name__)
# Определение layout
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        layout={'name': 'cose'},  # Используйте 'cose' для более приятного расположения
        style={'width': '100%', 'height': '600px'},
        zoomingEnabled=True,
        userZoomingEnabled=True,
        userPanningEnabled=True,  # Убедитесь, что это свойство правильно указано
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',  # Используем атрибут label для отображения
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'background-color': '#6FB1FC',
                    'border-color': '#000',
                    'border-width': 2,
                    'width': 100,
                    'height': 100,
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'width': 2,
                    'line-color': '#ccc',
                    'target-arrow-color': '#ccc',
                    'target-arrow-shape': 'triangle',
                }
            }
        ]
    ),
])
if __name__ == '__main__':
    app.run_server(debug=True)

# %%
