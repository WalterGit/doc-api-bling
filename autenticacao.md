# Autenticação

## Fundamentos

Dentro dos fundamentos da segurança entre redes, a API dispõe de regras que assegurem a confidencialidade, a integridade e a acessibilidade das informações disponíveis:

  * **Confidencialidade** : É a estrita regra de manter uma autorização através de uma autenticação de acesso ao recurso.

  * **Integridade** : Assegura que os dados não poderão ser alterados sem as devidas permissões, ou que os dados não sejam visualizados em conta diferente a qual está solicitando o uso ao recurso.

  * **Acessibilidade** : Permite a cada usuário uma disponibilidade de acesso sem prejudicar o serviço que por consequência afeta todos os outros usuários dos nossos recursos. Mantemos as informações dos nossos usuários seguras pela utilização de HTTPS e por _tokens_ gerados por aplicativos OAuth.

## OAuth e tokens de acesso

OAuth 2.0 é um protocolo de autorização utilizado para permitir que aplicativos de terceiros tenham acesso limitado aos recursos dos usuários do sistema, no qual o sistema detentor dos dados do usuário fica encarregado de realizar a autenticação e, por fim, após a aprovação deste usuário, conceder a autorização para o aplicativo acessar os seus recursos.

Descubra como criar seus aplicativos e gerar os _tokens_ de acesso através do [fluxo de autorização](<https://developer.bling.com.br/aplicativos#fluxo-de-autoriza%C3%A7%C3%A3o>). Em resumo, quando um usuário autoriza determinado aplicativo a acessar os seus recursos, este aplicativo conseguirá obter os _tokens_ necessários para realizar as requisições e acessar o recurso. Veja abaixo como utilizar o Bearer _token_ gerado pelos aplicativos OAuth.

## Como utilizar os tokens

O tipo de token fornecido pelo protocolo OAuth é o Bearer, portanto, utilize o esquema "Bearer" de autenticação HTTP, inserindo a chave de acesso no cabeçalho da requisição, veja o formato abaixo.

`GET /Api/v3/[caminho_da_api_desejada]`

**Host** : <https://api.bling.com.br>

**Header** : `Authorization: Bearer [access_token]`

Abaixo contempla um exemplo de uma requisição cURL para a API de contatos.

    curl --location --request GET 'https://api.bling.com.br/Api/v3/contatos'
    	--header 'Authorization: Bearer [REDACTED]'

Possíveis erros e exceções com relação ao uso destes _tokens_ são tratados [aqui](<https://developer.bling.com.br/aplicativos#token-expirou>).