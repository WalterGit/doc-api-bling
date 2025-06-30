# Erros comuns

## Introdução

Nós usamos HTTP codes para diferenciar as requisições bem sucedidas de requisições que contenham erros. Sempre serão informados o tipo, mensagem e descrição do erro.

Erros **4xx** apontam inconsistências nos dados enviados.

Erros **5xx** apontam falhas no nosso serviço.

A listagem abaixo exemplifica códigos de erros e mensagens que podem ser encontrados durante o uso da API.

## VALIDATION_ERROR

Ocorre quando houve erros na validação dos campos enviados pela requisição.

HTTP Code: `400`

    {
    	"error": {
    		"type": "VALIDATION_ERROR",
    		"message": "Não foi possível executar a operação",
    		"description": "Ocorreu um erro ao validar os dados recebidos."
    	}
    }

## MISSING_REQUIRED_FIELD_ERROR

Ocorre quando campos obrigatórios não foram enviados.

HTTP Code: `400`

    {
    	"error": {
    		"type": "MISSING_REQUIRED_FIELD_ERROR",
    		"message": "Não foi possível executar a operação",
    		"description": "Nenhum dado foi informado na requisição."
    	}
    }

## UNKNOWN_ERROR

Ocorre quando uma operação não pode ser concluida.

HTTP Code: `400`

    {
    	"error": {
    		"type": "UNKNOWN_ERROR",
    		"message": "Não foi possível executar a operação",
    		"description": "Ocorreu um erro inesperado."
    	}
    }

## UNAUTHORIZED

Ocorre quando a chave de acesso informada não está válida.

HTTP Code: `401`

    {
    	"error": {
    		"type": "UNAUTHORIZED",
    		"message": "Não autorizado.",
    		"description": "Você não está autorizado a realizar esta operação. Verifique suas credenciais e tente novamente."
    	}
    }

## FORBIDDEN

Ocorre quando o token enviado não possui permissão para operar nos escopos requisitados.

HTTP Code: `403`

    {
    	"error": {
    		"type": "FORBIDDEN",
    		"message": "Não permitido.",
    		"description": "Você não está autorizado a realizar esta operação. Consulte suas permissões com o administrador de sua conta."
    	}
    }

## RESOURCE_NOT_FOUND

Ocorre quando a URN ou URI informada não existe, ou quando o recurso solicitado não foi encontrado no sistema.

HTTP Code: `404`

    {
    	"error": {
    		"type": "RESOURCE_NOT_FOUND",
    		"message": "Não autorizado.",
    		"description": "O recurso requisitado não foi encontrado. Verifique se o endpoint solicitado está correto ou se o ID informado realmente existe no sistema."
    	}
    }

## TOO_MANY_REQUESTS

Ocorre quando o total de requisições feitas atingiu o seu limite. Conforme a página [limites](<https://developer.bling.com.br/limites#Limites>).

HTTP Code: `429`

    {
    	"error": {
    		"type": "TOO_MANY_REQUESTS",
    		"message": "Limite de requisições atingido.",
    		"description": "Você atingiu o limite de requisições disponível. Por favor, aguarde alguns minutos e tente novamente."
    	}
    }

## SERVER_ERROR

Ocorre quando algum processo interno no servidor da nossa aplicação possui alguma falha.

HTTP Code: `500`

    {
    	"error": {
    		"type": "SERVER_ERROR",
    		"message": "Não foi possível executar a operação",
    		"description": "Um erro interno ocorreu."
    	}
    }