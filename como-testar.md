# Como testar

## API v3 no Postman

Como pré-requisito para utilização da API v3, é necessário que haja um aplicativo já cadastrado. Caso não o tenha, confira [o passo a passo](<https://developer.bling.com.br/aplicativos#aplicativos>) para realizar o cadastro.

### Importação da collection

É possível importar toda a _collection_ da API v3 para o [Postman](<https://www.postman.com/>). Esse processo facilita a utilização da API, pois todos os _endpoints_ disponíveis ficam de fácil acesso.

[ __ Bling collection ](<https://developer.bling.com.br/build/assets/openapi-8dcd70b2.json>)

No Postman, clique em **Import** , selecione o arquivo anteriormente salvo na máquina e importe-o.

### Configurando a permissão de acesso

Nesse momento, será necessário configurar as permissões de acesso do aplicativo a conta Bling.

Para isso, clique no nome da _collection_ criada (Bling API) e escolha a aba _Authorization_.

Certifique-se que o campo **Type** esteja selecionado como **OAuth 2.0**.

Na seção "Configure New Token", altere os seguintes campos:

  1. **Callback URL** para o mesmo informado no cadastro do aplicativo no campo **Link de redirecionamento**.
  2. Preencha o campo **Client ID** de acordo com o dado exibido no cadastro do aplicativo.
  3. Preencha o campo **Client Secret** de acordo com o dado exibido no cadastro do aplicativo. Clique no ícone de olho para revelar o valor do _secret_.
  4. Preencha o campo **State** com um valor aleatório, pois o mesmo não pode ser vazio. Para mais informações sobre o campo `state`, acesse a seção [Authorization code](<aplicativos#authorization-code>).

Clique em **Get New Access Token**.

Nesse ponto, você precisará realizar o login na conta Bling.

Após o login, será exibida a tela de autorização. Clique em "Autorizar".

Assim que o login for concluído, a mensagem de sucesso será exibida.

Clique em **Use Token** , para que o _token_ seja preenchido de forma automática nas configurações da autorização de toda a _collection_.

Por fim, pressione **Ctrl + S** para salvar as configurações realizadas.

Agora você terá acesso aos escopos da conta Bling que o aplicativo configurado possui.

### Exemplo de requisição

Exemplo de requisição GET de Contatos.