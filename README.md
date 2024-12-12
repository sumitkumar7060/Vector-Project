# README

## Simulating a Vector Database with Random Embeddings

This project demonstrates the simulation of a vector database by generating random embeddings for products and finding the most similar products based on a query. Instead of using a pre-trained model for encoding product descriptions and queries, the embeddings are generated randomly for simplicity.

### Approach

1. **Loading Product Data**:
   - The script reads product data from a JSON file (`products.json`). Each product have a `name` and `description`.

2. **Embedding Generation**:
   - Normally, a pre-trained model like SentenceTransformer's `all-MiniLM-L6-v2` would be used to encode product descriptions and the query into embeddings.
      and this is auto create 384 dimensional vector embeddings. but your requirement according use the below example
   - In this simulation, random embeddings of size 5 are generated using NumPy for both the products and the query.

3. **Similarity Calculation**:
   -formula of cosine similarity:
      cosine_similarity=  v1 ⋅v2/(∣∣v1∣∣⋅∣∣v2∣∣)​

      cosine_similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
      where magnitude = np.linalg.norm(vector)
   - A custom `cosine_similarity` function is implemented to calculate the similarity between two vectors using their dot product and norms.

4. **Search Mechanism**:
   - The query embedding is compared with all product embeddings.
   - Products are ranked based on their similarity scores, and the top 3 most similar products are displayed.

### Instructions to Run the Script

1. **Prerequisites**:
   - Python 3.7 or higher installed on your machine.
   - A JSON file named `products.json` in the same directory as the script. This file should contain an array of products, where each product is an object with `name` and `description` fields.

2. **Steps**:
   - Install the required library using the following command:
     ```bash
     pip install numpy
     ```
   - Save the script as `vector_database.py`.
   - Run the script using:
     ```bash
     python vector_database.py
     ```

3. **Usage**:
   - Enter a query when prompted.
   - The script will output the top 3 products that are most similar to the query.

### Example Input and Output

#### Input
```
Enter your query: Wireless headphones with noise cancellation
```

#### Output
```
Top 3 Matches:
1. Product: "Smartphone Stand" | Similarity: 0.96
2. Product: "Gaming Mouse" | Similarity: 0.95
3. Product: "Noise-Canceling Headphones" | Similarity: 0.92
```

### Notes
- The similarity values and rankings are simulated and may not reflect real-world performance since random embeddings are used.
- To use this script with real embeddings, uncomment the lines related to SentenceTransformer, install the required library (`sentence-transformers`), and provide appropriate model and description data.
-for real time use a vector database i.e chromadb or faiss etc for create embeddings and store in chunks and get the similarity values content.

