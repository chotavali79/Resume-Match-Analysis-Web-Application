from flask import Flask, render_template, request
import PyPDF2
import docx2txt
import os
import re

app = Flask(__name__)

def extract_text(file):
    filename = file.filename
    if filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text
    elif filename.endswith('.docx'):
        return docx2txt.process(file)
    elif filename.endswith('.txt'):
        return file.read().decode('utf-8')
    else:
        return ''



def calculate_match_score(resume_text, jd_text):
    # Preprocessing: lowercase, remove punctuation, tokenize
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b\w+\b', jd_text.lower()))
    
    if not jd_words:
        return 0.0
    
    common_words = resume_words.intersection(jd_words)
    score = (len(common_words) / len(jd_words)) * 100
    return round(score, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume_file = request.files['resume']
        jd_text = request.form['jd']

        if not resume_file or not jd_text.strip():
            return render_template('index.html', error="Please upload a resume and paste job description.")

        resume_text = extract_text(resume_file)
        score = calculate_match_score(resume_text, jd_text)

        return render_template('index.html', score=score, resume_content=resume_text, jd_content=jd_text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
