# 🌐 Website Scraper Bot

A powerful AI-based web scraping and question-answering tool that extracts content from websites and allows users to interact with the data using a chat interface.

---

## 🚀 Features
- Scrape content from any website URL  
- Process and store text efficiently  
- Ask questions from scraped data using AI  
- Interactive chat-based UI using Streamlit  

---

## ⚙️ Step-by-Step Setup & Run Instructions

### 1️⃣ Prerequisites
- Python 3.10+ (Download from https://www.python.org/)
- أثناء installation, enable **"Add Python to PATH"**

**Verify Installation:**
```bash
python --version

or

python3 --version
2️⃣ Get the Code
git clone https://github.com/saisadhan1/Website_Scrapper_Bot
cd Website_Scrapper_Bot
3️⃣ Create Virtual Environment
OS	Commands
Windows	python -m venv venv
venv\Scripts\activate
macOS / Linux	python3 -m venv venv
source venv/bin/activate

✅ You should see (venv) in your terminal.

4️⃣ Install Dependencies
pip install -r requirements.txt

Includes:

streamlit
sentence-transformers
numpy
faiss-cpu
beautifulsoup4
requests
pandas
python-dotenv
tiktoken
langchain
openai
lxml
urllib3

👉 Optional (latest version):

pip install --upgrade streamlit
5️⃣ Run the Scraper (CLI)
python scraper.py
Enter website URL(s)
Specify number of characters (e.g., 1000)
6️⃣ Launch Interactive UI
streamlit run app.py

🌐 Opens in browser:

http://localhost:8501
Chat-based interface
Ask questions from scraped data
 Resources 
• Live demo (public): https://websitescrapperbot.streamlit.app/ 
• GitHub repo: https://github.com/saisadhan1/Website_Scrapper_Bot 
• Explanation video: https://drive.google.com/file/d/1aCc70yZa
iFtS7KPi_QFtcLgcYEI0g9m/view?usp=sharing
👤 Author

Saisadhan Kodurupaka
