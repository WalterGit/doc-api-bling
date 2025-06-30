# Bling API

## Introdução

Bem-vindo ao Bling Developers!

Neste repositório você irá encontrar toda a documentação necessária para integrar com o Bling. Por meio da nossa API é possível consumir recursos do Bling para atender as necessidades da sua empresa/clientes. Estruturada no padrão REST, onde você poderá utilizar métodos GET, POST, PUT, PATCH e DELETE, por meio de autenticação OAuth 2.0. A organização dessa documentação contempla informações sobre o Bling, o conceito de API e como utilizá-la.

## Sobre o Bling

O Bling é um ERP que facilita a emissão de notas fiscais e boletos, além de realizar integrações nativas com plataformas de e-commerce, marketplaces e logísticas, tais como por API.

Com o Bling é possível gerenciar todo o processo de compra e venda dos produtos de maneira facilitada, bem como possuir relatórios que auxiliam na análise e gestão empresarial.

## O que é API

API (_Application Programming Interface_) é um conjunto de protocolos e ferramentas que facilitam a integração entre softwares e permitem que uma solução se comunique com outros produtos e serviços sem precisar acessar a interface gráfica da solução diretamente, tudo isso através do que chamamos de interface.

O intuito de uma API é a troca de dados entre sistemas implementados em diferentes tecnologias que utilizam o mesmo protocolo de comunicação.

No Bling, usamos a API para integrar as nossas soluções com nossos parceiros, sendo possível criar processos de automatização, atualização ou análise de registros, criação de novos aplicativos e uma vasta gama de soluções podem ser criadas para facilitar a vida dos nossos clientes.

## Para quem é destinada a API

A API é pública e está disponível para quem deseja estender as funcionalidades já existentes no Bling, podendo criar plugins ou componentes em sistemas próprios.

A utilização da API permite a realização de operações de forma independente, visto que os recursos do Bling serão controlados pelo cliente da API, podendo utilizar a API para implementar soluções próprias.

## Padrão REST

No Bling, usamos um padrão de arquitetura para a API chamado de REST (_Representational State Transfer_).

O REST ignora os detalhes da implementação do componente e a sintaxe de protocolo visando focar nos papéis dos componentes, nas restrições sobre sua interação e na sua interpretação de elementos de dados significativos. Ou seja, o usuário deve fazer uma requisição HTTP para algum _endpoint_ disponível para solicitar, enviar ou modificar dados do sistema, então o _endpoint_ de API transfere uma informação do estado do recurso ao solicitante. Essa informação é entregue via HTTP utilizando um formato de mensagem do tipo JSON.

Exemplo de requisição, abaixo:

`GET https://api.bling.com.br/Api/v3/produtos`

Resposta do servidor:

    {
        data: {
            id: 1,
            nome: ‘Caderno universitário, 100 Folhas’
        }
    }

Cada requisição consiste em um método HTTP, um Header, uma URI e um Body que são explicados a seguir:

O método HTTP diferencia a ação que o usuário deseja realizar pela API, sendo eles:

  * **GET** : Ação para obter uma ou mais entidades
  * **POST** : Ação para criar uma entidade ou executar uma ação
  * **PUT** : Ação para atualizar todos os dados de uma entidade
  * **PATCH** : Ação para atualizar parcialmente os dados de uma entidade
  * **DELETE** : Ação para remover uma entidade

**Header** : É o cabeçalho da requisição, as informações enviadas no _header_ podem ser utilizadas para o servidor interpretar a requisição. Exemplo: `Content-Type: application/json`

**URI** : Define o caminho onde a requisição irá ocorrer, por exemplo, em uma requisição para obtenção dos dados de produtos, a URI seria: `/Api/v3/produtos`.

**Body** : É o corpo da requisição, nele são informados os dados que serão enviados para o sistema e também são retornadas as informações da resposta de uma requisição.