📄 Resume Match & Analysis Web Application
This is a Flask-based web application that allows users to upload resumes (PDF, DOCX, TXT) and paste job descriptions to instantly analyze how well the resume matches the job using basic NLP techniques.

🧠 Features
📤 Upload resume in .pdf, .docx, or .txt formats

📋 Paste job description directly into the browser

🧮 Calculates and displays a match percentage

🧾 Extracts and previews raw resume and job description content

🎯 User-friendly web interface with a modern design

🔧 Tech Stack & Tools Used
Category	Tools / Libraries
Languages	Python, HTML, CSS
Framework	Flask, Jinja2
Parsing Tools	PyPDF2, docx2txt
Text Processing	Regular Expressions (re), Set Operations
Web Hosting	Localhost (Flask Dev Server)
Version Control	Git, GitHub
🚀 How to Run the Project
bash
Copy
Edit
git clone https://github.com/chotavali79/Resume-Match-Analysis-WebApp.git
cd Resume-Match-Analysis-WebApp
pip install -r requirements.txt
python app.py
Then open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
📸 UI Preview (Optional)
(Upload a screenshot to your repo and link it here)

scss
Copy
Edit
![Web UI](screenshots/app-preview.png)
📂 Project Structure
sql
Copy
Edit
Resume-Match-Analysis-WebApp/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── uploaded_resumes/
├── sample_jd.txt
└── README.md
🧠 What You’ll Learn
Flask basics: routing, file handling, form processing

Resume parsing using PyPDF2 and docx2txt

Text comparison using set intersection (basic NLP)

Web app deployment concepts

GitHub project publishing 🚀

👨‍💻 Author
Shaik Chotavali
GitHub • LinkedIn

🌟 Like this project?
Don’t forget to ⭐ star the repo and give your feedback!
