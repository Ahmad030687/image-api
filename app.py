from flask import Flask, request, jsonify
from duckduckgo_search import DDGS
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🖼️ AHMAD RDX IMAGE ENGINE - DYNAMIC MODE"

@app.route('/find-img')
def find_image():
    query = request.args.get('q')
    # User jitni mangay ga (count), default 1 rakha hai
    count = request.args.get('count', default=1, type=int)
    
    if not query:
        return jsonify({"status": False, "msg": "Search query missing!"})

    try:
        with DDGS() as ddgs:
            # 50 results nikaalte hain variety ke liye
            results = list(ddgs.images(query, region="wt-wt", safesearch="off", max_results=50))
            
            if results:
                # Limit 10 rakhi hai taake Messenger crash na ho
                limit = min(len(results), count, 10)
                # 🎲 50 mein se 'limit' jitni random unique images uthana
                random_images = random.sample(results, limit)
                
                output = [{"url": img.get('image')} for img in random_images]
                
                return jsonify({
                    "status": True,
                    "count": len(output),
                    "data": output
                })
            else:
                return jsonify({"status": False, "msg": "No images found"})
                
    except Exception as e:
        return jsonify({"status": False, "error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
