import requests
import json
import pandas

def get_fresh_token():
    #shop url. Here is sample
    url = "https://sklep312597.shoparena.pl/webapi/rest/auth"

    payload = {}
    headers = {
        #credentials
        'client_id': '',
        'client_secret': '!',
        'Authorization': 'Basic '
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    token = response.text.split('"')[3]
    return token


def get_product(token, id):
    import requests

    url = "https://sklep312597.shoparena.pl/webapi/rest/products/"+str(id)

    payload = {}
    headers = {
        'Authorization': 'Bearer '+token,
        'Cookie': 'admin_ip_verify=d41d8cd98f00b204e9800998ecf8427e'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.text)
    return response.text

def update_image(id,token,link):
    url = "https://sklep312597.shoparena.pl/webapi/rest/product-images/"

    payload = json.dumps({
        "product_id": id,
        "url": link
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token,
        'Cookie': 'admin_ip_verify=d41d8cd98f00b204e9800998ecf8427e'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

df = pandas.read_csv('produkty.csv')
#optionally use toki for a once generated token.
#toki = ''
for i in range(1200,1230):
    tekst = json.loads(get_product(toki,i))
    print("Teraz artykul numer " + str(i))
    try:
        print(tekst["code"])
        kkk = df.query('produkt_id == '+str(tekst["code"]))
        for k in range(1, 10):
            if isinstance(kkk.values[0][k], str):
                print(kkk.values[0][k])
                update_image(i,toki,kkk.values[0][k])
    except:
        print('nie ma takiego indeksu')