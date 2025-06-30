# Limites

## Filtros

_Requests_ GET com filtros por período com intervalo superior a um ano retornarão o _status code_ `400`.

Filtros por período possuem os sufixos "Inicial" ou "Final", ex: `dataInicial`, `dataFinal`, `dataAlteracaoInicial` e `dataAlteracaoFinal`.

## Requisições

A API do Bling possui uma política de segurança para evitar prejudicar o usuário e assegurar a disponibilidade dos nossos recursos.

Existem limites sobre as requisições de cada conta Bling, não específicas por _endpoints_ , mas sim para todas. Isso significa que em quaisquer módulos que estejam sendo operados, o limite é aplicado para toda a conta.

Caso um limite seja atingido, os próximos _requests_ não serão processados.

Os limites por requisições são determinados pelas regras abaixo:

  * 3 requisições por segundo
  * 120.000 requisições por dia

Exemplos de retornos quando um limite é atingido:

HTTP Status code: `429` Too Many Requests

    {
    	"error": {
    		"type": "TOO_MANY_REQUESTS",
    		"message": "Limite de requisições atingido.",
    		"description": "O limite de requisições por segundo foi atingido, tente novamente mais tarde.",
    		"limit": 3,
    		"period": "second"
    	}
    }

HTTP Status code: `429` Too Many Requests

    {
    	"error": {
    		"type": "TOO_MANY_REQUESTS",
    		"message": "Limite de requisições atingido.",
    		"description": "O limite de requisições por dia foi atingido, tente novamente amanhã.",
    		"limit": 120000,
    		"period": "day"
    	}
    }

Também existem cenários aos quais o IP de origem da requisição pode ser bloqueado.

As regras de bloqueios por IP são especificadas abaixo:

  * 300 erros em 10 segundos, com duração de 10 minutos.
  * 600 _requests_ em 10 segundos, com duração de 10 minutos.
  * 20 _requests_ (`/oauth/token`) em 60 segundos, com duração de 60 minutos.

Com o objetivo de manter a integridade do sistema, se uma aplicação continuar ultrapassando os limites definidos, o IP poderá ser bloqueado por tempo indeterminado.