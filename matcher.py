from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pretrained BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(resume_text, job_desc):
    # Convert texts to embeddings
    embeddings = model.encode([resume_text, job_desc])
    
    # Calculate cosine similarity
    similarity = cosine_similarity(
        [embeddings[0]], 
        [embeddings[1]]
    )
    
    return round(float(similarity[0][0]) * 100, 2)
