# Requisitos para uso:

Primeiramente, para ultilizar o software desenvolvido nesse repositório você precisário fazer o clone do repositório com o seguinte comando:

````
git clone https://github.com/guiSanMelo/Automocao_Testes_Prova_P2.git 

````

Em seguida, vocÊ precisará iniciar o ambiente virtual. Para isso, esteja dentro da pasta que você clonou o repositório e digite:

> Windows:

````
venv\Scripts\activate 
````

>Linux:
````
source venv/bin/activate   
````
Após isso, você precisará baixar em seu projeto as dependências usadas e nas versões desse repositório. Abra o terminal dentro do repositório e digite:
````
pip install -r requirements.txt   
````
Por fim, você precisa criar um arquivo ".env", colocando as variáveis como no arquivo ".env_exemple". Em seguida você deve preenchê-las com as informações necessárias.
>  Os valores em "SAUCE_USERNAME" e "SAUCE_PASSWORD" são valores padrões para acessar o site do experimento, portanto não devem ser alterados.

# Automação de testes API


# Automação de testes Sauce
O objetivo dessa sessão do trabalho é fazer um fluxo de um usuário hipotético, que decidiu comprar alguns items numa loja hipoetética, ultilizando a loja fictícia do [Sauce Labs](https://www.saucedemo.com/).

Nessa situação, o usuário irá comprar todos items na loja porque é um oniomaníaco, comprador compulsivo, por isso irá colocar todos os items do catálogo no carrinho de compras e se direcionar pra essa página. 

No carrinho, ele irá verificar se possui orçamento o suficiente para adiquirir todos os items que colocou nele. Se possuir, irá finalizar a compra. Caso contrário, ele irá remover o item de maior valor do carrinho até que o total dos produtos seja igual menor ao seu orçamento.

Seguindo para o checkout, ele informará nome, sobrenome e CEP e clicar para finalizar a compra. Com todos os dados certos, ele irá finalisar a compra. Se não, irá voltar para a página em que coocou as informações e alterá-las, repetir anterior e finalizar a compra. 

Para comprovar o funcionamento do teste, coloque dados fictícios nos seguintes campos no seu arquivo ".env" com dados fictícios:
````
SAUCE_NOME=
SAUCE_SOBRENOME=
SAUCE_CEP=
SAUCE_ORCAMENTO=
````

## Demonstração Atutomação Sauce:
[![Watch the video](imgs\selenium-logo-png_seeklogo-394619.png)](https://youtu.be/ol5yTjFMmrg)   