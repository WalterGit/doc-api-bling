# Boas práticas

## Introdução

Quando se está desenvolvendo uma solução onde precisa consumir uma API de terceiro, é essencial saber lidar com ela para obter o melhor desempenho possível, dentro das condições que ela pode oferecer, para não se deparar com erros que poderiam ser evitados.

## Recomendações

Leia com atenção a documentação específica sobre a API que deseja implementar, para compreender todas as funcionalidades disponíveis para utilização.

Na documentação, estarão descritos os objetivos de cada _endpoint_ , método HTTP, filtros, _schemas_ de dados detalhado e os códigos de retornos.

## Paginação

A paginação é utilizada na obtenção de dados através do método GET. Para informar a página utilize o parâmetro `pagina`. Para controlar a quantidade de registros retornados na busca, utilize o parâmetro `limite`.

Por padrão, serão retornados 100 registros por requisição, sendo possível configurar a quantidade de registros conforme exemplo abaixo:

    GET /pedidos/vendas?pagina=2&limite=10

## Tratamento de erros

Durante o desenvolvimento é possível encontrar erros não previstos. Em decorrência a isso, é importante se atentar às mensagens de erro.

Verifique o código de estado HTTP, caso ele seja diferente de **2xx** , construa um tratamento de erros que seja eficiente e condizente ao retorno obtido.

Retornos com o HTTP code **4xx** , são erros provenientes de validação, leia a mensagem de erro no corpo da resposta e verifique os dados enviados na requisição.

Recomenda-se a criação de um ou mais componentes ou clientes REST para consumo da API.

## Segurança

De acordo com as orientações na seção de [autenticação](<https://developer.bling.com.br/autenticacao#Autentica%C3%A7%C3%A3o>), para maior segurança, as práticas abaixo são recomendadas:

  * Não deixe que mais alguém conheça o seu `client_secret`, `access_token` e nem do `refresh_token`.
  * Prefira gerar um `state` único para enviar na requisição e através dele valide a operação.
  * Garanta que a requisição para obter os _tokens_ de acesso sejam feitas sempre _server-to-server_.
  * Sempre utilize o protocolo HTTPS nas requisições.