# WebScraping-IBGE-PESQUISA
WebScraping para o site IBGE na pesquisa anual das empresas.
Pesquisa de CNPJs no IBGE com Selenium
Este script Python automatiza a pesquisa de CNPJs em um site do IBGE, utilizando a biblioteca Selenium para manipulação do navegador e pandas para manipulação de dados. O resultado das pesquisas é salvo em um arquivo Excel.

Requisitos
Python 3.x
Google Chrome
Bibliotecas Python:
pandas
selenium
webdriver-manager
tqdm
Instalação
Clone o repositório ou baixe o código.

Instale as dependências necessárias executando:

bash
Copiar código
pip install pandas selenium webdriver-manager tqdm
Certifique-se de ter o Google Chrome instalado.

Configuração
Arquivo de entrada: Certifique-se de ter um arquivo Excel chamado lista_ibge.xlsx na pasta raiz do projeto. Este arquivo deve conter uma coluna cnpj com os CNPJs a serem pesquisados e uma coluna razao com os nomes das empresas.
Uso
Execute o script Python:

bash
Copiar código
python script.py
O script irá automatizar o navegador Google Chrome, pesquisar cada CNPJ no site do IBGE, e salvar os resultados em um arquivo Excel chamado ibge_.xlsx.

Detalhes do Funcionamento
O script inicializa o navegador, acessa o site do IBGE e preenche o campo de pesquisa com os CNPJs fornecidos no arquivo lista_ibge.xlsx.
Para cada CNPJ, o script verifica se a pesquisa foi bem-sucedida e, em seguida, extrai as informações correspondentes.
Os resultados são salvos em um arquivo Excel, com as colunas "CNPJ", "Nome da Empresa" e "Informação".
Em caso de erro ou falha na pesquisa, o script registra o CNPJ com a indicação "Não encontrado".
