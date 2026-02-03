from flask import Flask, request, jsonify, Response
from duckduckgo_search import DDGS
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🖼️ AHMAD RDX IMAGE API - LIVE"

@app.route('/find-img')
def find_image():
    query = request.args.get('q')
    if not query: 
        return jsonify({"status": False, "msg": "Ahmad bhai, query missing hai!"})

    try:
        # DDGS (DuckDuckGo Search) engine use kar rahe hain
        with DDGS() as ddgs:
            # 50 results mangwaye hain taake variety zyada ho
            results = list(ddgs.images(query, region="wt-wt", safesearch="off", max_results=50))
            
            if results:
                # 🎲 Har bar list mein se 1 random image select hogi
                random_image = random.choice(results)
                return jsonify({
                    "status": True,
                    "title": random_image.get('title', 'Image Search Result'),
                    "url": random_image.get('image'),
                    "source": random_image.get('source')
                })
            else:
                return jsonify({"status": False, "msg": "Nahi mila kuch bhi!"})
                
    except Exception as e:
        return jsonify({"status": False, "error": str(e)})

if __name__ == "__main__":
    # Render ke liye port 10000 zaroori hai
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
