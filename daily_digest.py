# daily_digest.py

import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from dotenv import load_dotenv
import feedparser
import gspread
from google.oauth2.service_account import Credentials

# Load environment variables
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")  # Your own email
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "Daily Digest")

# Setup Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
GOOGLE_CREDS_JSON = os.getenv("GOOGLE_CREDS_JSON")
creds = Credentials.from_service_account_file(GOOGLE_CREDS_JSON, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open(GOOGLE_SHEET_NAME).worksheet("Digest")

# ---------- Data Sources ----------
def get_f1_highlights():
    try:
        response = requests.get("https://ergast.com/api/f1/current/last/results.json")
        data = response.json()
        race = data['MRData']['RaceTable']['Races'][0]
        race_name = race['raceName']
        circuit = race['Circuit']['circuitName']
        race_date = race['date']
        winner = race['Results'][0]['Driver']
        driver_name = f"{winner['givenName']} {winner['familyName']}"
        constructor = race['Results'][0]['Constructor']['name']
        return f"🏁 F1: {race_name} at {circuit} on {race_date}\n🥇 Winner: {driver_name} ({constructor})"
    except Exception:
        return "🏎️ No F1 news available."

def get_leetcode_daily():
    try:
        return "🧠 Visit https://leetcode.com for today’s challenge (LeetCode blocks scrapers)."
    except:
        return "🧠 Couldn't fetch LeetCode daily."

def get_github_trending():
    try:
        url = "https://github.com/trending/python"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        repo = soup.select("h2 a")[0]
        title = repo.text.strip().replace("\n", "").replace(" ", "")
        link = "https://github.com" + repo["href"]
        return f"📈 GitHub Trending: {title}\n🔗 {link}"
    except:
        return "📈 Could not fetch GitHub trending."

def get_youtube_video():
    try:
        feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UCt3kSliZl7LO3gQ9hM3Gb6g")
        if feed.entries:
            video = feed.entries[0]
            return f"📺 YouTube Pick: {video.title}\n🔗 {video.link}"
        return "📺 No YouTube video found."
    except:
        return "📺 No YouTube video found."

def get_podcast():
    try:
        feed = feedparser.parse("https://feeds.twit.tv/twit.xml")
        if feed.entries:
            ep = feed.entries[0]
            return f"🎙️ Podcast: {ep.title}\n🔗 {ep.link}"
        return "🎙️ No podcast found."
    except:
        return "🎙️ No podcast found."

def get_tech_news():
    try:
        url = "https://news.ycombinator.com"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        story = soup.find("span", class_="titleline")
        if story:
            link = story.find("a")
            return f"🗞️ Tech News: {link.text.strip()}\n🔗 {link['href']}"
        return "🗞️ Could not fetch tech news."
    except:
        return "🗞️ Could not fetch tech news."

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        res = requests.get(url).json()
        return f"😂 Joke: {res['setup']} — {res['punchline']}"
    except:
        return "😂 Couldn't fetch joke."

# ---------- Email Sending ----------
def write_digest_to_file(content):
    filename = f"digest_{date.today().isoformat()}.txt"
    with open(filename, "w") as f:
        f.write(content)
    return filename

def send_digest_email(filename, content, recipient_emails):
    msg = EmailMessage()
    msg["Subject"] = "🗞️ Your Daily Tech Digest"
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(recipient_emails)
    msg.set_content(content)

    with open(filename, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="plain", filename=filename)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)

# ---------- Feedback ----------
def parse_feedback(feedback_input):
    completed = []
    liked = []
    disliked = []

    lines = feedback_input.strip().splitlines()
    for line in lines:
        if "✔️" in line:
            completed += [item.strip() for item in line.split("✔️")[-1].split(",")]
        elif "👍" in line:
            liked += [item.strip() for item in line.split("👍")[-1].split(",")]
        elif "👎" in line:
            disliked += [item.strip() for item in line.split("👎")[-1].split(",")]
    return completed, liked, disliked

def record_feedback_to_sheet(client, completed, liked, disliked):
    try:
        feedback_sheet = None
        try:
            feedback_sheet = client.open(GOOGLE_SHEET_NAME).worksheet("Feedback")
        except gspread.exceptions.WorksheetNotFound:
            feedback_sheet = client.open(GOOGLE_SHEET_NAME).add_worksheet(title="Feedback", rows="100", cols="20")
            feedback_sheet.append_row(["Date", "Completed Tasks", "Liked", "Disliked"])

        today = date.today().isoformat()
        feedback_sheet.append_row([
            today,
            ", ".join(completed),
            ", ".join(liked),
            ", ".join(disliked)
        ])
        print("✅ Feedback recorded in the sheet.")
    except Exception as e:
        print(f"❌ Failed to log feedback: {e}")

# ---------- Main Function ----------
def main():
    today = date.today().isoformat()
    
    f1 = get_f1_highlights()
    leetcode = get_leetcode_daily()
    github = get_github_trending()
    youtube = get_youtube_video()
    podcast = get_podcast()
    news = get_tech_news()
    joke = get_joke()

    row = [today, f1, leetcode, github, youtube, podcast, news, joke]
    sheet.append_row(row)

    digest_text = f"""🗞️ DAILY TECH DIGEST — {today}

{f1}

{leetcode}

{github}

{youtube}

{podcast}

{news}

{joke}
"""

    filename = write_digest_to_file(digest_text)
    send_digest_email(filename, digest_text, [TO_EMAIL])

    # To-Do Display
    print("\n✅ To-Do Checklist:")
    tasks = [
        "Solve LeetCode Daily",
        "Check GitHub Trending",
        "Watch YouTube video",
        "Listen to Podcast",
        "Read Tech News",
        "Catch up on F1"
    ]
    for task in tasks:
        print(f"[ ] {task}")

    # Feedback
    print("\nReply with ✔️ for completed items. Also tell me which ones you liked (👍) or didn’t like (👎) – I’ll learn from your feedback!")
    feedback_input = input("\n🗣️ Your Feedback:\n")
    completed, liked, disliked = parse_feedback(feedback_input)
    record_feedback_to_sheet(client, completed, liked, disliked)

# ---------- Run ----------
if __name__ == "__main__":
    main()

