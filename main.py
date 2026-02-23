import requests

SHOPIFY_STORE = "exemplositeblzportugal.myshopify.com"
API_VERSION = "2024-01"
ACCESS_TOKEN = "XXXXTOKENXXXX"

url = f"https://{SHOPIFY_STORE}/admin/api/{API_VERSION}/graphql.json"

headers = {
    "X-Shopify-Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

query = """
query {
  checkouts(first: 10) {
    edges {
      node {
        id
        email
        createdAt
        totalPriceV2 {
          amount
          currencyCode
        }
      }
    }
  }
}
"""

response = requests.post(url, json={"query": query}, headers=headers)
data = response.json()
