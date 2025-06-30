# Migração API v2/v3

Alterações mapeadas até o dia 15 de abril de 2024. Para acompanhamento de novos updates, acesse o [changelog](<https://developer.bling.com.br/changelogs>).

# 🔐 Autenticação

Uma das maiores mudanças entre as versões das APIs foi a maneira como a autenticação é realizada:

API v2 | API v3  
---|---  
Autenticação via API key. | Autenticação pelo protocolo OAuth 2.0.  
Geração de usuário API na conta do cliente. | Criação de um aplicativo na conta do desenvolvedor.  
Encaminhamento manual da API key gerada para o integrador. | Instalação (autorização) do aplicativo na conta do cliente Bling.  
Chave estática e imutável. | Controle por tokens não visíveis a nível de interface e com tempos de expiração.  

Para mais informações sobre a autenticação na API v3, acesse [aqui](<https://developer.bling.com.br/autenticacao#fundamentos>).

## 🗂️ Padronização na identificação das rotas

Descrição | API v2 | API v3  
---|---|---  
Borderôs | /bordero | /borderos  
Campos customizados | /camposcustomizados | /campos-customizados  
Categorias de produtos | /categorias e /categoria | /categorias/produtos  
Categorias de lojas | /categoriasLojas | /categorias/lojas  
Contatos | /contatos e /contato | /contatos  
Contas a pagar | /contaspagar e /contapagar | /contas/pagar  
Contas a receber | /contasreceber e /contareceber | /contas/receber  
Contratos | /Contratos e /Contrato | /contratos  
Depósitos | /depositos e /deposito | /depositos  
Formas de pagamento | /formaspagamento | /forma-pagamentos  
NFC-e | /nfces e /nfce | /nfce  
NFS-e | /notasservico | /nfse  
NF-e | /notasfiscais e /notafiscal | /nfe  
Ordens de produção | /ordensproducao | /ordens-producao  
Pedidos de compra | /pedidoscompra e /pedidocompra | /pedidos/compras  
Pedidos de venda | /pedidos e /pedido | /pedidos/vendas  
Produtos | /produtos e /produto | /produtos  
Produtos fornecedores | /produtosfornecedores e /produtofornecedor | /produtos/fornecedores  
Produtos lojas | /produtoLoja | /produtos/lojas  
Situações | /situacao | /situacoes  

## 🔎 Obtenção de dados

  * A obtenção de múltiplos registros retorna informações sucintas da entidade. Para obter informações completas, utilize os métodos individuais.
  * O ID (identificador único no Bling) se tornou o parâmetro padrão para obtenção individual das entidades.

## 🖇️ Segmentação de resources

Criação de endpoints específicos, dentro de um módulo ou associado, com objetivo organizacional e estrutural:

Descrição | API v2 | API v3  
---|---|---  
Produtos | /produtos | /produtos   
/produtos/estruturas   
/produtos/variacoes   
/estoques - obtenção, criação e atualização  
Situações | /situacao | /situacoes   
/situacoes/modulos   
/situacoes/transicoes  
Logísticas | /logistica/servicos   
/logistica/evento   
/logistica/rastreamento | /logisticas   
/logisticas/etiquetas   
/logisticas/objetos   
/logisticas/remessas   
/logisticas/servicos  

## ✨ Adição/alteração de endpoints

A seguir, são exibidas as alterações de endpoints entre versões. Entretanto, alguns comportamentos foram alterados e não necessariamente um endpoint será operado na v3 da mesma forma que era na v2. Para os detalhes de cada endpoint, será necessário analisar a [documentação completa](<https://developer.bling.com.br/referencia>).

### Borderôs

Endpoint | API v2 | API v3  
---|---|---  
DELETE | /bordero/{id} | /borderos/{idBordero}  
GET individual | ❌ | /borderos/{idBordero}  

### Campos Customizados

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /campos-customizados/{idCampoCustomizado}  
GET | ❌ | /campos-customizados/modulos   
/campos-customizados/tipos   
/campos-customizados/modulos/{idModulo}  
GET individual | /camposcustomizados/{módulo} | /campos-customizados/{idCampoCustomizado}  
PATCH | ❌ | /campos-customizados/{idCampoCustomizado}/situacoes  
POST | ❌ | /campos-customizados  
PUT | ❌ | /campos-customizados/{idCampoCustomizado}  

### Categorias de Produtos

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /categorias/produtos/{idCategoriaProduto}  
GET all | /categorias | /categorias/produtos  
GET individual | /categoria/{idCategoria} | /categorias/produtos/{idCategoriaProduto}  
POST | /categoria | /categorias/produtos  
PUT | /categoria/{idCategoria} | /categorias/produtos/{idCategoriaProduto}  

### Categorias de Lojas

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /categorias/lojas/{idCategoriaLoja}  
GET vínculo de categoria por loja | /categoriasLoja/{idLoja} | /categorias/lojas  
GET vínculo de categoria por loja e categoria | /categoriasLoja/{idLojas}/{idCategoria} | /categorias/lojas/{idCategoriaLoja}  
POST | /categoriasLoja/{idLoja} | /categorias/lojas  
PUT | /categoriasLoja/{idLoja}/{idCategoria} | /categorias/lojas/{idCategoriaLoja}  

### Contatos

Endpoint | API v2 | API v3  
---|---|---  
DELETE individual | ❌ | /contatos/{idContato}  
DELETE múltiplos | ❌ | /contatos  
GET all | /contatos | /contatos  
GET individual | /contato/{identificador} | /contatos/{idContato}  
GET por tipo de contato | ❌ | /contatos/{idContato}/tipos  
GET Consumidor Final | ❌ | /contatos/consumidor-final  
PATCH | ❌ | /contatos/{idContato}/situacoes  
POST | /contato | /contatos  
POST atualização da situação de múltiplos | ❌ | /contatos/situacoes  
PUT | /contato/{id} | /contatos/{idContato}  

### Contas a Pagar

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /contas/pagar/{idContaPagar}  
GET all | /contaspagar | /contas/pagar  
GET individual | /contapagar/{id} | /contas/pagar/{idContaPagar}  
POST | /contapagar | /contas/pagar  
POST recebimento de uma conta | ❌ | /contas/pagar/{idContaPagar}/baixar  
PUT | /contapagar/{id} | /contas/pagar/{idContaPagar}  

### Contas a Receber

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /contas/receber/{idContaReceber}  
GET all | /contasreceber | /contas/receber  
GET individual | /contareceber/{id} | /contas/receber/{idContaReceber}  
POST | /contareceber | /contas/receber  
POST recebimento de uma conta | ❌ | /contas/receber/{idContaReceber}/baixar  
PUT | /contareceber/{id} | /contas/receber/{idContaReceber}  

### Depósitos

Endpoint | API v2 | API v3  
---|---|---  
GET all | /depositos | /depositos  
GET individual | /deposito/{idDeposito} | /depositos/{idDeposito}  
POST | /deposito | /depositos  
PUT | /deposito/{idDeposito} | /depositos/{idDeposito}  

### Formas de Pagamento

Endpoint | API v2 | API v3  
---|---|---  
DELETE | /formapagamento | /formas-pagamentos/{idFormaPagamento}  
GET all | /formapagamento | /formas-pagamentos  
GET individual | /formapagamento/{id} | /formas-pagamentos/{idFormaPagamento}  
POST | /formapagamento | /formas-pagamentos  
PUT | /formapagamento/{id} | /formas-pagamentos/{idFormaPagamento}  

### Ordens de Produção

Endpoint | API v2 | API v3  
---|---|---  
DELETE | /ordemproducao | /ordens-producao/{idOrdemProducao}  
GET all | /ordensproducao | /ordens-producao  
GET individual | /ordemproducao/{numero} | /ordens-producao/{idOrdemProducao}  
POST | /ordemproducao | /ordens-producao  
POST gerar sob demanda | /ordensproducaogeracao | /ordens-producao/gerar-sob-demanda  
PUT | ❌ | /ordens-producao/{idOrdemProducao}  
PUT situação | ❌ | /ordens-producao/{idOrdemProducao}/situacoes  

### NFC-e

Endpoint | API v2 | API v3  
---|---|---  
GET all | /nfces | /nfce  
GET individual | /nfce/{numero}/{serie} | /nfce/{idNotaFiscalConsumidor}  
POST | /nfce | /nfce  
POST autorização da nota | /nfce/{numero}/{serie} | /nfce/{idNotaFiscalConsumidor}/enviar  
POST lançamento de estoque | ❌ | /nfce/{idNotaFiscalConsumidor}/lancar-estoque  
POST lançamento de estoque por depósito | ❌ | /nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}  
POST estorno de estoque | ❌ | /nfce/{idNotaFiscalConsumidor}/estornar-estoque  
POST lançamento de contas | ❌ | /nfce/{idNotaFiscalConsumidor}/lancar-contas  
POST estorno de contas | ❌ | /nfce/{idNotaFiscalConsumidor}/estornar-contas  
PUT | ❌ | /nfce/{idNotaFiscalConsumidor}  

### NFS-e

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /nfse/{idNotaServico}  
GET all | /notasservico | /nfse  
GET individual | /notaservico/{numero} | /nfse/{idNotaServico}  
GET configurações de nota | ❌ | /nfse/configuracoes  
POST | /notaservico | /nfse  
POST autorização de nota | /notaservico/{numero}/{serie} | /nfse/{idNotaServico}/enviar  
POST cancelamento de nota | ❌ | /nfse/{idNotaServico}/cancelar  
PUT configurações de nota | ❌ | /nfse/configuracoes  

### NF-e

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /nfe  
GET all | /notasfiscais | /nfe  
GET individual | /notafiscal/{numero}/{serie} | /nfe/{idNotaFiscal}  
POST | /notafiscal | /nfe  
POST autorização da nota | /notafiscal/{numero}/{serie} | /nfe/{idNotaFiscal}/enviar  
POST lançamento de estoque | ❌ | /nfe/{idNotaFiscal}/lancar-estoque  
POST lançamento de estoque por depósito | ❌ | /nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}  
POST estorno de estoque | ❌ | /nfe/{idNotaFiscal}/estornar-estoque  
POST lançamento de contas | ❌ | /nfe/{idNotaFiscal}/lancar-contas  
POST estorno de contas | ❌ | /nfe/{idNotaFiscal}/estornar-contas  
PUT | ❌ | /nfe/{idNotaFiscal}  

### Pedidos de Compra

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /pedidos/compras/{idPedidoCompra}  
GET all | /pedidoscompra | /pedidos/compras  
GET individual | /pedidocompra/{numero} | /pedidos/compras/{idPedidoCompra}  
POST | /pedidocompra | /pedidos/compras  
POST lançar estoque | ❌ | /pedidos/compras/{idPedidoCompra}/lancar-estoque  
POST estornar estoque | ❌ | /pedidos/compras/{idPedidoCompra}/estornar-estoque  
POST lançar contas | ❌ | /pedidos/compras/{idPedidoCompra}/lancar-contas  
POST estornar contas | ❌ | /pedidos/compras/{idPedidoCompra}/estornar-contas  
PUT | ❌ | /pedidos/compras/{idPedidoCompra}  
PUT situação | /pedidocompra/{numero} | **PATCH** /pedidos/compras/{idPedidoCompra}/situacoes  

### Pedidos de Venda

Endpoint | API v2 | API v3  
---|---|---  
DELETE individual | ❌ | /pedidos/vendas/{idPedidoVenda}  
DELETE múltiplos | ❌ | /pedidos/vendas  
GET all | /pedidos | /pedidos/vendas  
GET individual | /pedido/{numero} | /pedidos/vendas/{idPedidoVenda}  
POST | /pedido | /pedidos/vendas  
POST geração NF-e | ❌ | /pedidos/vendas/{idPedidoVenda}/gerar-nfe  
POST geração NFC-e | ❌ | /pedidos/vendas/{idPedidoVenda}/gerar-nfce  
POST lançar estoque | ❌ | /pedidos/vendas/{idPedidoVenda}/lancar-estoque  
POST lançamento de estoque por depósito | ❌ | /pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}  
POST estornar estoque | ❌ | /pedidos/vendas/{idPedidoVenda}/estornar-estoque  
POST lançar contas | ❌ | /pedidos/vendas/{idPedidoVenda}/lancar-contas  
POST estornar contas | ❌ | /pedidos/vendas/{idPedidoVenda}/estornar-contas  
PUT | ❌ | /pedidos/vendas/{idPedidoVenda}  
PUT situação | /pedido/{numero} | **PATCH** /pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}  

### Produtos

Endpoint | API v2 | API v3  
---|---|---  
DELETE individual | /produto | /produtos/{idProduto}  
DELETE múltiplos | ❌ | /produtos  
GET all | /produtos | /produtos  
GET individual | /produto/{codigo} | /produtos/{idProduto}  
GET por fornecedor (código e ID) | /produto/{codigo}/{id_fornecedor} | /produtos/fornecedores/{idProdutoFornecedor}  
PATCH situação de produto | ❌ | /produtos/{idProduto}/situacoes  
POST | /produto | /produtos  
POST atualização de produto | /produto/{codigo} | **PUT** /produtos/{idProduto}  
POST atualização de situações | ❌ | /produtos/situacoes  

### Produtos Fornecedores

Endpoint | API v2 | API v3  
---|---|---  
GET all | /produtosfornecedores | /produtos/fornecedores  
GET individual | /produtofornecedor/{id} | /produtos/fornecedores/{idProdutoFornecedor}  
PATCH | ❌ | /produtos/fornecedores/{idProdutoFornecedor}  
POST | /produtofornecedor/{id} | /produtos/fornecedores  
PUT | /produtofornecedor | /produtos/fornecedores/{idProdutoFornecedor}  

### Produtos Lojas

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /produtos/lojas/{idProdutoLoja}  
GET all | ❌ | /produtos/lojas  
GET individual | /produto/{codigo} - parâmetro loja | /produtos/lojas/{idProdutoLoja}  
POST | /produtoLoja/{idLoja}/{codigo} | /produtos/lojas  
PUT | /produtoLoja/{idLoja}/{codigo} | /produtos/lojas/{idProdutoLoja}  

### Situações

Para ver todos os resources novos, acesse a [segmentação](<https://developer.bling.com.br/migracao-v2-v3#%F0%9F%96%87%EF%B8%8F-segmenta%C3%A7%C3%A3o-de-resources>).

Endpoint | API v2 | API v3  
---|---|---  
GET all | ❌ | /situacoes/modulos  
GET individual | /situacao/{módulo} | /situacoes/modulos/{idModuloSistema}  
GET ações | ❌ | /situacoes/modulos/{idModuloSistema}/acoes  
GET transições | ❌ | /situacoes/modulos/{idModuloSistema}/acoes  

### Logísticas

Para ver todos os resources novos, acesse a [segmentação](<https://developer.bling.com.br/migracao-v2-v3#%F0%9F%96%87%EF%B8%8F-segmenta%C3%A7%C3%A3o-de-resources>).

#### Serviços

Endpoint | API v2 | API v3  
---|---|---  
GET all | /logisticas/servicos | /logisticas/servicos  
GET individual | /logistica/{id}/servicos | /logisticas/servicos/{idLogisticaServico}  
PATCH | ❌ | /logisticas/{idLogisticaServico}/situacoes - Desativação/ativação de um serviço logístico  
POST | /logistica/servicos | /logisticas/servicos  
PUT | /logistica/{id}/servicos | /logisticas/servicos/{idLogisticaServico}  

#### Objetos

Endpoint | API v2 | API v3  
---|---|---  
DELETE | ❌ | /logisticas/objetos/{idObjeto}  
GET individual | ❌ | /logisticas/objetos/{idObjeto}  
POST vinculo rastreamento venda | /logistica/rastreamento/pedido/{numero} | /logisticas/objetos  
POST vinculo rastreamento NF-e | /logistica/rastreamento/notafiscal/{numero}/{serie} | /logisticas/objetos  
POST | /logistica/evento/{codigo_rastremento} | **PUT** /logisticas/objetos/{idObjeto}  
PUT | ❌ | /logisticas/objetos/{idObjeto}  

## 🌟 Novos resources

  * /categorias/receitas-despesas
  * /contas-contabeis
  * /contatos/tipos
  * /empresas
  * /estoques
  * /homologacao
  * /naturezas-operacoes
  * /notificacoes
  * /produtos/estruturas
  * /produtos/variacoes
  * /situacoes/modulos
  * /situacoes/transicoes
  * /usuarios
  * /vendedores

## 🚫 Resources indisponíveis

Alguns resources não estão disponíveis na API v3, sendo eles:

  * CT-e
  * Grupos de produtos
  * Proposta comercial