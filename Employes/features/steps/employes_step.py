from common.apis.employes_api import get_employes
from hamcrest import assert_that, is_
from constants.status_code import *


@when('Realizo a buscar por todos os funcionarios')
def step_impl(context):
    context.get_employer_response = get_employes(context,"")


@when('Realizo a buscar do funcionário pelo cadastro de numero {id}')
def step_impl(context,id):
    context.get_employer_response = get_employes(context,'/'+id)


@then('Valido que é retornado a lista com todos os funcionarios')
def step_impl(context):
    assert_that(context.get_employer_response.status_code, is_(SUCESSFULL))


@then('Valido que é retornado os dados do cliente')
def step_impl(context):
    assert_that(context.get_employer_response.status_code, is_(SUCESSFULL))