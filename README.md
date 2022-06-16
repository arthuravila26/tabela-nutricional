# tabela-nutricional API

A API de Tabela Nutricional tem a ideia de poder trazer o calculo para a criação
de um alimento a partir de ingredientes informados em um JSON. Desta forma, teremos
os valores de uma tabela nutricional de uma receita em forma de JSON.

# Conceito técnico

Dentro desse projeto, temos um JSON com alimentos e seus valores nutricionais.
Por ser um projeto aonde não possue dados sensíveis, não há risco de manter esses
dados dentro do proprio projeto.

O banco de dados utilizado para o projeto é o MongoDB, um banco NoSQL que permite
trabalhar o armazenamento de dados a partir de um JSON. Por ser tratar de um projeto
ainda pequeno, não será necessário a criação de um banco de dados, que envolveria custos.
Como melhor opção para o projeto, o banco de dados será provisionado em um ambiente
de container, que nos permite ter um banco de dados local de forma mais prática e com
mais facilidade de administrar.

A linguagem principal do projeto será Python e utilizaremos a MicroFramework FastAPI
para utilizarmos o Python para Web. A principio, o programa será executado fara uma
verificação no banco de dados local para saber se o mesmo já está populado com os dados
nutricionais dos alimentos. Caso positivo, ele ira inicializar o webserver responsavel por
subir a API, caso negativo, o programa fara a população dos dados no banco local utilizando
o arquivo JSON com as informações no diretorio /app/db/initial_load/lista-combinada.json e 
após a população, inicializará a API.

# Como executar

O programa exige que a máquina possua os seguintes programas instalados para ser executado localmente:

- Python 3.x
- Pip 3.x
- Docker Compose e Docker

Antes de executar o programa, é necessário ter o banco de dados inicializado. O mesmo pode ser
inicializado com o comando (Este comando precisa ser executado dentro do diretorio do projeto):
`docker-compose up`

Apos ter o banco de dados provisionado, é necessário criar um ambiente virtual para poder instalar
os requerimentos do Python para a execução do programa. Esse não é um passo obrigatório, porem, é
altamente recomendável e pode ser feito seguindo os passos do link: https://docs.python.org/pt-br/3/library/venv.html

Após ter os passos executados, é necessário fazer a instalação dos requerimentos do programa. Isso pode
ser feito utilizando o comando: `pip3 install -r requeriments.txt`

Feito isso, antes de executar o programa, é necessário exportar para o sistema operacional a váriavel
que se encontra dentro do arquivo `env`. Esta variavel é a URI de conexão com o banco de dados e utilizando
a mesma como variavel de ambiente, evitamos de utilizar a mesma de forma hard coded no código.

Para executar a API, é preciso rodar o comando `python3 run.py` e com isso, o webserver será inicializado com
a API.
