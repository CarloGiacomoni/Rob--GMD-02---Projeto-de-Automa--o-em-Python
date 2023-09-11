# Robô GMD 02 - Projeto de Automação em Python
Este é um projeto de automação em Python que visa facilitar o processo de cadastro de produtos em um formulário da empresa. O projeto utiliza a biblioteca PyAutoGUI para automatizar as ações do teclado e do mouse, e o Pandas para importar dados a partir de um arquivo CSV.

## Passo 1: Entrar no sistema da empresa / formulário / site
Para começar, é necessário entrar no sistema da empresa ou acessar o formulário online onde os produtos serão cadastrados. No exemplo abaixo, é utilizado o navegador Google Chrome:

![](https://github.com/CarloGiacomoni/Rob--GMD-02---Projeto-de-Automa--o-em-Python/blob/main/FOTO%2001.jpg)

Certifique-se de ajustar o link para o formulário correto ou o sistema da empresa que você deseja acessar.

## Passo 2: Importar a base de produtos para cadastrar
Antes de iniciar o cadastro, é necessário importar a base de produtos a partir de um arquivo CSV. Neste exemplo, utiliza-se a biblioteca Pandas para ler o arquivo "dados.csv" e armazenar os dados em um DataFrame:

![](https://github.com/CarloGiacomoni/Rob--GMD-02---Projeto-de-Automa--o-em-Python/blob/main/FOTO%2002.jpg)


Certifique-se de que o arquivo "dados.csv" esteja no mesmo diretório do seu projeto ou forneça o caminho correto para o arquivo.

## Passo 3: Cadastrar um produto
Agora, o código irá percorrer a base de produtos e realizar o cadastro de cada um deles no formulário. Ele faz isso preenchendo os campos necessários com as informações da base de dados:

![](https://github.com/CarloGiacomoni/Rob--GMD-02---Projeto-de-Automa--o-em-Python/blob/main/FOTO%2003.jpg)

Ajuste as coordenadas (X, Y) de acordo com a posição dos campos no seu formulário, se necessário.

Nota: O código inclui uma pausa entre as ações (1 segundo), que pode ser ajustada de acordo com a velocidade desejada para a automação.

# Observações
Para o formulário utilizado no teste, foi mencionado que a solução para ativar a próxima página e localizar a primeira caixa de resposta foi através da localização por coordenadas (X, Y). Recomenda-se que, se possível, você encontre métodos mais robustos para interagir com os elementos da página, como identificar campos por meio de seus atributos HTML ou usar bibliotecas específicas para automação web, como o Selenium.

Lembre-se de que a automação de sites ou sistemas deve ser realizada com responsabilidade e em conformidade com os termos de uso do serviço. Certifique-se de não violar nenhum regulamento ou política da empresa ou site que está sendo automatizado.
