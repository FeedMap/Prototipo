from transformers import pipeline
import subprocess
import json
import re

distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    return_all_scores=True
)

def run_snscrape_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print('Erro ao executar o comando:', str(e))
        return None

def clean_text(text):
    # Remove caracteres especiais usando expressões regulares
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text.strip()

# Comando para baixar dados do Twitter usando Snscrape
twitter_command = ['snscrape', '--jsonl', '--max-results', '100', 'twitter-search', 'Caso Suzano']
output = run_snscrape_command(twitter_command)

if output is not None:
    tweets = output.split('\n')
    with open('Relatorio_suzano_twt.txt', 'w', encoding='utf-8') as file:
        for tweet in tweets:
            if tweet.strip():
                tweet_data = json.loads(tweet)
                raw_content = tweet_data['rawContent']
                cleaned_content = clean_text(raw_content)
                file.write(f"Raw Content: {raw_content}\n")
                file.write(f"Cleaned Content: {cleaned_content}\n")

                # Análise de Sentimento
                sentiment_results = distilled_student_sentiment_classifier(cleaned_content)

                for result in sentiment_results[0]:
                    label = result['label']
                    score = result['score']
                    file.write(f"Sentimento: {label}, Score: {score}\n")
                file.write("-----\n")
