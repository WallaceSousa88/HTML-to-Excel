# Documentação do Script de Extração de Dados HTML para Excel

## Visão Geral
Este script Python foi desenvolvido para extrair informações de um arquivo HTML que segue um padrão específico e salvar essas informações em um arquivo Excel (.xlsx). O script faz uso das bibliotecas `BeautifulSoup` e `pandas` para realizar essa tarefa.

## Pré-Requisitos
Antes de executar este script, você deve garantir que o seguinte software e bibliotecas estejam instalados em seu ambiente de desenvolvimento:

1. Python: O script foi desenvolvido em Python 3.

2. Biblioteca `BeautifulSoup`: Essa biblioteca é usada para analisar o HTML e extrair informações. Você pode instalá-la com o comando:

   pip install beautifulsoup4

3. Biblioteca `pandas`: Esta biblioteca é usada para criar e salvar DataFrames em arquivos Excel. Você pode instalá-la com o comando:

   pip install pandas

4. Biblioteca `openpyxl`: Esta biblioteca é usada pelo `pandas` para salvar arquivos Excel. Você pode instalá-la com o comando:

   pip install openpyxl

## Uso
Siga estas etapas para utilizar o script:

1. Certifique-se de que todos os pré-requisitos estão instalados corretamente.

2. Altere a variável `html_file_path` para o caminho do arquivo HTML que você deseja analisar.

3. Execute o script Python. Isso pode ser feito a partir do terminal ou do ambiente de desenvolvimento de sua escolha. Por exemplo:

   python extrair_dados.py

4. O script lerá o arquivo HTML, extrairá as informações e as salvará em um arquivo Excel. O arquivo Excel resultante será chamado de "resultados.xlsx".

## Resultados
Após a execução bem-sucedida do script, você terá um arquivo Excel chamado "resultados.xlsx" que contém duas colunas. As informações extraídas do arquivo HTML serão organizadas nessas colunas.

## Notas Adicionais
- Este script assume que o arquivo HTML de origem segue o padrão mencionado na descrição. Certifique-se de que o HTML que você deseja analisar está formatado corretamente.
- Você pode personalizar ainda mais o script para atender às suas necessidades específicas, como alterar o nome do arquivo de saída ou o formato da data e hora na saída.
- Esta documentação fornece uma visão geral e instruções básicas para usar o script de extração de dados HTML para Excel. Certifique-se de configurar corretamente o ambiente e o arquivo HTML de origem antes de executar o script.