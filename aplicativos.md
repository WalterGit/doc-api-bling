# Aplicativos

## Introdução

Este manual contempla o passo a passo aos integradores que desejam criar um aplicativo e entender o funcionamento do fluxo de autorização para a obtenção dos tokens de acesso do OAuth 2.0.

### Acesso ao módulo

É possível cadastrar um aplicativo pela conta do administrador ou criando um usuário para tal finalidade. Recomendamos a criação de um usuário para cada desenvolvedor, dessa forma, cada usuário poderá gerenciar somente os seus aplicativos.  

  1. Para criar um usuário acesse o menu ["Preferências > Sistema > Usuários"](<https://bling.com.br/usuarios.php>), clique em "Incluir usuário".  

  2. Nas permissões de "Cadastros" selecione "Cadastro de aplicativos" e preencha as informações da conta do usuário.  

Após esse processo, o usuário possuirá acesso ao módulo de [Cadastro de aplicativos](<https://bling.com.br/cadastro.aplicativos.php>).

### Como cadastrar

  1. Acesse a Central de Extensões
  2. Clique em "Área do Integrador"

Na tela de cadastro de aplicativos clique no botão **CRIAR NOVO APLICATIVO**.

#### Visibilidade

Escolha a visibilidade do aplicativo:

Visibilidade | Descrição  
---|---  
Público | O aplicativo será utilizado para realizar operações em outras contas Bling e passará pelo processo de [homologação](<https://developer.bling.com.br/homologacao#homologa%C3%A7%C3%A3o>). Enquanto não for homologado, o número de usuários que podem autorizá-lo estará restrito a 10.  
Privado | O aplicativo será utilizado para realizar operações na própria conta Bling.  

Clique em próximo. Na sequência preencha os seguintes dados do aplicativo:

  * **Logo** : Exibido aos usuários do aplicativo.
  * **Nome** : Exibido aos seus usuários.
  * **Categoria** : Classificação de negócio.
  * **Descrição** : Detalhamento das principais características e finalidades deste aplicativo.
  * **Link de redirecionamento** : Utilizado na etapa de [autorização](<https://developer.bling.com.br/aplicativos#fluxo-de-autoriza%C3%A7%C3%A3o>).
  * **Link da homepage** : Endereço do site do aplicativo.
  * **Nome do desenvolvedor** : Nome do desenvolvedor do aplicativo.
  * **Email** : Email para eventuais contatos do nosso time.
  * **Celular** : Celular para eventuais contatos do nosso time.
  * **Lista de escopos** : [Escopos](<https://developer.bling.com.br/aplicativos#escopos>) referentes aos dados dos usuários que serão acessados pelo aplicativo.

Após o preenchimento dos dados, clique no botão **Salvar** para finalizar a criação do aplicativo. O botão será habilitado somente após a inserção de um escopo.

#### Categorias

As categorias são utilizadas para facilitar o cliente na busca por um aplicativo, sendo elas:

Nome | Descrição  
---|---  
Marketplace | Plataforma para reunir diversos vendedores em um só lugar.  
Plataforma de e-commerce | Sistema para criação e gerenciamento de lojas virtuais.  
Hub | Plataforma centralizadora de conexões com canais de venda.  
Delivery | Plataforma para entrega rápida de produtos.  
Social commerce | Estratégia para venda de produtos e serviços através de redes sociais.  
Gestão de entregas | Controle, organização e acompanhamento dos envios e entregas.  
Gestão de estoques | Controle, organização e acompanhamento de estoque dos produtos.  
Controle financeiro | Sistema para realizar a gestão de operações financeiras.  
Precificação | Sistema para ajudar a determinar os preços ideais de produtos.  
Vendas presenciais | Gestão de vendas realizadas em lojas físicas, balcões ou pontos de venda.  
Automação de vendas | Sistema para automatizar tarefas comerciais referentes ao processo de vendas.  
CRM | Sistema para gerenciar interações com clientes.  
Dashboards e BI | Painel para apresentar informações importantes, resumidas e permite uma análise rápida.  
Soluções em IA | Resolução de problemas por meio de inteligência artificial.  
ERP | Sistema para controlar operações da empresa, como estoque, vendas, entre outros.  
Outro | Destinada para casos não enquadrados em outras categorias.  

#### Imagens do aplicativo

Utilizadas somente em aplicativos públicos.

As imagens do aplicativo são exibidas na tela de contratação do aplicativo e podem ser usadas como uma forma de divulgar as funcionalidades presentes no sistema. É permitido realizar o upload de até cinco imagens.

Exemplo de aplicativo com imagens:

#### Escopos

O Escopo é a representação da permissão para operar sobre os recursos do usuário. Portanto, informe somente os escopos necessários, passando maior clareza e segurança ao usuário no momento da autorização do aplicativo.

Para inserir os escopos clique no botão **Adicionar** , conforme ilustrado na imagem a seguir.

Marque os escopos que serão utilizados pelo aplicativo e clique no botão **Adicionar**. Caso seja necessário, é possível filtrar os escopos por módulo e nome, usando a busca localizada no topo desta janela.

Os escopos escolhidos serão listados no formulário. Para excluir um escopo, passe o cursor sobre a linha desejada e clique no ícone da lixeira, uma janela pedindo a confirmação da exclusão será exibida.

Se precisar inserir novos escopos, clique na ação de **Adicionar escopo** logo abaixo da listagem.

É importante lembrar que o aplicativo só terá acesso aos dados referentes aos escopos selecionados. Qualquer adição ou exclusão de escopos só será confirmada após o salvamento do aplicativo. Se isso acontecer, uma janela de confirmação será exibida.

Ao confirmar a edição, todos os usuários do aplicativo serão automaticamente revogados. Desta forma, é garantida a segurança das informações dos usuários, exibindo a nova listagem de escopos no momento da autorização.

#### Modelo de manual

##### Passos no Bling:

Para integrar com o aplicativo XXXXX, na API v3, acesse a sua conta Bling e clique no menu da **Central de Extensões**.

Neste menu é possível buscar na barra de pesquisa o aplicativo XXXXX.

Ao localizar o aplicativo desejado, será possível clicar em **Instalar aplicativo**.

Ao clicar para instalar, é solicitada a autorização:

Isso irá autorizar o aplicativo a obter os tokens e se comunicar com sua conta Bling. A partir desse momento, todas as configurações no Bling estão finalizadas.

##### Passos no Integrador (Informações que o desenvolvedor do app deve adicionar no manual)

Descreva o fluxo que o cliente precisa seguir em seu site/sistema:

**REQUISITOS**

**Existe a obrigatoriedade de ter uma conta antes de instalar o aplicativo?**

Se sim, explique como e onde criar a conta:

Ex: Acesse [www.aplicativov3.com.br](<http://www.aplicativov3.com.br>), clique em criar a conta, forneça email e nome…

**Há preparações necessárias na conta antes de autorizar o aplicativo? Se sim, descrever os processos necessários:**

Ex: Para integrar com o Bling, antes de permitir a integração, deve ser acessado a tela de “gerir conta” e clicar em “Integrar com o Bling”

**Após a autorização, quais passos o cliente deve seguir para que a integração ocorra com sucesso?**

**CONTATO**

**Informe o contato do suporte ao seu sistema:**

Ex: Telefone/Email que o cliente pode entrar em contato.

#### Informações do aplicativo

Após a criação do aplicativo, a aba "Informações do app" ficará disponível. Atente-se ao **Client Id** e ao **Client Secret** , que serão utilizados no momento da [autorização](<https://developer.bling.com.br/aplicativos#fluxo-de-autoriza%C3%A7%C3%A3o>).

É possível revogar os usuários do aplicativo. Essa ação exclui todos os _tokens_ de acesso e faz com que os usuários tenham que realizar novamente a etapa de autorização. Ao executar a ação através do botão **Revogar usuários** , será solicitada a confirmação da ação.

Logo abaixo da quantidade de usuários é possível visualizar as credenciais do aplicativo. Para revelar o **Client Secret** clique no ícone de olho. Assim como qualquer credencial, é importante manter a chave em segredo. Essa credencial será utilizada nas requisições para obtenção de [tokens de acesso](<https://developer.bling.com.br/aplicativos#tokens-de-acesso>). O **Client Secret** poderá ser alterado a qualquer momento clicando no botão **Redefinir client secret**.

Após pressionar o botão **Redefinir client secret** será solicitada a confirmação da ação. A ação gera um novo **Client Secret** , portanto será necessário realizar a alteração nas requisições que fazem uso do **Client Secret** anterior.

#### Exclusão

Com a exclusão do aplicativo, todos os _tokens_ de acesso dos usuários serão automaticamente revogados.

Para excluir, na aba "Informações do app", ao confirmar a ciência da ação, o botão **Excluir aplicativo** será exibido.

### Códigos de acesso

Para gerar os códigos de acesso é necessário que os usuários deem autorização sobre o acesso aos dados das contas, ao aplicativo. O OAuth 2 protocola 4 tipos de concessão para que essa autorização seja realizada, no entanto o Bling fará uso de apenas uma delas, que é o _Authorization Code_. Portanto, será necessário seguir o fluxo de autorização descrito abaixo para obter os códigos de acesso.

#### Terminologia

Termo | Detalhamento  
---|---  
Client App | Aplicativo que fará uso dos dados das contas dos usuários (conta Bling).  
Authorization Code | Código enviado ao _Client App_ quando um usuário autoriza acesso aos dados.  
Access Token | _Token_ utilizado para requisição do recurso dos usuários.  
Refresh Token | _Token_ utilizado para requisitar um novo `access_token`, quando o mesmo expirar.  

#### Fluxo de autorização

Segue abaixo um resumo das etapas do fluxo de autorização.

  1. O _client app_ , com a intenção de obter o `authorization_code`, redireciona o usuário (através do seu _user agent_) para o _authorization server_.
  2. O usuário se autentica no sistema e autoriza, ou não, o aplicativo.
  3. O _authorization server_ redireciona o usuário (através do _user agent_) de volta ao _client app_ , utilizando a “URL de redirecionamento” inserida no cadastro do aplicativo. Se o usuário autorizou o acesso aos seus recursos, o `authorization_code` será incluído no retorno e segue-se para o passo a seguir. Caso contrário, o fluxo de autorização termina aqui.
  4. O _client app_ requisita o `access_token`, fazendo uma requisição para o _authorization server_ com o `authorization_code` recebido no passo anterior.
  5. Se o `authorization_code` for válido, o _authorization server_ retornará um JSON contendo o `access_token` e o `refresh_token`.

#### Authorization code

Utilizando redirecionamento de URL o _client app_ direciona o usuário para o _endpoint_ `authorize`:

    GET
    /Api/v3/oauth/authorize?response_type=code&client_id=[seu_client_id]&state=[sequencia_de_caracteres_aleatorios] HTTP/1.1
    Host: https://www.bling.com.br

Parâmetro | Descrição  
---|---  
`response_type` | O valor deve ser code. Significa que o aplicativo está requisitando um `authorization_code`.  
`client_id` | _Client_ id do aplicativo, exibido na edição do aplicativo.  
`state` | Sequência aleatória de caracteres e de preferência única para cada sessão. O valor informado será mantido pelo _authorization server_ e incluído na resposta ao _client_. Assim, ao comparar o valor recebido do enviado, é possível amenizar problemas com _cross-site request forgery_ (CSRF).  

Os parâmetros `redirect_uri` e `scope` são considerados de uso opcional pela [RFC](<https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.1>), portanto, os mesmos não serão exigidos na requisição. Para estes dois parâmetros sempre serão usados os valores inseridos previamente no cadastro de aplicativos, mesmo que os mesmos sejam utilizados na requisição.

URL de exemplo da requisição:

    https://bling.com.br/Api/v3/oauth/authorize?response_type=code&client_id=[REDACTED]77594&state=291e61b56ab3d845622cf137b1e1e2

Se o usuário autorizar a sua solicitação, o _authorization server_ irá redirecionar o _user agent_ para a URL de redirecionamento do aplicativo. Os parâmetros abaixo são incluídos na URL de redirecionamento:

Parâmetro | Descrição  
---|---  
`code` | _Authorization code_ , que possui tempo de expiração de 1 minuto. Utilizado para obtenção dos _tokens_ de acesso.  
`state` | Mesmo valor informado na requisição. Caso o state retornado for diferente do utilizado na requisição, ignore-a e interrompa o fluxo de autorização.  

Exemplo de URL usada como _callback_ com os parâmetros utilizados no retorno do _authorization server_ :

    https://www.clientapp.com.br/callback?code=[REDACTED]&state=291e61b56ab3d845622cf137b1e1e2

#### Tokens de acesso

Com o `authorization_code` o _client app_ deve realizar uma requisição POST para o _endpoint_ `/token`, nisso o code será validado e os _tokens_ de acesso serão retornados. Lembrando que o prazo para realizar esta requisição é de 1 minuto, este é o tempo de expiração do _code_.

Formato da requisição HTTP que deve ser utilizado e uma tabela com o conteúdo que deve ser inserido no _body_ :

    POST /Api/v3/oauth/token? HTTP/1.1
    Host: https://www.bling.com.br
    Content-Type: application/x-www-form-urlencoded
    Accept: 1.0
    Authorization: Basic [base64_das_credenciais_do_client_app]
    grant_type=authorization_code&code=[authorization_code]

Parâmetro no body | Descrição  
---|---  
`grant_type` | O valor deve ser authorization_code. Informa o tipo de concessão utilizado.  
`code` | _Authorization code_ obtido na requisição do tópico anterior.  

O _client app_ precisa ser autenticado para realizar esta operação, portanto, será necessário informar as suas credenciais no cabeçalho da requisição (não é permitida a inserção destes parâmetros no _body_). Para isso use o esquema “Basic” de autenticação HTTP inserindo um cabeçalho no formato:

    Authorization: Basic [credenciais_do_client_app]

Lembrando que estas credenciais devem ser o `client_id` junto do `client_secret` separados por "`:`" e codificados em `base64`. Também é importante utilizar HTTPS / TLS para garantir a segurança dos seus dados.

Faça a requisição inteiramente no lado do servidor, busque evitar a exposição de qualquer dado inserido nela, como as credenciais do app ou o `authorization_code`.

Segue um exemplo de requisição dos _tokens_ de acesso utilizando cURL:

    curl --location --request POST 'https://api.bling.com.br/Api/v3/oauth/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --header 'Accept: 1.0' \
    --header 'Authorization: Basic [REDACTED][REDACTED][REDACTED]N2Y0NjYxOWFhMDk=' \
    --data-urlencode 'grant_type=authorization_code' \
    --data-urlencode 'code=[REDACTED]'

Caso a requisição seja válida, será retornado um objeto JSON contendo o `access_token`, com o seu tipo, tempo de expiração, escopos permitidos e o `refresh_token`. Veja abaixo um exemplo desse retorno e um quadro com a explicação de cada parâmetro.

    {
    	"access_token": "[REDACTED]",
    	"expires_in": 21600,
    	"token_type": "Bearer",
    	"scope": "98309 318257570 5862218180",
    	"refresh_token": "[REDACTED]"
    }

Parâmetro da resposta | Descrição  
---|---  
`access_token` | _Token_ utilizado para requisitar os recursos do usuário.  
`expires_in` | Tempo de expiração do `access_token` em segundos.  
`token_type` | Tipo do esquema de autenticação (Bearer Authentication).  
`scope` | Lista dos ids dos escopos que o app possui permissão de acesso.  
`refresh_token` | _Token_ utilizado para requisitar um novo token de acesso, após a expiração do `access_token`.  

#### Refresh Token

Quando o tempo do `access_token` terminar é possível requisitar um novo utilizando o `refresh_token`, o qual foi enviado junto do `access_token` e possui um tempo de expiração superior, de 30 dias. Para isso é realizada uma requisição POST para o _endpoint_ `token`, na mesma estrutura da requisição apresentada anteriormente, a única diferença está nos parâmetros que devem ser apresentados no _body_. Veja abaixo o formato da requisição HTTP que deve ser utilizado e a tabela com o conteúdo que deve ser inserido no _body_.

    POST /Api/v3/oauth/token? HTTP/1.1
    Host: https://www.bling.com.br
    Content-Type: application/x-www-form-urlencoded
    Accept: 1.0
    Authorization: Basic [base64_das_credenciais_do_client_app]

    grant_type=refresh_token&refresh_token=[refresh_token]

Parâmetros no body | Descrição  
---|---  
`grant_type` | O valor deve ser `refresh_token`. Informa o tipo de concessão utilizado.  
`refresh_token` | _Refresh token_ obtido na requisição do `access_token` que expirou.  

O retorno desta requisição é o mesmo JSON retornado na requisição do `access_token` com uso do `authorization_code`.

#### Utilizando o access token

Com o `access_token` é possível realizar requisições para a API do Bling e, assim, acessar os recursos do usuário. Lembrando que este tipo de autenticação só está disponível pela API v3 e só será possível requisitar os dados dos escopos que foram permitidos pelo usuário.

Como informado no JSON de retorno dos _tokens_ de acesso, o tipo do token fornecido é o Bearer, portanto, utilize o esquema "Bearer" de autenticação HTTP, inserindo a chave de acesso no cabeçalho da requisição, conforme exemplo:

    GET /Api/v3/[caminho_da_api_desejada] HTTP/1.1
    Host: https://www.bling.com.br
    Authorization: Bearer [access_token]

Exemplo de uma requisição cURL para a API de contatos:

    curl --location --request GET 'https://api.bling.com.br/Api/v3/contatos' \
    --header 'Authorization: Bearer [REDACTED]' \

#### Revogando o access token

É possível revogar um `access_token` ou `refresh_token` para impedir que um usuário ou uma empresa continuem acessando a API. Essa funcionalidade garante que apenas os tokens desejados sejam invalidados.

Para revogar um token, o _client app_ deve realizar uma requisição POST para o _endpoint_ `/oauth/revoke`, utilizando o esquema "Basic" de autenticação HTTP para fornecer suas credenciais, conforme exemplo:

    POST /oauth/revoke HTTP/1.1
    Host: https://www.bling.com.br
    Content-Type: application/x-www-form-urlencoded
    Authorization: Basic [base64_das_credenciais_do_client_app]

    token=[ACCESS_OR_REFRESH_TOKEN]&token_type_hint=[access_token|refresh_token]

Parâmetros no body | Descrição  
---|---  
`token` | O `access_token` ou `refresh_token` utilizado para se autenticar na api.  
`token_type_hint` | Define o tipo de token informado. Pode ser "access_token" ou "refresh_token".  

Se essa requisição for bem-sucedida, o token informado será revogado, impedindo seu uso para novas requisições na API.

#### Revogação avançada

Para atender a necessidade de remoção de todos os tokens associados a um usuário ou empresa, foram adicionados os parâmetros `revoke_action` e `revoke_target`, que ampliam o escopo da revogação.

    POST /oauth/revoke HTTP/1.1
    Host: https://www.bling.com.br
    Content-Type: application/x-www-form-urlencoded
    Authorization: Basic [base64_das_credenciais_do_client_app]

    token=[ACCESS_OR_REFRESH_TOKEN]&token_type_hint=[access_token|refresh_token]&revoke_action=[logout|uninstall]&revoke_target=[user|company]

Parâmetro no body | Descrição  
---|---  
`revoke_action` | Define o tipo de revogação. Valores possíveis: `logout` ou `uninstall`. **Se não for informado** , apenas o token enviado na requisição será revogado.  
`revoke_target` | Define o alvo da revogação. Valores possíveis: `user` (padrão) ou `company`. **Se não for informado** , o padrão será `user` (revoga os tokens apenas do usuário relacionado ao token informado).  

### Exceções

#### Obtenção do authorization code

Neste tópico são citados alguns erros que poderão ocorrer na etapa de requisição do `authorization_code`. De modo geral, os erros serão retornados para a URL de redirecionamento informada no cadastro do aplicativo com a estrutura de parâmetros demonstrada na tabela abaixo.

Parâmetro | Descrição  
---|---  
`error` | O código do erro. Ex.: "invalid_request".  
`error_description` | Descrição sobre o erro.  
`error_uri` | Link contendo informações adicionais sobre o erro.  
`state` | Valor do parâmetro state informado na requisição.  

#### Aplicativo não autorizado

Caso o usuário não autorize o acesso aos escopos solicitados pelo aplicativo, o erro será retornado através da URL de redirecionamento do aplicativo.

    https://www.clientapp.com.br/callback?error=access_denied&error_description=[REDACTED]on&state=291e61b56ab3d845622cf137b1e1e2

#### Aplicativo inativado

Caso o aplicativo esteja inativado (conforme seção [situação do aplicativo](<https://developer.bling.com.br/homologacao#situa%C3%A7%C3%B5es>)) você não será capaz de realizar nenhum tipo de requisição. Um erro, como o do exemplo abaixo, será retornado através da URL de redirecionamento do aplicativo.

    https://www.clientapp.com.br/callback?error=app_inativo&error_description=[REDACTED]mente&state=291e61b56ab3d845622cf137b1e1e2

#### Usuário não autorizado

Exceções causadas por usuários não autorizados poderão ser redirecionadas para o _callback_ do aplicativo, veja o exemplo abaixo.

    https://www.clientapp.com.br/callback?error=UNAUTHORIZED_ERROR&error_description=O+usu%C3%A1rio+n%C3%A3o+possui+autoriza%C3%A7%C3%[REDACTED]s&state=xyz

Isso poderá ocorrer especificamente quando for requisitado um novo `authorization_code` para um usuário que já concedeu autorização previamente ao aplicativo. Porém, este usuário perdeu alguns privilégios durante este tempo (deixou de ter permissão para algum escopo solicitado na autorização) ou a conta passou para a situação inadimplente.

#### Obtenção da URL de redirecionamento

Ocorre geralmente quando o `client_id` da requisição for inválido.

### Exceções na obtenção dos tokens de acesso

O formato dos erros retornados durante esta requisição seguem o modelo adotado pela API v3 do Bling, um objeto JSON contendo as informações sobre o erro no _body_ da resposta HTTP.

Este tópico não é uma lista completa de todos os erros que poderão ocorrer durante a requisição dos _tokens_ de acesso, porém, a leitura deste manual poderá ajudar na interpretação da maioria dos erros.

#### Sintaxe

Independente do _grant type_ (`authorization_code` ou `refresh_token`) utilizado, os erros mais comuns durante esta etapa são causados por problemas na sintaxe da requisição. Os exemplos mais comuns são: ausência parâmetros obrigatórios no _body_ ou as credenciais no cabeçalho, _grant type_ inválido, credenciais inválidas, _code_ inexistente ou expirado.

Veja abaixo os objetos JSON retornados nas requisições com erro nas credenciais do aplicativo e `authorization_code` expirado.

    {
    	"error": {
    		"type": "invalid_client",
    		"message": "invalid_client",
    		"description": "The client credentials are invalid"
    	}
    }

    {
    	"error": {
    		"type": "invalid_grant",
    		"message": "invalid_grant",
    		"description": "The authorization code has expired"
    	}
    }

#### Authorization code já utilizado

É permitido que cada `authorization_code` seja utilizado apenas uma vez. Caso um `authorization_code` válido (não expirado) for utilizado em uma segunda requisição para obtenção dos _tokens_ de acesso, esta requisição não será válida e por medidas de segurança o usuário vinculado ao code terá o seu acesso revogado. Segue abaixo o JSON retornado neste caso.

    {
    	"error": {
    		"type": "VALIDATION_ERROR",
    		"message": "Invalid authorization code",
    		"description": "This authorization code has already been used, for security reasons the user has been revoked."
    	}
    }

#### Empresa inativa

Assim como não é permitida a geração de um novo `authorization_code` aos usuários vinculados a empresas com situação diferente de ativa, não será permitida a obtenção de novos _tokens_ de acesso com uso do `refresh token`. Nestes casos, o JSON abaixo será inserido no retorno.

    {
    	"error": {
    		"type": "UNAUTHORIZED_ERROR",
    		"message": "Empresa inativa",
    		"description": "A empresa vinculada ao token esta inativa."
    	}
    }

#### Obter recurso do usuário

O formato dos erros retornados durante esta requisição seguem o modelo adotado pela API v3 do Bling, um objeto JSON contendo as informações sobre o erro no _body_ da resposta HTTP.

Este tópico detalha os erros causados durante a validação do `access_token` utilizado na autenticação OAuth, não serão detalhados os demais erros que poderão ocorrer na requisição do recurso, para isso consulte o tópico sobre [erros da API v3](<https://developer.bling.com.br/erros-comuns#erros-comuns>).

#### Problemas de sintaxe

Qualquer problema com relação à sintaxe da inserção do [_access token_](<https://developer.bling.com.br/aplicativos#utilizando-o-access-token>) na requisição.

    {
    	"error": {
    		"type": "invalid_request",
    		"message": "invalid_request",
    		"description": "Malformed auth header"
    	}
    }

#### Token expirou

_Access token_ expirado.

    {
    	"error": {
    		"type": "invalid_token",
    		"message": "invalid_token",
    		"description": "The access token provided has expired"
    	}
    }

Utilize o `refresh token` para gerar uma nova chave a este usuário, veja o tópico [_refresh token_](<https://developer.bling.com.br/aplicativos#refresh-token>) para mais informações.

#### Token não autorizado

Caso o recurso requisitado não tenha sido autorizado pelo usuário, ou seja, o `access_token` não possui permissão para acessar o escopo referente a este recurso.

    {
    	"error": {
    		"type": "insufficient_scope",
    		"message": "insufficient_scope",
    		"description": "The request requires higher privileges than provided by the access token"
    	}
    }

## Gerenciamento

Através da aba [Minhas instalações](<https://bling.com.br/central.extensoes.php#/pages/minhas-instalacoes>) da Central de Extensões é possível gerenciar os aplicativos que foram autorizados a operar a conta.

Ao clicar sobre o menu de contexto de uma instalação, será possível reportá-lo, desinstalá-lo ou reautenticá-lo, caso os códigos de acesso tenham expirados e seja preciso autorizar o aplicativo novamente.