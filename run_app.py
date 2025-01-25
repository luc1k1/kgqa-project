from modules.pipeline import KGQAPipeline

if __name__ == "__main__":
    # Path to your Turtle file
    KG_FILE_PATH = "data/raw/small_dbpedia_subset.ttl"
    pipeline = KGQAPipeline(KG_FILE_PATH)

    while True:
        user_question = input("Ask a question (or 'exit')> ")
        if user_question.lower() == "exit":
            break
        answer = pipeline.answer_question(user_question)
        print("Answer:", answer)
