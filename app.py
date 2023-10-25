from bs4 import BeautifulSoup
import re
import pandas as pd

# Caminho do arquivo HTML
html_file_path = r'C:\x'

# Abra o arquivo HTML
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse o HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Encontre todas as tags <div> com 'Ultima atualização:'
last_update_divs = soup.find_all('div', style='text-align:left;')

# Crie listas para armazenar os nomes das máquinas e as últimas atualizações
machine_names_list = []
last_updates_list = []

# Itere sobre as tags <div> com 'Ultima atualização:'
for update_div in last_update_divs:
    # Encontre a tag <h2> dentro da mesma <div>
    machine_name = update_div.find_previous('h2', class_='fs-4 fw-bold').get_text(strip=True)
    # Tente encontrar a tag <p> dentro da mesma <div>, verificando se ela existe
    last_update_tag = update_div.find('p')
    
    if last_update_tag:
        last_update = last_update_tag.get_text(strip=True)
        # Remova a parte decimal dos segundos (caso exista)
        last_update = re.sub(r'\.\d+', '', last_update)
        machine_names_list.append(machine_name)
        last_updates_list.append(last_update)

# Crie um DataFrame do pandas
data = {'Nome da Máquina': machine_names_list, 'Última Atualização': last_updates_list}
df = pd.DataFrame(data)

# Salve o DataFrame em um arquivo Excel
output_excel_path = 'Resultados.xlsx'
df.to_excel(output_excel_path, index=False)

print(f"Os resultados foram salvos em '{output_excel_path}'.")