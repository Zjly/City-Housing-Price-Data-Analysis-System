from emotion.emotion_analysis import emotion_analysis
from emotion.database_operating import get_data, save_emotion_score
from emotion.participle import participle

data = get_data()
news_cut_list = participle(data)
emotion_data = emotion_analysis(news_cut_list)
save_emotion_score(emotion_data)
