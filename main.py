import os

project_files = {
    "persona_generator.py": """
import praw
from jinja2 import Environment, FileSystemLoader
import pdfkit
from urllib.parse import urlparse
import os
from collections import Counter, defaultdict
import re

# Reddit API Setup
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    user_agent='persona_generator'
)

# Template loader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

def extract_username(url):
    return urlparse(url).path.split('/')[2]

def fetch_data(username, limit=50):
    user = reddit.redditor(username)
    posts = [(post.title, post.selftext) for post in user.submissions.new(limit=limit)]
    comments = [c.body for c in user.comments.new(limit=limit)]
    return posts, comments

def infer_persona(posts, comments):
    text = " ".join([p[0] + " " + p[1] for p in posts] + comments)
    persona = {
        "name": f"u/{username}",
        "age": re.search(r"\\bI'?m (\\d{1,2})\\b", text).group(1) if re.search(r"\\bI'?m (\\d{1,2})\\b", text) else "Unknown",
        "occupation": "Student" if "university" in text or "college" in text else "Unknown",
        "status": "Single",
        "location": "Unknown",
        "tier": "Early Adopter",
        "archetype": "Explorer",
        "traits": ["Curious", "Active", "Practical"],
        "motivations": {
            "convenience": text.count("quick") + text.count("easy"),
            "wellness": text.count("healthy") + text.count("exercise"),
            "speed": text.count("fast"),
            "comfort": text.count("relax"),
            "preferences": text.count("prefer"),
        },
        "personality": {
            "Introvert vs Extrovert": 5,
            "Feeling vs Thinking": 7,
            "Judging vs Perceiving": 5,
            "Intuition vs Sensing": 3
        },
        "habits": [
            "Posts mostly in tech-related subreddits.",
            "Prefers commenting over posting.",
            "Mentions staying up late coding."
        ],
        "frustrations": [
            "Too many frameworks to learn.",
            "Tutorials skip hard parts.",
            "Overpriced courses."
        ],
        "goals": [
            "Become a better developer.",
            "Stay consistent with practice.",
            "Land a tech internship."
        ]
    }
    return persona

def render_pdf(persona, filename):
    html = template.render(**persona)
    output_path = os.path.join("persona_output", filename)
    os.makedirs("persona_output", exist_ok=True)
    pdfkit.from_string(html, output_path)
    print(f"PDF saved to {output_path}")

if __name__ == "__main__":
    input_url = input("Enter Reddit user profile URL: ").strip()
    username = extract_username(input_url)
    posts, comments = fetch_data(username)
    persona = infer_persona(posts, comments)
    render_pdf(persona, f"{username}_persona.pdf")
""",
    "template.html": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>User Persona: {{ name }}</title>
    <style>
        body { font-family: sans-serif; padding: 30px; }
        h1 { color: #ff6600; }
        .section { margin-bottom: 25px; }
        .bar { background: #ddd; width: 100%; height: 10px; position: relative; margin: 5px 0; }
        .fill { background: #ff6600; height: 10px; }
    </style>
</head>
<body>
    <h1>{{ name }}</h1>
    <p><strong>Age:</strong> {{ age }} | <strong>Occupation:</strong> {{ occupation }} | <strong>Status:</strong> {{ status }}</p>
    <p><strong>Location:</strong> {{ location }} | <strong>Tier:</strong> {{ tier }} | <strong>Archetype:</strong> {{ archetype }}</p>

    <div class="section">
        <h2>Traits</h2>
        <p>{{ traits | join(' | ') }}</p>
    </div>

    <div class="section">
        <h2>Motivations</h2>
        {% for item, val in motivations.items() %}
            <p>{{ item.capitalize() }}</p>
            <div class="bar"><div class="fill" style="width:{{ val*10 }}%"></div></div>
        {% endfor %}
    </div>

    <div class="section">
        <h2>Personality</h2>
        {% for trait, val in personality.items() %}
            <p>{{ trait }}</p>
            <div class="bar"><div class="fill" style="width:{{ val*10 }}%"></div></div>
        {% endfor %}
    </div>

    <div class="section">
        <h2>Behaviour & Habits</h2>
        <ul>
            {% for line in habits %}
            <li>{{ line }}</li>
            {% endfor %}
        </ul>
    </div>

    <div class="section">
        <h2>Frustrations</h2>
        <ul>
            {% for f in frustrations %}
            <li>{{ f }}</li>
            {% endfor %}
        </ul>
    </div>

    <div class="section">
        <h2>Goals & Needs</h2>
        <ul>
            {% for g in goals %}
            <li>{{ g }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""
}

# Save the files reddit_persona_exporter/
base_path = "reddit_persona_exporter"
os.makedirs(base_path, exist_ok=True)
for filename, content in project_files.items():
    with open(os.path.join(base_path, filename), "w", encoding="utf-8") as f:
        f.write(content.strip())

base_path
