# backend-test

Foi utilizado o framework *request* para realizar as chamadas na api

## PARA CONFIGURAR O AMBINTE
-> Raiz do diretorio do projeto executar o comando:
 - pip install -r requirements.txt
 

## PARA EXECUCAO DO TESTE DE BACKEND
- Entrar no diretorio com "cd backend-test/Employes"
- Digitar comando behave --tags=@nomedaTag
Obs: altere o @nomedaTag de acordo com a tag que necessita executar. caso queira executar todos os cenarios simplesmente insira behave


## IMPORTANTE
Foi implementado mock no response utilizando postman com mock server. Mude o ambiente de acordo com a necessidade do teste atraves do arquivo behave.ini