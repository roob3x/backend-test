#language: pt
Funcionalidade: Funcionario


    @pesquisa
    Cenário: LISTAR_FUNCIONARIO_001 - Verifique que é retornado a lista de funcionarios
        Quando Realizo a buscar por todos os funcionarios
        Então  Valido que é retornado a lista com todos os funcionarios


    @pesquisa @por_id
    Cenário: LISTAR_FUNCIONARIO_002 - Verifique que é retornado os dados de um funcionário em específico
        Quando Realizo a buscar do funcionário pelo cadastro de numero 13
        Então  Valido que é retornado os dados do cliente