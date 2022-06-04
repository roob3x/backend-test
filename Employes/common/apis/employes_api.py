import requests


def get_employes(context,param):
    if context.config.userdata['environment'] == 'MOCK':
        url = 'https://d733f97f-b535-4b74-96ba-ed1e5e4c3fe1.mock.pstmn.io/v1/funcionario'
    else:
        url = 'http://dummy.restapiexample.com/api/v1/employees'
    url = url + param
    try:
        response = requests.get(url)
        return response
    except OSError as err:
        print("Request of Employees has been failed", err)