# Reddit User Persona Generator (PDF Exporter)

This project allows you to generate a **visual PDF persona** for any Reddit user based on their posts and comments.  
It uses the Reddit API, some basic NLP rules, and exports the result using an HTML template and PDF conversion.

---

## Features

- Scrapes Reddit user posts and comments
- Infers user traits: age, occupation, behavior, motivations, etc.
- Generates a professional-looking PDF persona
- 100% local — does not use any GPT or LLM

---

## 🛠️ Requirements

- Python 3.7+
- Reddit Developer App credentials
- `wkhtmltopdf` installed on your system (used by `pdfkit`)

---

## 📦 Setup

### 1. Clone or Download

Download the directory or clone:

```bash
git clone https://github.com/yourusername/assignment.git
cd assignment
```

### 2. Install dependencies

```
bash
pip install -r requirements.txt
```

Also install wkhtmltopdf:

#### Ubuntu/Debian:

```bash
sudo apt install wkhtmltopdf
```

#### macOS (with Homebrew):

```bash
brew install wkhtmltopdf
```

#### Windows:
Download installer from https://wkhtmltopdf.org/downloads.html
Then, add its installation folder (with bin) to your PATH.

### Reddit API Setup

- Go to https://www.reddit.com/prefs/apps
- Click "create an app" → type: script

#### Note down:
- client_id

- client_secret

- username

- password

Edit assignment.py and replace:
```
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    user_agent='persona_generator'
)
```

### Run the Script
```
python main.py

Enter Reddit user profile URL: https://www.reddit.com/user/Hungry-Move-6603/
```

### Output
- The generated PDF includes:
- Age, location, status, archetype
- Motivations and personality (as bar charts)
- Behaviors, frustrations, and goals
- Clean professional layout based on a UX persona template


