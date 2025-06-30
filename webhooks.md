# Webhooks

## Introdução

_Webhook_ é um método de comunicação utilizado para que aplicativos e sistemas se comuniquem em tempo real de forma reativa e acontece sempre que um evento específico ocorre em uma das aplicações.

Para exemplificar o uso de _webhooks_ , imagine que, a cada produto cadastrado, atualizado ou excluído no Bling, seja necessário realizar a mesma operação em outro sistema. Em vez de criar uma rotina que periodicamente consulte a API do Bling para verificar alterações, é possível configurar _webhooks_ para que sejam acionados automaticamente a cada uma dessas ações. Dessa forma, o sistema receberá os dados em tempo real, processará as informações necessárias e evitará o uso de rotinas automáticas que demandem consultas constantes ao Bling.

## Como cadastrar

  1. Acesse o aplicativo já [cadastrado](<https://developer.bling.com.br/aplicativos#como-cadastrar>).

  2. Certifique-se que o aplicativo possua os escopos referentes aos [recursos](<https://developer.bling.com.br/webhooks#recursos>) aos quais queira ser notificado. Caso o aplicativo não possua um escopo específico, o recurso de webhook correspondente não será exibido para configurar.

  3. Navegue até a aba "Webhooks".

  4. Configure os servidores que receberão os eventos.

  5. Configure os recursos que deseja receber as notificações.

  * Selecione o servidor que deseja receber o evento.
  * Marque as [ações](<https://developer.bling.com.br/webhooks#a%C3%A7%C3%B5es>) que deseja ser notificado.
  * Selecione a versão do _payload_ conforme a [estrutura de retorno](<https://developer.bling.com.br/webhooks#estrutura-de-retorno>).

  6. Salve as alterações.

## Webhooks vs Polling

### Atualização de informações

Webhooks e _polling_ são duas técnicas amplamente utilizadas para integração de sistemas e comunicação entre aplicações. Ambos os métodos têm como objetivo transferir informações entre sistemas, mas funcionam de maneira fundamentalmente diferente. A escolha entre _webhooks_ e _polling_ depende do caso de uso, das demandas de desempenho e das restrições do sistema.

### Webhooks

Webhooks são uma abordagem baseada em eventos, onde um servidor é configurado para enviar notificações para outro sistema sempre que um determinado evento ocorre. Isso é feito através de requisições HTTP para um _endpoint_ previamente definido. O uso de _webhooks_ reduz a sobrecarga de requisições desnecessárias, enviando apenas quando há dados novos.

### Polling

_Polling_ é uma técnica onde um sistema consulta periodicamente o servidor de origem para verificar se há novos dados ou atualizações. Nesse modelo, o cliente faz requisições repetitivas, independentemente de haver ou não dados novos. Em relação ao _webhook_ , é menos eficiente, visto que podem ser realizadas muitas requisições sem dados novos.

## Autenticação

### Técnica

A autenticação das mensagens enviadas pelo Bling deve ser realizada por meio do cabeçalho HTTP `X-Bling-Signature-256`. Esse cabeçalho contém um _hash_ de autenticação HMAC (Hash-Based Message Authentication Code) composto pelo _payload_ JSON da resposta e o _client secret_ do aplicativo. Esse processo garante a integridade e a autenticidade dos dados enviados pelo Bling.

### Validação do hash

Para garantir que a mensagem recebida é legítima e não foi manipulada, considere os seguintes passos:

  1. Gerar um _hash_ HMAC utilizando o _payload_ e o _client secret_ do aplicativo.
  2. Comparar se o _hash_ informado no _header_ `X-Bling-Signature-256` é igual ao _hash_ gerado.

Exemplo de _hashes_ :

  * _Hash_ gerado: `[REDACTED]ffc25e08ba9db4ab35515516`
  * _Header_ informado na requisição: `sha256=[REDACTED]ffc25e08ba9db4ab35515516`

Observações:

  * O Bling usa um código _hash_ hexadecimal HMAC para calcular o _hash_.
  * A assinatura do _hash_ sempre começa com `sha256=`.
  * O padrão de codificação utilizado é o UTF-8.

## Idempotência

Idempotência é a capacidade de uma operação retornar o mesmo resultado, independentemente de quantas vezes seja executada, desde que os parâmetros sejam os mesmos.

No contexto de _webhooks_ , caso o Bling envie o mesmo _webhook_ duas vezes, sua aplicação deve responder a ambas as requisições com um código HTTP `2xx`.

## Entrega não ordenada

Não há garantia da entrega dos eventos na ordem em que foram gerados. Por exemplo, um _webhook_ de atualização de produto pode ser recebido antes que o _webhook_ de criação deste mesmo produto.

Uma prática recomendada para lidar com esse cenário é gerenciar os _webhooks_ recebidos de maneira assíncrona, usando filas, por exemplo.

## Retentativas

O processo de retentativas foi projetado para garantir a entrega confiável de _webhooks_ aos integradores, mesmo diante de falhas temporárias no sistema de destino. Serão feitas tentativas no período máximo de 3 dias onde, a cada retentativa, o tempo da próxima retentativa poderá ser maior. Ao final do processo de retentativas, caso o processamento do evento continue com problemas, a configuração do _webhook_ para o recurso em questão será desabilitada e o Bling não enviará novos eventos até que a configuração seja habilitada manualmente através das configurações de _webhooks_ do aplicativo.

Uma requisição é considerada entregue com sucesso quando o integrador responde com um código HTTP `2xx` em até **5** segundos. Caso exceda o tempo de resposta ou o código for diferente de `2xx` serão feitas as retentativas no envio da mensagem.

## Ações

Abaixo estão detalhadas as ações disponíveis:

  * `created`: Ocorre quando um recurso é criado.
  * `updated`: Ocorre quando um recurso é atualizado.
  * `deleted`: Ocorre quando um recurso é deletado definitivamente. 
    * Alterar a situação de um recurso para excluído gera um evento de `updated`.

## Recursos

### Recursos disponíveis

Antes de configurar um recurso de _webhook_ , é necessário adicionar o escopo referente ao recurso aos dados básicos do aplicativo.

  * Pedido de Venda: `order`
  * Produto: `product`
  * Estoque: `stock`
  * Produto fornecedor: `product_supplier`
  * Nota fiscal: `invoice`
  * Nota fiscal de consumidor: `consumer_invoice`

**Obs: Atualmente, webhooks de estoque notificam somente operações transacionais. A liberação da notificação de atualizações de _estoque virtual_ está prevista para versões futuras.**

### Estrutura de retorno

    {
    	"eventId": "01945027-150e-72b4-e7cf-4943a042cd9c",
    	"date": "2025-01-10T12:18:46Z",
    	"version": "v1",
    	"event": "$resource.$action",
    	"companyId": "[REDACTED]",
    	"data": $payload
    }

Detalhamento dos campos:

  * `eventId`: Identificador único do evento.
  * `date`: Data no formato ISO 8601.
  * `version`: Versão do webhook.
  * `event`: Recurso junto a ação separados por "`.`".
  * `companyId`: ID da empresa. 
    * Para obtê-lo, consulte os [dados básicos](<https://developer.bling.com.br/referencia#/Empresas/get_empresas_me_dados_basicos>) da empresa por API.
  * `data`: _Payload_ do evento.

Considere:

  * `$resource`: O [recurso](<https://developer.bling.com.br/webhooks#recursos>) do _webhook_.
  * `$action`: A [ação](<https://developer.bling.com.br/webhooks#a%C3%A7%C3%B5es>) do _webhook_.
  * `$payload`: Uma das estruturas abaixo, conforme o recurso e a ação do _webhook_.

### Pedido de venda

Estrutura dos _payloads_ dos _webhooks_ de pedido de venda:

#### Versão 1

Created | Updated | Deleted  
---|---|---  

    {
      "id": 12345678,
      "data": "2024-09-25",
      "numero": 123,
      "numeroLoja": "Loja_123",
      "total": 123.45,
      "contato": {
        "id": 12345678
      },
      "vendedor": {
        "id": 12345678
      },
      "loja": {
        "id": 12345678
    	}
    }

| 

    {
      "id": 12345678,
      "data": "2024-09-25",
      "numero": 123,
      "numeroLoja": "Loja_123",
      "total": 123.45,
      "contato": {
        "id": 12345678
      },
      "vendedor": {
        "id": 12345678
      },
      "loja": {
        "id": 12345678
      }
    }

| 

    {
      "id": 12345678
    }

### Produto

Estrutura dos _payloads_ dos _webhooks_ de produto:

#### Versão 1

**Created** | **Updated** | **Deleted**  
---|---|---  

    {
      "id": 12345678,
      "nome": "Copo do Bling",
      "codigo": "COD-4587",
      "tipo": "P",
      "situacao": "A",
      "preco": 4.99,
      "unidade": "UN",
      "formato": "S",
      "idProdutoPai": 12345678,
      "categoria": {
        "id": 12345679
      }
    }

| 

    {
      "id": 12345678,
      "nome": "Copo do Bling",
      "codigo": "COD-4587",
      "tipo": "P",
      "situacao": "A",
      "preco": 4.99,
      "unidade": "UN",
      "formato": "S",
      "idProdutoPai": 12345678,
      "categoria": {
        "id": 12345679
      }
    }

| 

    {
      "id": 12345678
    }

### Estoque

Estrutura dos _payloads_ dos _webhooks_ de estoque:

#### Versão 1

**Created** | **Updated** | **Deleted**  
---|---|---  

    {
      "produto": {
        "id": 12345678
      },
      "deposito": {
        "id": 12345678,
        "saldoFisico": 1250.75,
        "saldoVirtual": 1250.75
      },
      "operacao": "E",
      "quantidade": 25,
      "saldoFisicoTotal": 1500.75,
      "saldoVirtualTotal": 1500.75
    }

| 

    {
      "produto": {
        "id": 12345678
      },
      "deposito": {
        "id": 12345678,
        "saldoFisico": 1250.75,
        "saldoVirtual": 1250.75
      },
      "operacao": "E",
      "quantidade": 26,
      "saldoFisicoTotal": 1500.75,
      "saldoVirtualTotal": 1500.75
    }

| 

    {
      "produto": {
        "id": 12345678
      },
      "deposito": {
        "id": 12345678,
        "saldoFisico": 1250.75,
        "saldoVirtual": 1250.75
      },
      "saldoFisicoTotal": 1500.75,
      "saldoVirtualTotal": 1500.75
    }

### Produto fornecedor

Estrutura dos _payloads_ dos _webhooks_ de produto fornecedor:

#### Versão 1

**Created** | **Updated** | **Deleted**  
---|---|---  

    {
      "id": 12345678,
      "descricao": "Copo do Bling",
      "codigo": "COD-123",
      "precoCusto": 3.9,
      "precoCompra": 3.5,
      "padrao": false,
      "garantia": 3,
      "produto": {
        "id": 12345678
      },
      "fornecedor": {
        "id": 12345678
      }
    }

| 

    {
      "id": 12345678,
      "descricao": "Copo do Bling",
      "codigo": "COD-123",
      "precoCusto": 3.9,
      "precoCompra": 3.5,
      "padrao": true,
      "garantia": 5,
      "produto": {
        "id": 12345678
      },
      "fornecedor": {
        "id": 12345678
      }
    }

| 

    {
      "id": 12345678
    }

### Nota fiscal eletrônica e de consumidor

Estrutura dos _payloads_ dos _webhooks_ de nota fiscal eletrônica e de consumidor:

#### Versão 1

Created | Updated | Deleted  
---|---|---  

    {
      "id": 12345678,
      "tipo": 1,
      "situacao": 1,
      "numero": "1234",
      "dataEmissao": "2024-09-27 11:24:56",
      "dataOperacao": "2024-09-27 11:00:00",
      "contato": {
        "id": 12345678
      },
      "naturezaOperacao": {
        "id": 12345678
      },
      "loja": {
        "id": 12345678
      }
    }

| 

    {
      "id": 12345678,
      "tipo": 1,
      "situacao": 1,
      "numero": "1234",
      "dataEmissao": "2024-09-27 11:24:56",
      "dataOperacao": "2024-09-27 11:00:00",
      "contato": {
        "id": 12345678
      },
      "naturezaOperacao": {
        "id": 12345678
      },
      "loja": {
        "id": 12345678
      }
    }

| 

    {
      "id": 12345678
    }

### Exemplo de retorno

Para exemplicicar, conforme a [estrutura de retorno](<https://developer.bling.com.br/webhooks#estrutura-de-retorno>), em uma [ação](<https://developer.bling.com.br/webhooks#a%C3%A7%C3%B5es>) de atualização no [recurso](<https://developer.bling.com.br/webhooks#recursos>) de produtos, teríamos o seguinte _payload_ :

    {
    	"eventId": "01945027-150e-72b4-e7cf-4943a042cd9c",
    	"date": "2025-01-10T12:18:46Z",
    	"version": "v1",
    	"event": "product.updated",
    	"companyId": "[REDACTED]",
    	"data": {
    		"id": 12345678,
    		"nome": "Copo do Bling",
    		"codigo": "COD-4587",
    		"tipo": "P",
    		"situacao": "A",
    		"preco": 4.99,
    		"unidade": "UN",
    		"formato": "S",
    		"idProdutoPai": 12345678,
    		"categoria": {
    			"id": 12345679
    		}
    	}
    }