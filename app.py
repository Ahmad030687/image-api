from flask import Flask, request, jsonify
from duckduckgo_search import DDGS
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🖼️ AHMAD RDX IMAGE ENGINE - DYNAMIC MODE LIVE"

@app.route('/find-img')
def find_image():
    query = request.args.get('q')
    count = request.args.get('count', default=1, type=int) # Default 1
    
    if not query:
        return jsonify({"status": False, "msg": "Query missing!"})

    try:
        with DDGS() as ddgs:
            # Variety ke liye 50 results nikaalte hain
            results = list(ddgs.images(query, region="wt-wt", safesearch="off", max_results=50))
            
            if results:
                # Jitni user ne mangi hain (max 10)
                limit = min(len(results), count, 10) 
                random_images = random.sample(results, limit)
                
                output = []
                for img in random_images:
                    output.append({
                        "url": img.get('image')
                    })
                
                return jsonify({
                    "status": True,
                    "count": limit,
                    "data": output
                })
            else:
                return jsonify({"status": False, "msg": "No images found"})
                
    except Exception as e:
        return jsonify({"status": False, "error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
