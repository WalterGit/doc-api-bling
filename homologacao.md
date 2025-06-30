# Homologação

## Inscrição

Caso você ainda não possua uma conta no Bling [clique aqui](<https://www.bling.com.br/inscricao/plano-cobalto>) e faça a sua inscrição.

## Processo

O processo de homologação é destinado a aplicativos com [visibilidade](<https://developer.bling.com.br/aplicativos#visibilidade>) pública, realizando integração com clientes do Bling.

A primeira etapa consiste na [revisão](<homologacao#revis%C3%A3o>) do uso da API. Após, é possível solicitar a revisão do aplicativo, onde os itens serão validados pela nossa equipe técnica conforme as regras descritas na seção [validação de dados](<https://developer.bling.com.br/homologa%C3%A7%C3%A3o#valida%C3%A7%C3%A3o-de-dados>).

## Validação de dados

**❌ Exemplo incorreto:**

**✅ Exemplo correto:**

**Logo** : Deve ser condizente com a aplicação desenvolvida.

**Nome do aplicativo** : Nome que será exibido para os clientes do Bling.

**Descrição** : Descrição clara e objetiva da solução proposta pelo seu aplicativo/plataforma.

**Categoria** : Deve ser condizente com a solução proposta, assim o cliente poderá encontrar o seu aplicativo facilmente.

**URI de redirecionamento** : Conforme o [fluxo de autorização](<https://developer.bling.com.br/aplicativos#fluxo-de-autoriza%C3%A7%C3%A3o>), espera-se que, ao trocar o `authorization_code` pelo `access_token`, haja uma interface amigável para o usuário, tanto nos casos de sucesso quanto de erro. Esse fluxo ininterrupto facilita a experiência do usuário e a integração entre o seu aplicativo e o Bling.

**URI da homepage** : Recomenda-se que a página disponível pela URI possua uma descrição mais detalhada da solução que o aplicativo oferece, auxiliando, também, a promover e converter novos clientes. Aconselha-se que não necessite de autenticação para acessá-la.

**Escopos** : Os escopos selecionados devem possuir relação com a finalidade do aplicativo.   

_Os itens apresentados acima são essencialmente utilizados na revisão dos dados cadastrados. No entanto, atente-se para a criação de um serviço seguro e bem otimizado. Qualquer indício de problema que possa prejudicar os nossos usuários fará com que o aplicativo seja inativado._

## Revisão

### Introdução

Para iniciar o processo de revisão do aplicativo, acesse a aba "Homologação".

Após confirmar o preenchimento dos dados, uma interface para acompanhar o processo será exibida. Caso ocorram inconsistências, elas serão exibidas e será necessário iniciar a revisão novamente.

Já, se o teste for bem sucedido, será possível solicitar a revisão do aplicativo para a nossa equipe técnica.

### Execução

O objetivo é validar o correto uso da API, através da execução de _requests_ sequenciais para a [API de homologação](<referencia#/Homologa%C3%A7%C3%A3o>).

Em uma das etapas será invalidado o _access token_ , nesse caso, utilize o [refresh token](<aplicativos#refresh-token>).

A cada _request_ realizado, será retornado no _header_ um `hash` que deve ser informado no _header_ do passo seguinte.

Exemplo de retorno do _header_ :

`x-bling-homologacao: [REDACTED]Y/c=`

**1.** O primeiro _request_ deve ser feito para obter os dados que serão utilizados para o segundo _request_ , utilizando o método `GET`.

`GET https://api.bling.com.br/Api/v3/homologacao/produtos`

Exemplo de resposta:

    {
    	"data": {
    		"nome": "Copo do Bling",
    		"preco": 32.56,
    		"codigo": "COD-4587"
    	}
    }

**2.** Realize o _request_ para o _endpoint_ de método `POST` informando, no _body_ da requisição, os dados contidos na propriedade `data`, obtidos no primeiro passo. Será retornado o `id` do produto "criado", lembrando que o `id` é apenas para representar um novo produto.

`POST https://api.bling.com.br/Api/v3/homologacao/produtos`

Exemplo do _body_ :

    {
    	"nome": "Copo do Bling",
    	"preco": 32.56,
    	"codigo": "COD-4587"
    }

Exemplo de resposta:

    {
    	"data": {
    		"nome": "Copo do Bling",
    		"preco": 32.56,
    		"codigo": "COD-4587",
    		"id": 16842381880
    	}
    }

**3.** Após criar o produto, realize a alteração do atributo `descricao` para "Copo". Para isso utilize o método `PUT`, informando no _path_ o `id` do produto obtido no passo anterior e no _body_ informe os dados atualizados do produto.

`PUT https://api.bling.com.[REDACTED]80`

Exemplo do _body_ :

    {
    	"nome": "Copo",
    	"preco": 32.56,
    	"codigo": "COD-4587"
    }

**4.** Altere a situação do produto utilizando o método `PATCH`. A situação do produto deve ser informada no _body_.

`PATCH https://api.bling.com.[REDACTED]80/situacoes`

Exemplo do _body_ :

    {
    	"situacao": "I"
    }

**5.** Por fim, remova o produto por meio do método `DELETE`.

`DELETE https://api.bling.com.[REDACTED]80`

### Limites

O tempo total do teste deve ser de no máximo 10 segundos.

O limite entre cada requisição é de 2 segundos.

Caso o limite seja atingido, revise a implementação e refaça a operação.

## Situações

As 5 situações de um aplicativo público são:

  * **Em desenvolvimento** : Ao salvar um aplicativo de visibilidade pública, no momento da criação, ele será salvo nessa situação.

  * **Em revisão** : Após o aplicativo estar desenvolvido e pronto para operar contas do Bling, na edição do aplicativo clique em "Solicitar revisão". Após, nossa equipe técnica fará a revisão.

  * **Aprovado** : Caso não haja incoerência, o aplicativo será aprovado.

  * **Rejeitado** : Havendo inconsistência no aplicativo, ele será rejeitado durante a fase de revisão. Se isso acontecer, você será notificado e os motivos da rejeição serão apresentados na edição do aplicativo. Realize os ajustes e salve o aplicativo, nesse momento uma nova revisão será solicitada. Durante a fase de rejeição o aplicativo funcionará como na fase de revisão.

  * **Inativado** : Caso sejam identificados ou reportados abusos, o aplicativo poderá ser inativado. Será notificado o problema encontrado e o aplicativo terá todos os tokens de acesso revogados. Para poder reativar o seu aplicativo, será necessário entrar em contato com a nossa equipe.

Se a situação do aplicativo for alterada, você será notificado no Bling. Caso a situação tenha sido alterada para rejeitado ou inativado, o motivo será informado na tela de edição do aplicativo.