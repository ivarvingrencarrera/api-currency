from datetime import datetime

from httpx import AsyncClient

date = datetime.now().strftime('%Y-%m-%d')
value = 529.99


async def test_must_convert_currency_brl_to_usd(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'USD', 'date': date, 'value': value}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['currency_symbol'] == '$'
    assert output['formatted_value'] == '$98,23'
    assert output['value'] == 98.23


async def test_must_convert_currency_brl_to_eur(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'EUR', 'date': date, 'value': value}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['currency_symbol'] == '€'
    assert output['formatted_value'] == '€83,26'
    assert output['value'] == 83.26


async def test_must_convert_currency_brl_to_inr(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'INR', 'date': date, 'value': value}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['currency_symbol'] == '₹'
    assert output['formatted_value'] == '₹7.318,93'
    assert output['value'] == 7318.93


async def test_must_convert_currency_brl_to_brl(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'BRL', 'date': date, 'value': value}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['currency_symbol'] == 'R$'
    assert output['formatted_value'] == 'R$529,99'
    assert output['value'] == 529.99


async def test_must_not_convert_currency_brl_to_yen(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'YEN', 'date': date, 'value': value}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['detail'] == 'Currency with code YEN not found'


async def test_must_not_convert_currency_brl_to_usd_with_negative_value(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'USD', 'date': date, 'value': -value}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['detail'] == 'value must be greater than zero'


async def test_must_not_convert_currency_brl_to_usd_with_priceless_value(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'USD', 'date': date, 'value': 0}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['detail'] == 'value must be greater than zero'


async def test_must_not_convert_currency_brl_to_usd_when_data_not_exist(client: AsyncClient) -> None:
    input_ = {'currency_from': 'BRL', 'currency_to': 'USD', 'date': '2023-06-09', 'value': value}
    url = '/currencies/converter'
    response = await client.post(url, json=input_)
    output = response.json()
    assert output['detail'] == 'No exchange rate found for the given currencies.'


async def test_get_currency_brl(client: AsyncClient) -> None:
    currency = 'BRL'
    url = f'/currencies/{currency}'
    response = await client.get(url)
    output = response.json()
    assert output['code'] == 'BRL'
    assert output['name'] == 'Brazilian Real'
    assert output['symbol'] == 'R$'
