import pandas as pd

# Пример ключевых слов для различных тем (их можно расширить)
topic_keywords = {
    'Технологии': [
        'tech', 'iphone', 'apple', 'android', 'google', 'ai', 'software', 
        'innovation', 'cloud', 'robotics', '5g', 'machinelearning', 'gadget', 
        'cybersecurity', 'data', 'iot', 'blockchain', 'virtualreality', 'augmentedreality', 'startup'
    ],
    'Политика': [
        'election', 'government', 'vote', 'president', 'congress', 'senate', 
        'democracy', 'democrat', 'republican', 'impeachment', 'campaign', 
        'policy', 'tax', 'bills', 'politician', 'legislation', 'supremecourt', 
        'voterid', 'votingrights', 'civilrights', 'politicalparty', 'presidentialdebate', 'foreignpolicy'
    ],
    'Спорт': [
        'football', 'soccer', 'basketball', 'worldcup', 'nba', 'olympics', 
        'sports', 'athletics', 'team', 'goal', 'championship', 'superbowl', 
        'mvp', 'tournament', 'fifa', 'euros', 'formula1', 'athlete', 'rugby', 
        'baseball', 'hockey', 'boxing', 'wrestling', 'tennis'
    ],
    'Здоровье': [
        'covid', 'vaccine', 'health', 'pandemic', 'flu', 'hospital', 'mentalhealth', 
        'wellness', 'fitness', 'nutrition', 'exercise', 'medication', 'virus', 
        'healthcare', 'doctor', 'patient', 'surgery', 'prevention', 'healthyliving', 
        'vaccination', 'covid19', 'coronavirus', 'publichealth', 'disease', 'cancer', 'diabetes'
    ],
    'Экология': [
        'climate', 'environment', 'earth', 'sustainability', 'globalwarming', 'nature', 
        'pollution', 'recycling', 'greenenergy', 'conservation', 'carbonfootprint', 'wildlife', 
        'biodiversity', 'ecosystem', 'cleanenergy', 'renewable', 'forest', 'ocean', 'waterconservation', 
        'climatechange', 'greenhousegases', 'earthday', 'environmentalist', 'deforestation', 'co2', 'earthhour'
    ],
    'Развлечения': [
        'movie', 'music', 'hollywood', 'tv', 'celebrity', 'film', 'oscar', 
        'netflix', 'streaming', 'concert', 'actor', 'actress', 'popculture', 
        'tvshow', 'cinema', 'album', 'radio', 'videogames', 'gaming', 'band', 
        'comedy', 'theater', 'blockbuster', 'superhero', 'awardshow', 'streamer', 'podcast', 'tiktok', 'celebritynews'
    ],
    'Бизнес': [
        'economy', 'finance', 'stocks', 'investment', 'entrepreneur', 'startup', 
        'market', 'cryptocurrency', 'bitcoin', 'business', 'trade', 'shares', 
        'corporation', 'company', 'profit', 'sales', 'tax', 'fintech', 'investor', 
        'banking', 'ecommerce', 'funding', 'venturecapital', 'merger', 'acquisition', 'realestate'
    ],
    'Образование': [
        'school', 'university', 'college', 'student', 'education', 'degree', 
        'learning', 'teacher', 'classroom', 'graduation', 'scholarship', 
        'onlinelearning', 'elearning', 'academic', 'curriculum', 'research', 
        'exams', 'course', 'study', 'homework', 'educationpolicy', 'teachertraining', 'studentloan', 'highereducation'
    ],
    'Наука': [
        'science', 'research', 'discovery', 'physics', 'chemistry', 'biology', 
        'mathematics', 'astronomy', 'space', 'quantum', 'laboratory', 'experiment', 
        'genetics', 'cloning', 'biotechnology', 'fossils', 'climate', 'archaeology', 
        'medicalresearch', 'spaceexploration', 'scientist', 'innovation', 'scientificdiscovery', 'theory', 'robotics'
    ]
}

# Сохранение ключевых слов для каждой темы в отдельный файл
keywords_df = pd.DataFrame([(topic, keyword) for topic, keywords in topic_keywords.items() for keyword in keywords],
                           columns=['Topic', 'Keyword'])

keywords_df.to_csv(r'data\topic_keywords.csv', index=False, encoding='utf-8')

print("Ключевые слова по темам успешно сохранены в файл 'topic_keywords.csv'.")