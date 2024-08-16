import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from tqdm import tqdm  # Importar tqdm para a barra de progresso
encontrado = 0
nao_encontrado = 0
# Função para salvar os resultados em um arquivo Excel
def salvar_resultados_excel(resultados, caminho_arquivo):
    df = pd.DataFrame(resultados, columns=['CNPJ', 'Nome da Empresa', 'Informação'])
    df.to_excel(caminho_arquivo, index=False)
    print(f"Resultados salvos em {caminho_arquivo}")



# Configuração do serviço do ChromeDriver usando o WebDriver Manager

service = Service()
# Inicializar o navegador
navegador = webdriver.Chrome(service=service)

# Acessar o link
link = "https://economicasnet.ibge.gov.br/UploadPesquisa/pesquisar"
navegador.get(link)

# Ler a tabela de CNPJs
tabela = pd.read_excel('lista_ibge.xlsx')

# Maximizar a janela
navegador.maximize_window()

# Lista para armazenar os resultados
resultados = []

# Barra de progresso
for index, row in tqdm(tabela.iterrows(), total=tabela.shape[0], desc="Processando CNPJs"):
    cnpj = row['cnpj']
    nome_empresa = row['razao']
    try:
        time.sleep(2)  # Espera para garantir que o navegador esteja pronto
        print(f"Pesquisando CNPJ: {cnpj}")
        
        # Encontrar e preencher o campo de CNPJ
        cnpj_field = WebDriverWait(navegador, 4).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="RaizCNPJ"]'))
        )
        cnpj_field.clear()
        cnpj_field.send_keys(cnpj)
        
        # Clicar no botão de pesquisa
        search_button = WebDriverWait(navegador, 4).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/form/button'))
        )
        search_button.click()
        
        # Verificar se a pesquisa foi encontrada
        print('Verificar se a pesquisa foi encontrada')
        ibge_element = WebDriverWait(navegador, 4).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/p[3]'))
        )
        
        informacao = ibge_element.text  # Obter o texto da informação
        print(f'Pesquisa encontrada para o CNPJ \033[32m{cnpj}\033[0m')
        encontrado +=1
        print(f'\033{encontrado}\033[0m empresas encontradas')
        resultados.append([cnpj, nome_empresa, informacao])  # Adicionar à lista de resultados
        
    except Exception as e:
        print(f'Erro ao processar o CNPJ {cnpj}: {e}')
        nao_encontrado +=1
        print(f'\033[91m{nao_encontrado}\033[0m empresas nao encontradas')
        resultados.append([cnpj, nome_empresa, 'Não encontrado'])  # Adicionar CNPJ com informação de erro
        time.sleep(1)
        navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/p[1]/a').click()

# Fechar o navegador
navegador.quit()

# Definir caminhos dos arquivos
caminho_arquivo_excel = 'ibge_.xlsx'


# Salvar resultados no arquivo Excel
salvar_resultados_excel(resultados, caminho_arquivo_excel)

# Salvar resultados no arquivo texto

