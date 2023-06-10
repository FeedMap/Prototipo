from transformers import pipeline

distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    return_all_scores=True
)


while True:
    input_text = input("Digite o texto de entrada (ou 'sair' para encerrar): ")

    if input_text.lower() == 'sair':
        break

    results = distilled_student_sentiment_classifier(input_text)

    for result in results[0]:
        label = result['label']
        score = result['score']
        print(f"Sentimento: {label}, Score: {score}")
