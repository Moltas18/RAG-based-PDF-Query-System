import openai

openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key

def generate_response(retrieved_texts, query, max_tokens=150):
    """
    Generates a response based on the retrieved texts and query.

    Args:
    retrieved_texts (list): List of retrieved text strings.
    query (str): Query string.
    max_tokens (int): Maximum number of tokens for the response.

    Returns:
    str: Generated response.
    """
    context = "\n".join(retrieved_texts)
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message['content']