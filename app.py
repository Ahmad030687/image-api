from flask import Flask, request, jsonify, Response
from duckduckgo_search import DDGS # 🛡️ High-speed image scraper
import random
import os

app = Flask(__name__)

# ... aapka purana ahmad-dl wala code yahan rehne dein ...

@app.route('/find-img')
def find_image():
    query = request.args.get('q')
    if not query: return jsonify({"status": False, "msg": "Search query missing"})

    try:
        with DDGS() as ddgs:
            # 🔎 Query search karke images ki list nikaalna
            results = ddgs.images(query, region="wt-wt", safesearch="off", max_results=50)
            
            if results:
                # 🎲 RANDOMIZER: 50 results mein se koi bhi 1 random uthana
                random_choice = random.choice(results)
                return jsonify({
                    "status": True,
                    "query": query,
                    "image_url": random_choice['image'],
                    "source": random_choice['source']
                })
            else:
                return jsonify({"status": False, "msg": "No images found"})
                
    except Exception as e:
        return jsonify({"status": False, "error": str(e)})

# ... proxy-dl aur baqi code ...
