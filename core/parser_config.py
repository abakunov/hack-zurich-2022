import requests
import os
import re
# from core.models import *


import requests

cookies = {
    'fvgs_ml': 'mosaic',
    'Zalando-Client-Id': 'cbee5c89-2e8d-489c-91b6-1fd7923abfeb',
    'language-preference': 'da',
    '_gcl_au': '1.1.649208744.1663445637',
    'sqt_cap': '1663445627388',
    '_ga': 'GA1.2.506774501.1663445637',
    '_gid': 'GA1.2.248003707.1663445637',
    '_fbp': 'fb.1.1663446322136.2078032114',
    'ncx': 'm',
    'catalog.follow_brand_banner_re': '%7B%22count%22%3A3%2C%22isClosed%22%3Atrue%7D',
    'mpulseinject': 'true',
    'bm_sz': '6055D12B7AD2878616D686B33F5A79B0~YAAQDmAVAgTLQEWDAQAAVJQrThHygVCCPc68WlYxAXbHj/DxJrZLkss5tJ6aI1niDcvCq4LC5jOlqd1Ro5sStu69bBX5xLq4gXiB8Hysf4B/2xLql1hrITe7okJmpVkwqCr8TpiPYZ3hCwDNTS/MedNAcM7KaSfFB941sg7Cn4LKzFsrShJk6gUOGPBU+WKCblvvmVpGjUhEa7+iy8gWLRrHB1MR4b9pJ2zKBsErBDgdBAFeUNRi0iwBSX/gQHNCUSf9/Om3sAssLTDt+g0fGgCA1otIQ3u/Hy2aPfoDzTVUUVacl/pzoiav2BzywDCUDdQlWuj5FqZe+bo2anp35Lu/V2cUsUUad9SQabi3nWhwvdLt7HVgVb3E715nkFenbQBIEQ==~3359041~4404801',
    'bm_mi': 'F99E158BD12024B5C15797D489884A27~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~1',
    'ak_bmsc': '4C192FE5AE9E6F2E773323F505CB4E34~000000000000000000000000000000~YAAQl5pkX0fpeTaDAQAAsoM2ThH6U4/lNcmH4rA4JO/w19thVBf8fBglTnh804fN9R1nBhAgul2jed+0CZhTSi5RXQgcMZVwTRb+W2ADmxKdTrgMXNBSJuYVpdWpiWaA1FyDfdSQdikcCTGC0YjXjwXKWy4Z17ZZbsthdmbir/ej2rvzlLaPVHIRiept5GKgs1xjlxPZo/7MzBIll2TDJiN/NAFhxo1YKIMgLMQKSk9O0R3seSS6fpA2kjWVSbjagwC52wBwodV9avvISsMdnb/PcUb9pTWQIqJhDTsPEZBA3EbCyC+Fxo+y+9cW3aHQNJeOLhqxTaRfnRP2cFzWi3IZuhkM/I9McxlcRGHspJaO+ARnEVBwUL5nnk+5Z/amHDv0lF7O/kkzpGKMgc4MNZQB3C5cohZmhGVZUAfKR7dsfoF7Nhn02rmQPYEA8q97XQSfklxrc/ImP+/HVSJbD0CtZRLHxPQ+iJIvWM9s2+33f9K/3aAbo2NYzgMpSvtYl4gTnBUqwRAPWRcRt9bJQTgjXpJVQyUZQcZE1wjR9aXMlJXvN64yVuvy95svZfCdbeLv82h0o5o2A6xeqiL/e833Tr6lE+aQ+azudwpnBKMqSIeUK80ez9omafn+lRwawU5BBGj/j07F8qYZLwMP0Cwkp5ZTbwH1iys9sEHso4oxBKN/de/D+da7+9n0cdQMId6pfFoBBDH6e8FOz2/5cvxA3jSKtODn24pGJvQxwZov1BqUngvIvaV04YqSW7dcW/vxkMYqTTObkrcadisiA1AMzphCysELGweRGFO+MEQEOKOkCqvt7O6s8abknWHIvdXHcCYN9lUsHzXBxYQfyMPV8VHbVvwY/Oo9aPcYK2vIhufBM72rqU2fnEhA+tblN+SmuMtJ2nPZfa/xiFADA8rtTE0x6gDm2gPO2halLDCYNT2jkilJuGbn5YSjsYzqv4lTcOHh7vvdLU9N4JnXcPqSugFdRfZqkSe3auQOy4uxWcjZpDwLk4VNAT67xpjjlefN6NzvqqbB34ang++BtgdxEUHfhCljKRHHXgMko/SY4SXPcG/1jZVMuA7oGrHgvJgRSdewh8Gl/EmJR4nilVRXXkmHIzTmlk8wudh8Sjhmw3kG2hkhwG/Mi9WrhwTeilZMGz6YMq7/ebiM5FPxbqxPhehnLEbMFatfGZoIZiUYd+GyPV9y345zpVLASINaWN63cGNPtNPfOhWNdEOYdzM7mu4ObIRdW9ezvb/zfIbQxJoE01Dx6IIsFq/dgYBbo1xLeZtRtmeDgbdB91O8BBQ0ACqIBL0GRt+vefSOT4NFr8R16cE4YPLKtiJ4KPsJ3cN9QL8AAlhU+A8jjXDnnFmXlOcMfUQUVx+HD+tvN1iiqCHAp4PC7CYU8y4BfneyGeR2lAFUyzy5LuFW8x8SVLVyclDRktQznt/uLfbSN2bcNJa5C2zSZsqDhT60uo3nTIS5f2vXTllgcH/UWhGy/3v2A9jxpvM7jPAZTcMJvQL/+TfB2c6VdcXnHxfase6TO1UmuI6ctrTNF/22PwUhbgInuzt2mfDH4aCGz+IEA8HYDdyMpZht2S0fjKisC1ccRxKEDm5GY7DEOQ2KsdiVYOXTuTk7xXmJkCAmsqyGEKKvgXpaeRm7rGJIJr49RFbDYjL8H/QknK71IGaxjehcYgjOVNfuw3w1zf4j4TJ4pU/rKQd/dneulyuqQlPWp9KrOMgDpN3VFX+lzOkZm/qUkuLBCnOjgkKhTpgTf6jwi86hKNozscHouJjPC5xMUvrJGTXTSuNYqH0pRo5kWUlf5selIEGu7V1HiQ2Hy09Sn8DLsinWJPPI2hTcKs6ENlOKOdkng01nPkR/VvzT2dSk2h/2gWHTaVEF0SMBET/Njg7aUut1rbmds+YM8QfufAOu4qAstOwEg6OTgbqo3UyI2nEEcXwOWoe4VC4Et1Owrux/0Ghhd8QvUSFJVLAtOKlRfwbwjhmAkLsVqn+Na9KxMtXFhdYfjiyaCx6mI9rBEhckHYAN0Cxd4eYtv/0VUR9J/1nuVNtrCcbTt3QyrWKZB9F5IW6b6L5tuX63t/tz6ztrmuRwEJ6NLAuGx4e9U0DnuIBI+rTPTo8Og14ap+6ekr6rRW5SaGo1CuQFkOb/XpowO9DiZPE8FFH47pGjlgyO90EN+Oq2+H2A7Yr3pafwLRSumri/9i1utPNHneoxhiTip66rL535LShPBIcUoJ1vSB2E+CLlquR4xsE2K83/B51DD4dB1p3h5RgVNV68B2aHBouSC7PWjdRrqgJKAHVorF/sG/FhRmnRg74yLR8JBJUVbsleUf55Uw+cwGS1TkU/la62QZ2e6VuDEH//oH8+keQUDe1MzfpnjkyVedcJD1olW6IBimug1uvKI7n99cZJ2U+DB5dAplsVrJMpvFx2OYUJMzefK4DG9gwSxvsGifPY0p46CGbPyx6N728UwRrdQ4T9w9OyglNu533je2mat4XZAXnJwHfLiQsol75SS6h5wplRY3Qb/NasnMi6fUjYlmWBcHio19YVOYTxLKZwK+DOuBKKxnOrSiOCEdFUSK4EirYh/n5RvXz4BP9bHC7EnWJGFFFATJkNxrtnD+ONfiXIpFO3/3mX6Fpn3BQ/yN3SYOj1LgmmIqCNWk/VjPXERGsikGz4GvAFVnh1bqAWCA6jD81hlxwgbtY9FvBCrVnX/0lxq82RRfhmpPlfX69P85vsPFT83c/M/EdEl0KqhvIB+a2DkYcZdYcaVO9fLZFlIJGNooZc4pZ/XV5BP+T6urdX+mqq4EdfOr+RovQw7wARQjWo6pKDtjWOkqd2yTs/GgSc2EziQszcLxdUp5dc2pEcTo6QEfZEyFPg4fJgFwzNTGBxaGcF2Y/6TnCwNYQ52R7OLKgelRVGpqGJzIVnMKWK5tv9dPGzBAJXVcDw0AV8YczOma9h0CGYO/oRXkjwaCIQAXLe/vWKWNRtiHowSGLmz9my78ERWPhEDVN0IeBJucuE/kGv86brPSCtN9mVizxgvZXzR74ubOLJGsDKF6voW88iKs81TvTfY1xZdXCcS+Zmpyqo6o193AehIsvOEh+9FwTV/xhWjIeOjUZb9QqLc/BnVUlAVzfWS6QrhEbI3K0rd4+cuNvjFV7RZscDWDl+GrkDqWod+F1Kd861b/VWNbMXz+UVcpBpJw+qwF04Wpg+l28YT+kPegcOWx5s88CNJtVTJGsxdplXUofkEjfM9KaEFuQcoey2L7WKVnS/tSU4Wh/gaqr90kVBeb/K/dwFZF1Vo1diTVCWs32OAT3AOusUD1X/0bGhdGXYJDjIMpZal4RwxSPfEnTt/33fweqc+Zs/d3ktDoOevvIpiaToyQZZPA6MeXNbWyzTyFjmOc8erzR17iWcHCjZU0nNtlJH/4tYN9uS5j00VAo912gy6zVX+55HNvYR',
    '_gat_zalga': '1',
    'frsx': 'AAAAAL7-Ox2S69lEIm8c5nuqP4EP68gTym2JIckL1uA0ynNG7XanaZpHd_4WGfFjOE2hKICoUKbnw_3cZE1gBtuMe3bzu1yuZyK9lx8fAYvpvWVlL93gCGqwY3hvswgslL__SDtKKWUpfYA9l_u2fgk=',
    '_abck': '736B5C37A91E8DBB4FE8983A443C51FD~-1~YAAQl5pkX5lUejaDAQAAsXA7TggaaqYawbT5sGucpqqrwJLMZva/cMbuRI6QZCWoB/PZ6Q/qY3Pvly9+FWehkyNnXzHtDL9UT4atNxjH8XgJeIdINmcgu5rOBxjD91n4vrkxBFPoyKJbEMRJx8ZFu1W7FZK8Rg8XO86F7fOqzDt4JquFk3DQTe+MY6F1T3wHsMnFb7gOTm+tQaMDrjtUKcl4MCMsMpf1UqBhgb5R4crr5DdjfbyZ9uWl9EbBV5GUq6E8rRiM9AYNGt1G8t0pON66bG1IAN2thekcD0m1sTI3Qkp+1Y2OkXzev7CVqHkMmOsY9o1rfhOoLa9HSM+g6w1I1tSMiMCl98FZp6fMRF30tsMYikUtbirncHbCs+ypQ4mICJIAswOZFiqxgBpc5trhFobAWpg3WFyMKdNDn4MxLKL/Io7rb6yYLH+qybXGFIWYVhJb7ei2CT6YhbpcH/me8A0V0UIYoMfghkZZuMxW/g==~-1~-1~-1',
    'bm_sv': '5A43D40B919C187F184B3BB4029415F2~YAAQl5pkX8pUejaDAQAAUHI7ThEsU6EBT/6sO+pd0f7uzxqbyHIGLbyK2k11QIp03shLhYgYygNP4e7K8x6kxy8NHrCChdxk4I/1Yt6xebpKOCNbPiKT0fQkJyTZuvxgWgYxxUAnclzm0vlcbIQ27dwEpa2+1xUwl2CuRGthPPy/CubB4I+r26shAb9hdbMCW+YP2BkaGhkB3bGd2hK5DCV2EY+VIKVM+nrI2MWbmGYVSLkL2mpsuuO98TFBvc3zFgw=~1',
}

headers = {
    'authority': 'www.zalando.dk',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'fvgs_ml=mosaic; Zalando-Client-Id=cbee5c89-2e8d-489c-91b6-1fd7923abfeb; language-preference=da; _gcl_au=1.1.649208744.1663445637; sqt_cap=1663445627388; _ga=GA1.2.506774501.1663445637; _gid=GA1.2.248003707.1663445637; _fbp=fb.1.1663446322136.2078032114; ncx=m; catalog.follow_brand_banner_re=%7B%22count%22%3A3%2C%22isClosed%22%3Atrue%7D; mpulseinject=true; bm_sz=6055D12B7AD2878616D686B33F5A79B0~YAAQDmAVAgTLQEWDAQAAVJQrThHygVCCPc68WlYxAXbHj/DxJrZLkss5tJ6aI1niDcvCq4LC5jOlqd1Ro5sStu69bBX5xLq4gXiB8Hysf4B/2xLql1hrITe7okJmpVkwqCr8TpiPYZ3hCwDNTS/MedNAcM7KaSfFB941sg7Cn4LKzFsrShJk6gUOGPBU+WKCblvvmVpGjUhEa7+iy8gWLRrHB1MR4b9pJ2zKBsErBDgdBAFeUNRi0iwBSX/gQHNCUSf9/Om3sAssLTDt+g0fGgCA1otIQ3u/Hy2aPfoDzTVUUVacl/pzoiav2BzywDCUDdQlWuj5FqZe+bo2anp35Lu/V2cUsUUad9SQabi3nWhwvdLt7HVgVb3E715nkFenbQBIEQ==~3359041~4404801; bm_mi=F99E158BD12024B5C15797D489884A27~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~1; ak_bmsc=4C192FE5AE9E6F2E773323F505CB4E34~000000000000000000000000000000~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; _gat_zalga=1; frsx=AAAAAL7-Ox2S69lEIm8c5nuqP4EP68gTym2JIckL1uA0ynNG7XanaZpHd_4WGfFjOE2hKICoUKbnw_3cZE1gBtuMe3bzu1yuZyK9lx8fAYvpvWVlL93gCGqwY3hvswgslL__SDtKKWUpfYA9l_u2fgk=; _abck=736B5C37A91E8DBB4FE8983A443C51FD~-1~YAAQl5pkX5lUejaDAQAAsXA7TggaaqYawbT5sGucpqqrwJLMZva/cMbuRI6QZCWoB/PZ6Q/qY3Pvly9+FWehkyNnXzHtDL9UT4atNxjH8XgJeIdINmcgu5rOBxjD91n4vrkxBFPoyKJbEMRJx8ZFu1W7FZK8Rg8XO86F7fOqzDt4JquFk3DQTe+MY6F1T3wHsMnFb7gOTm+tQaMDrjtUKcl4MCMsMpf1UqBhgb5R4crr5DdjfbyZ9uWl9EbBV5GUq6E8rRiM9AYNGt1G8t0pON66bG1IAN2thekcD0m1sTI3Qkp+1Y2OkXzev7CVqHkMmOsY9o1rfhOoLa9HSM+g6w1I1tSMiMCl98FZp6fMRF30tsMYikUtbirncHbCs+ypQ4mICJIAswOZFiqxgBpc5trhFobAWpg3WFyMKdNDn4MxLKL/Io7rb6yYLH+qybXGFIWYVhJb7ei2CT6YhbpcH/me8A0V0UIYoMfghkZZuMxW/g==~-1~-1~-1; bm_sv=5A43D40B919C187F184B3BB4029415F2~YAAQl5pkX8pUejaDAQAAUHI7ThEsU6EBT/6sO+pd0f7uzxqbyHIGLbyK2k11QIp03shLhYgYygNP4e7K8x6kxy8NHrCChdxk4I/1Yt6xebpKOCNbPiKT0fQkJyTZuvxgWgYxxUAnclzm0vlcbIQ27dwEpa2+1xUwl2CuRGthPPy/CubB4I+r26shAb9hdbMCW+YP2BkaGhkB3bGd2hK5DCV2EY+VIKVM+nrI2MWbmGYVSLkL2mpsuuO98TFBvc3zFgw=~1',
    'dpr': '2',
    'origin': 'https://www.zalando.dk',
    'referer': 'https://www.zalando.dk/herretoej-t-shirts-og-poloer/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'viewport-width': '1067',
    'x-xsrf-token': 'AAAAAL7-Ox2S69lEIm8c5nuqP4EP68gTym2JIckL1uA0ynNG7XanaZpHd_4WGfFjOE2hKICoUKbnw_3cZE1gBtuMe3bzu1yuZyK9lx8fAYvpvWVlL93gCGqwY3hvswgslL__SDtKKWUpfYA9l_u2fgk=',
    'x-zalando-experiments': 'b891eec6-b3d5-4760-b685-fe1fbe3ce330=THE_LABEL_IS_ENABLED;07fb3627-d56d-4909-954d-d58607a2abd6=RES_CATALOG_ENTITIES;90aa955b-d7f6-4fe1-a14f-2522788af1bb=fdbe-release1-enabled;b951ad11-ec05-4c78-9772-1eb1100c5c96=ABB_DISABLED;cb304bd0-53f9-4d2c-9817-3fdd9e388aaa=sephora_garden_disabled;163908b6-4ba9-4442-981f-b340d4b4e9fe=experience_theme_disabled',
    'x-zalando-feature': 'catalog',
    'x-zalando-intent-context': 'navigationTargetGroup=MEN',
    'x-zalando-request-uri': '/herretoej-t-shirts-og-poloer/',
}

json_data = [
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::OS322S0LB-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::ZI122O011-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::DEO22O01P-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::HU342D076-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100OX-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100T7-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100IN-I11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::JA221001S-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::WOD22O01T-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::WOD22O01O-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100N0-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::VIO21003C-M11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100SA-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100M4-J11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::AD122O0UQ-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100PF-O11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::DEO22O01S-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::OS322O0YX-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100P2-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::NI122O0US-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::M0M22O0B7-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::CS622O09P-B11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::JA222O543-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100SE-J11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100P8-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100TG-B11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::M0M22O06Y-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PUC22O1IJ-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::BEJ22D08X-C11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::HU342D08A-N11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::UR622O08W-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::OS322O19I-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::JA221001P-A12',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::H3A2102RB-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::ZI121000A-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO121001I-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::H0422O0D7-T11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::JA222O46D-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100M4-O11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::NI122O0US-C11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::JA222O467-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO121000A-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::NI122O0U9-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PUC22O1H7-C11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::NI122O0U9-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::C1422O0G7-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::TH342D00W-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PUC22O1BY-O11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO121002E-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::NIJ22O04K-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO121001P-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::OS322O0KY-Q12',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::R1V210031-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::ZI122O014-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100M4-C11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100AI-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100PF-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::C7642D09K-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100M6-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::SIF22O0M7-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO121002A-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PUC22O1DB-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100NX-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::LE222O072-N12',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::VIO210002-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO121007C-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::JA222O4H0-B11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::TO122O07A-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::AD1210016-K16',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::M0M22O05T-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::OS322O122-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO121003F-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::C1422O0DC-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PI922O0GY-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PUC22O0S2-T11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::HU342D08A-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::TOB22O018-K11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PI922O0UM-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::TOB22O018-C11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PI922O0VF-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::M0M22O0Z2-A11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::PUC22O1IG-O11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::YO12100PX-Q11',
        },
    },
    {
        'id': '0ec65c3a62f6bd0b29a59f22021a44f42e6282b7f8ff930718a1dd5783b336fc',
        'variables': {
            'id': 'ern:product::NI122O0CE-K12',
        },
    },
]


response = requests.post('https://www.zalando.dk/api/graphql/', cookies=cookies, headers=headers, json=json_data).json()

def start():
    for good in response:
        # try:
            good = good['data']['product']['family']['products']['edges'][:-1]
            print(good)
            # name = good['name']
            # brand = good['brand']['name']
            # image_url = re.findall("(.*\.jpg).*", good['largeDefaultMedia']['uri'])[0]
            # link = good['uri']
            # price = int(good['displayPrice']['original']['formatted'][:-6])
            # silhouette = good['silhouette']
            # print(price)
        # except Exception as e:
        #     print(e)

start()