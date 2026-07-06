def calculate_ats_score(text):
    keywords ={
        "python","machine learning","deep learning","sql","tensor flow","pytorch","scikit-learn","numpy",
        "pandas","opencv","nlp","data analysis","streamlit","flask","git"
    }

    text = text.lower()

    score = 0
    found =[]

    for keyword in keywords:
        if keyword in text:
            score+= 100/len(keywords)
            found.append(keyword)
    return round(score),found