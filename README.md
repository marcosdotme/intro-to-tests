# O que são testes?

Teste é a tarefa de executar e avaliar se o comportamento do código está de acordo com o que é esperado dele.

Fazemos isso para garantir a qualidade e resiliência do produto final que estamos entregando. Sem teste, ficamos reféns à bugs e inconsistências geradas pelo nosso código.

A maneira mais trivial de realizar um teste é executá-lo manualmente e observar o seu comportamento. Após isso, imaginar cenários onde o código pode falhar, executá-lo manualmente e verificar se falhou no ponto que imaginávamos. Caso tenha falhado, aplicamos a correção e continuamos esse processo até que estejamos satisfeitos.

**É impossível entregar algo 100% testado, pois há infinitas possibilidades de cenários e não é viável testar todos eles, então, primeiro precisamos testar as funcionalidades mais críticas da aplicação afim de mitigar o impacto.**

<br>

# Testes automatizados

Afim de evitar que precisemos executar manualmente os testes em todas as vezes que o nosso código for alterado, os testes automatizados servem para **automatizar** esse processo. Além de nos poupar tempo, mitiga também a possibilidade de executarmos um teste de forma errada, o que é contraditório, mas pode acontecer.

As bibliotecas mais famosas de testes automatizados são:

* Pytest
* Unittest
