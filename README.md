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
# Teste completo:
![Fluxo completo](imgs\teste_completo.gif)
# Automação de testes API PetStore
O objetivo dessa sessão do trabalho é fazer um teste dos endpoint da api da [PetStore](https://petstore.swagger.io/#/).

Nesse teste foram elaborados scripts usando o pytest para automatizar o processo e evitar de fazer verificar todos os endpoint da api manualmente.

Ele focou principalmente em descobrir se a API se comportava adequadamente quando as requisções corretas chegavam a ela.
## Considerações:
Pessoalmente, essa foi a parte complicada do trabalho porque o uso de API, até então, ainda não tinha sido um ponto de foco dos meus estudos. Por isso, eu fiz mais uso de inteligÊncia artificiais, como o claude, para auxiliar o projeto.

Outra tópico importante, é que inicialmente, eu pretendia fazer os testes tanto de acertos, quanto de erros, porém devido minha inexperiência na época eu não consegui fazer a parte dos erros e nem acho que fiz as respostas da melhor forma possível, faltando deixar mais clara as saídas no terminal além de se deu certo ou errado, um falaha que pretendo corrigir fututamente.

Além dessa minha inexperiência, eu tambem tive dificuldades em forçar erros na api ultilizada porque ela tem poucas medidas de segurança, aceitando quase qualquer coisa. Por exemplo, em dos testes implementados, o de login de usuário, ela aceita campos nulos para fazer login.

Ademais, ela possui problemas graves na forma como implementada e documentada. Por exemplo, ela faz a requisição do login usando o método "GET" ao invés de post, o que causa uma falha de segurança ao expor na url do navegador dados sensíveis como o nome de usuário e a senha dele. Além de que, o campo "/user/createWithList" está duplicado na documentação gerando possíveis confusões na hora do uso dela.

Por fim, em atualizações futuras pretendo adicionar testes que forcem o erro, melhorar as saídas do teste no terminal e possivelmente repetir os mesmo testes utilizando a ferramenta Postman


## Demonstração:
![Fluxo Api PetStore](imgs\teste_api_pet_store.gif)
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
>obs: No env_exemple o "SAUCE_NOME" e o "SAUCE_PASSWORD" já estão com valores padrões indicados pelo pro Sauce, de uma lista pronta. Caso deseje mudar esses valores acesse o site do [Sauce Store](https://www.saucedemo.com/)

## Considerações:
Essa parte do trabalho eu achei ela mais tranquila de fazer, porem um pouco mais trabalhosa. Isso deve ao fato que para efetuar a altomação eu precisei ficar buscando os componentes do HTML, manualmente.

Essa foi a minha maior dificiuldade porque eu não sabia, no início do trabalho, que dava para por eles dentro duma lista de uma vez se eles tivesse algo em comum, como ID, CLASS_NAME ou TAG_NAME. Depois que descobri isso o trabalho foi bem fácil de fazer.

A conclusão que eu cheguei é que o selenium é ferramenta muito boa de usarm, porém as vezes pode ficar dependente de quem escreveu as páginas que serão testadas ter seguido boa práticas de desenvolvimento web, como colocar classes e id's nos elementos HTML.

## Demonstração:

![Teste com interface](imgs\teste_sauce_inter.gif)

![Teste sem a interface](imgs\teste_sauce_no_int.gif)

# Rodando a aplicação:
Para rodar ambas os testes ao mesmo tempo rode o comando abaixo, na raiz do projeto, no terminal:

> python main.py

Para rodar apenas o teste da API, dentro da raiz do projeot, rode em seu terminal:
>python PetStore_Swager_Teste\main.py

Para rodar apaenas o teste do Sauce, dentro da raiz do projeto, rode o comando:
> python automacao_sauce\main.py
