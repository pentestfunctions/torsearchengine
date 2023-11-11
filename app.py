from flask import Flask, request, render_template
import urllib.parse
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        keywords = request.form.get("keywords")
        selected_engine = request.form.get("search_engine")

        if not keywords:
            message = "No keywords provided."
            return render_template("index.html", message=message)

        encoded_keywords = urllib.parse.quote(keywords.encode("utf-8"))

        search_engines = {
            "ahmia": "https://ahmia.fi/search/?q={}",
            "excavator": "http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion.ly/search/{}",
            "torch": "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion.ly/search?query={}",
            "deepsearch": "http://search7tdrcvri22rieiwgi5g46qnwsesvnubqav2xakhezv4hjzkkad.onion.ly/result.php?search={}",
            "underdir": "http://underdiriled6lvdfgiw4e5urfofuslnz7ewictzf76h4qb73fxbsxad.onion.ly/?search={}",
            "onionland": "https://onionland.io/search?q={}",
            "grams": "http://grams64rarzrk7rzdaz2fpb7lehcyi7zrrf5kd6w2uoamp7jw2aq6vyd.onion.ly/search?key={}"
        }

        if selected_engine not in search_engines:
            selected_engine = "ahmia"
            message = "Invalid search engine selected, setting default to ahmia."
            return render_template("index.html", message=message)

        search_url = search_engines[selected_engine].format(encoded_keywords)

        if selected_engine == "ahmia":
            search_command = f"curl -s '{search_url}' | grep -oE 'http[s]?://[^/]+\\.onion' 2>/dev/null | head -n 15 > domains.txt 2>/dev/null"
        elif selected_engine == "excavator":
            search_command = f"curl -s '{search_url}' | grep -A 400 '<h6>SEARCH RESULTS</h6>' | grep -oE 'http[s]?://[^/]+\\.onion' | head -n 15 > domains.txt 2>/dev/null"
        elif selected_engine == "torch":
            search_command = f"curl -s '{search_url}' | grep -A 800 'Your search' | grep -oE 'http[s]?://[^/]+\\.onion' 2>/dev/null | uniq -u | head -n 15 > domains.txt 2>/dev/null"
        elif selected_engine == "deepsearch":
            search_command = f"curl -s '{search_url}' | grep -oE 'http[s]?://[^/]+\\.onion' 2>/dev/null | head -n 40 | uniq > domains.txt 2>/dev/null"
        elif selected_engine == "underdir":
            search_command = f"curl -s '{search_url}' | grep -oE 'http[s]?://[^/]+\\.onion' 2>/dev/null | head -n 20 > domains.txt 2>/dev/null"
        elif selected_engine == "onionland":
            search_command = f"curl -s '{search_url}' | grep -oE 'http[s]?://[^/]+\\.onion' 2>/dev/null | head -n 40 | uniq > domains.txt 2>/dev/null"
        elif selected_engine == "grams":
            search_command = f"curl -s '{search_url}' | grep -A 800 '<ul>' | grep -oE 'http[s]?://[^/]+\\.onion' 2>/dev/null | head -n 15 > domains.txt 2>/dev/null"
        else:
            search_command = "echo 'Invalid search engine'"

        # Execute the search command
        try:
            os.system(search_command)
            # Read the contents of domains.txt
            with open('domains.txt', 'r') as file:
                domains = file.readlines()
            # Clean up the domains list
            domains = [domain.strip() for domain in domains]
        except Exception as e:
            return render_template("index.html", message=str(e))

        return render_template("index.html", domains=domains)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
