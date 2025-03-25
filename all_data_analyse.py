import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy import stats

# Загрузка данных
data_dir = Path('data/')
all_files = list(data_dir.glob('2021_*_all_trends_data.csv'))
df_list = []

for file in sorted(all_files):
    df = pd.read_csv(file, parse_dates=['searched_at_datetime'])
    df['month'] = file.stem.split('_')[1].capitalize()
    df_list.append(df)

full_df = pd.concat(df_list, ignore_index=True)

# Очистка трендов (как в твоем коде)
full_df['trend_type'] = full_df['trend_name'].apply(lambda x: 'hashtag' if str(x).startswith('#') else 'keyword')
full_df['trend_clean'] = full_df['trend_name'].str.replace(r'^#', '', regex=True)

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

# Создание метки для каждой темы на основе ключевых слов
def assign_topic(trend_name):
    for topic, keywords in topic_keywords.items():
        if any(keyword.lower() in trend_name.lower() for keyword in keywords):
            return topic
    return 'Другие'

# Применение метки к трендам
full_df['topic'] = full_df['trend_clean'].apply(assign_topic)

# Исключаем тренды, которые попадают в категорию "Другие"
filtered_df = full_df[full_df['topic'] != 'Другие']

# Построение графика распределения трендов по темам (только для отфильтрованных данных)
plt.figure(figsize=(10, 6))
sns.countplot(data=filtered_df, x='topic', palette='Set2')
plt.title('Распределение трендов по темам (без категории "Другие")')
plt.xlabel('Тема')
plt.ylabel('Количество трендов')
plt.xticks(rotation=45)
plt.show()

# Построение графика активности трендов в течение дня
daily_activity = filtered_df.groupby([filtered_df['searched_at_datetime'].dt.date, filtered_df['searched_at_datetime'].dt.hour])['trend_name'].count().unstack().fillna(0)

plt.figure(figsize=(14, 6))
sns.heatmap(daily_activity.T, cmap="YlOrRd", cbar_kws={'label': 'Количество трендов'})
plt.title('Активность трендов в течение дня (по дням)')
plt.ylabel('Часы')
plt.xlabel('Дни')
plt.show()

# Группировка по дням недели для топ-трендов
filtered_df['hour'] = filtered_df['searched_at_datetime'].dt.hour
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
filtered_df['day_of_week'] = pd.Categorical(filtered_df['searched_at_datetime'].dt.day_name(), categories=days_order, ordered=True)

heatmap_data = filtered_df.pivot_table(index='day_of_week', columns='hour', values='tweet_volume', aggfunc='sum').fillna(0)

plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap="YlOrRd")
plt.title('Топ-тренды по дням недели и часам')
plt.xlabel('Часы')
plt.ylabel('Дни недели')
plt.show()

# Расчет продолжительности жизни трендов
duration = filtered_df.groupby('trend_name').agg(min=('searched_at_datetime', 'min'), max=('searched_at_datetime', 'max'))
duration['life_hours'] = (duration['max'] - duration['min']).dt.total_seconds() / 3600

# Построение гистограммы продолжительности трендов
plt.figure(figsize=(10, 6))
sns.histplot(duration['life_hours'], bins=50, kde=True)
plt.xlim(0, duration['life_hours'].quantile(0.95))  # Обрезаем выбросы
plt.title('Продолжительность жизни трендов')
plt.xlabel('Часы жизни тренда')
plt.ylabel('Количество трендов')
plt.show()

def compare_hashtags_keywords(df):
    """
    Сравнивает хэштеги и ключевые слова по:
    - продолжительности жизни
    - активности (твиты)
    - статистической значимости
    """
    # Классификация трендов
    df['type'] = df['trend_name'].apply(
        lambda x: 'hashtag' if isinstance(x, str) and x.startswith('#') else 'keyword'
    )
    
    # Расчет продолжительности
    duration = df.groupby(['trend_name', 'type']).agg(
        start=('searched_at_datetime', 'min'),
        end=('searched_at_datetime', 'max'),
        tweet_volume=('tweet_volume', 'sum')
    ).reset_index()
    
    duration['life_hours'] = (duration['end'] - duration['start']).dt.total_seconds() / 3600
    
    # Визуализация
    plt.figure(figsize=(12, 5))
    
    # График активности
    plt.subplot(1, 2, 2)
    sns.boxplot(data=duration, x='type', y='tweet_volume', showfliers=False)
    plt.title('Объем упоминаний')
    plt.ylabel('Твиты (log)')
    plt.yscale('log')
    
    plt.tight_layout()
    plt.show()
    
    # Статистический тест
    hashtag_life = duration[duration['type'] == 'hashtag']['life_hours']
    keyword_life = duration[duration['type'] == 'keyword']['life_hours']
    t_stat, p_val = stats.ttest_ind(hashtag_life, keyword_life, equal_var=False)
    
    # Результаты
    stats_df = duration.groupby('type').agg(
        mean_life=('life_hours', 'mean'),
        median_life=('life_hours', 'median'),
        mean_volume=('tweet_volume', 'mean'),
        count=('trend_name', 'count')
    )
    
    print(f"Статистическая значимость различий (p-value): {p_val:.4f}")
    return stats_df

# Пример использования
comparison_results = compare_hashtags_keywords(df)
print(comparison_results)