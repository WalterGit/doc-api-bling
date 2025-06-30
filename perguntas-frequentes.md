# Perguntas frequentes

## Como gerar o Access Token?

O primeiro passo é a criação de um [aplicativo](<https://developer.bling.com.br/aplicativos#aplicativos>). Após o desenvolvedor irá solicitar por meio do aplicativo, acesso à conta do Bling que deseja operar. Nesse momento o cliente que opera a conta irá fazer login e autorizar o aplicativo a realizar as operações na mesma, retornando de forma automática o _authorization code_ na URL de redirecionamento configurada no aplicativo. Por fim, será necessário o desenvolvedor realizar uma requisição ao _authorization server_ com o _authorization code_ obtido, e então o _access token_ será retornado no formato JSON. Para o passo a passo detalhado, acesse a seção de [fluxo de autorização](<https://developer.bling.com.br/aplicativos#fluxo-de-autoriza%C3%A7%C3%A3o>).

## Como gerar o client_id e o client_secret?

Após a criação do aplicativo, será exibido ao lado do formulário o `client_id` e `client_secret`.

## Qual é o formato de retorno das respostas da API?

O formato de retorno é em JSON, conforme o exemplo:

    {
    	"data": {
    		"id": 123,
    		"nome": "Bling",
    		"numero": 1
    	}
    }

## Quais são os limites da API?

No Bling existem limites de frequência, no qual a regra permite até 3 requisições por segundo e 120 mil requisições por dia. Entretanto, existe também outras validações por [bloqueio de IP](<https://developer.bling.com.br/limites#requisi%C3%A7%C3%B5es>).

A limitação de API é o processo de limitar o número de requisições que um usuário pode fazer em um determinado período.

## Quantos registros são retornados por página em cada requisição?

Por padrão são retornados até 100 registros por requisição.

APIs que possuem paginação irão retornar os resultados em páginas, ou seja, para obter todos os registros serão necessárias mais de uma requisição, informando o parâmetro `pagina`. Mais informações podem ser encontradas na seção de [boas práticas](<https://developer.bling.com.br/boas-praticas#paginacao>).

## Qual é a utilidade do campo state?

A utilidade principal do campo state é evitar _cross-site request forgery_ (CSRF) para o endpoint configurado na URL de redirecionamento do aplicativo. O _client app_ gera um token aleatório e o informa no campo `state` ao solicitar o [Authorization code](<aplicativos#authorization-code>), após o usuário conceder acesso ao aplicativo, o token é retornado ao _client app_ junto à URL de redirecionamento, dessa forma, é possível verificar que a origem é de fato o Bling.

Além disso, pode ser usado de maneira flexível, já que é possível informar qualquer valor para o campo e reinterpretá-lo no redirecionamento. Por exemplo, criptografando um json contendo um timestamp e um ambiente `{"timestamp":1698757251.796,"environment":"dev"}`, após o redirecionamento ao _client app_ , é possível descriptografar o `state` e verificar se o processo foi realizado em tempo hábil e se o ambiente que o usuário está é valido para a utilização do aplicativo.

## Preciso criar uma conta no Bling para utilizar a API?

Sim. A utilização da API do Bling requer a criação de uma conta, para cadastro de um aplicativo de visibilidade pública. É necessário também passar por um processo de homologação, o qual assegura a conformidade da conta com os padrões exigidos pela API. Concluída a etapa de testes de 30 dias, a conta permanece ativa, dispensando a necessidade de solicitar isenções para prosseguir com o uso do serviço.