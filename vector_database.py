import numpy as np
import json
# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L6-v2')

with open('./products.json', 'r') as products_file:  
    products = json.load(products_file)

# product_embeddings_model = {
#     product['name']: model.encode(product['description']) for product in products
# }

# print(len(product_embeddings_model['Wireless Earbuds'])) 384

product_embeddings_random = {product['name']: np.random.rand(5) for product in products}

# print(len(product_embeddings_random['Wireless Earbuds']))

def cosine_similarity(vec1, vec2):
    
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)


def search_similar_products(query, top_n=3):
    
    # query_embedding = model.encode(query) # for pretrained model
    query_embedding = np.random.rand(5)  # Random embedding for the query

    similarities = []
    for product_name, embedding in product_embeddings_random.items():
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((product_name, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities[:top_n]

if __name__ == "__main__":
    while True:
        query = input("Enter your query: ")
        results = search_similar_products(query)

        print("\nTop 3 Matches:")
        for rank, (product_name, similarity) in enumerate(results, start=1):
            print(f"{rank}. Product: \"{product_name}\" | Similarity: {similarity:.2f}")
