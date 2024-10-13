import requests

# Jūsu API atslēga (nedalieties ar to)
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGQ1OWNlZi1kYmI4LTRlYTUtYjE3OC1kMjU0MGZjZDY5MTkiLCJqdGkiOiIyNDFmMjI3NDVkZDBhZjI1NjE4YjlkYzVmNzcxYjg0ZjU1YzA3YWQ5N2VmOWYwYzYyYzdiY2ZkMzEzY2MxMDMyZGNjOGI5MTUzMTRkODhlNyIsImlhdCI6MTcyODUwMTU2MS4yODY2MjksIm5iZiI6MTcyODUwMTU2MS4yODY2MzIsImV4cCI6MjA0NDAzNDM2MS4yNDYyOCwic3ViIjoiMzUxMjkwMyIsInNjb3BlcyI6W119.q6aX1NQgBmNthYzhFyFIT3C9Zh8tO0L01qHZ120pN_WNDIUx3NCI025S0FNmdGqPr6rXQkTN0NwG14wW_tlv43XR4OFzEb-jH8NzvxWAus6Qo1RGCy4qiukvhnv7xwgVKtZluFMOwvm25vi9e54dHYP-qgDNZEXjCcCyy4DNTu1eE773XcFA4DQ0DIl9ym3IzInw7_ts7QUy2cbFGqT9bnRffn7DwxaoCN-pEO-lY838w3Ig9CZgsP95ebGUT6pNZoG2LZbZ5jtmke0m8GpRP51ZofKIz1f8xzi5o42bz28cJaHiuBx0QpywN2c9vmE-tbO8YHyQbP1rPziJj5ITF-WG16gaJc-W7PH3rK0Ggy55aOMPlCyXliGRI8_hoAldR_1_Z6Sk4El9s0JL0ii6PXwto9f8gbLZ6h0d033Hmos7CegKcdhrSWHSq0FBwtfGcP4lzzM0njfje_b4-RykBi6GjRNMs0y7GJoDxqTyeWvRKjSsDcH7nCnC5X9nJXc1'

# Produkta ID
product_id = '368076'

# API pieprasījuma galvenes
headers = {
    'Accept': 'application/vnd.api+json',
    'Authorization': f'Bearer {api_key}'
}

# Veicam GET pieprasījumu, lai iegūtu produkta informāciju
response = requests.get(
    f'https://api.lemonsqueezy.com/v1/products/{product_id}',
    headers=headers
)

# Pārbaudām atbildi
if response.status_code == 200:
    print("Produkta informācija veiksmīgi iegūta:")
    product_data = response.json()['data']['attributes']
    print(f"Nosaukums: {product_data['name']}")
    print(f"Apraksts: {product_data['description']}")
    print(f"Cena: {product_data['price_formatted']}")
    print(f"Statuss: {product_data['status_formatted']}")
else:
    print(f"Kļūda: {response.status_code}")
    print(response.text)