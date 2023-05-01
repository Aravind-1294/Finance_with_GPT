from flask import Flask, request, render_template
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity
import pandas as pd
import numpy as np
import config

app = Flask(__name__)

openai.api_key = config.OPENAI_API_KEY

@app.route('/static/<path:filename>')
def serve_static(filename):
  return app.send_static_file(filename)

@app.route('/')
def search_form():
  return render_template('search_form.html')


@app.route('/search')
def search():
    # Get the search query from the URL query string
    query = request.args.get('query')

    search_term_vector = get_embedding(query, engine="text-embedding-ada-002")

    df = pd.read_csv('Data_with_Embeddings.csv')
    df['embedding'] = df['vectors'].apply(eval).apply(np.array)
    df["similarities"] = df['embedding'].apply(lambda x: cosine_similarity(x, search_term_vector))
    sorted_by_similarity = df.sort_values("similarities", ascending=False).head(3)

    results = sorted_by_similarity['Answers']

    COMPLETIONS_MODEL = "text-davinci-003"
    EMBEDDINGS_MODEL = "text-embedding-ada-002"

    model_engine = COMPLETIONS_MODEL
    model_prompt = f"""Answer the following question using only the context below .Answer in style of warren buffett.

    Context: {results}
    Q: {query} A:"""

    response = openai.Completion.create(
      engine=model_engine,
      prompt=model_prompt,
      max_tokens=100,
      n=1,
      stop=None,
      temperature=0.5,)

    answer = response.choices[0].text.strip()
  
    
    answers = answer
    print(answers)



    # Render the search results template, passing in the search query and results
    return render_template('search_results.html', query=query, results=answers)

if __name__ == '__main__':
  app.run()
