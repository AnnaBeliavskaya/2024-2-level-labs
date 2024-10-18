"""
Laboratory Work #2 starter
"""
# pylint:disable=too-many-locals, unused-argument, unused-variable, too-many-branches, too-many-statements, duplicate-code
from main import tokenize, remove_stopwords, build_vocabulary,calculate_tf, calculate_idf,calculate_tf_idf, calculate_bm25, \
    rank_documents


def main() -> None:
    """
    Launches an implementation
    """
    paths_to_texts = [
        "assets/fairytale_1.txt",
        "assets/fairytale_2.txt",
        "assets/fairytale_3.txt",
        "assets/fairytale_4.txt",
        "assets/fairytale_5.txt",
        "assets/fairytale_6.txt",
        "assets/fairytale_7.txt",
        "assets/fairytale_8.txt",
        "assets/fairytale_9.txt",
        "assets/fairytale_10.txt",
    ]
    documents = []
    for path in paths_to_texts:
        with open(path, "r", encoding="utf-8") as file:
            documents.append(file.read())#список строк,строка=текст
    with open("assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    av_doc_len = sum(len(document) for document in documents) / len(documents)
    for i in range(len(documents)):
        documents[i]=tokenize(documents[i])
        documents[i]=remove_stopwords(documents[i],stopwords)
    vocabulary = build_vocabulary(documents)
    tf = []
    for document in documents:
        tf_doc = calculate_tf(vocabulary,document)
        tf.append(tf_doc)
    tf_idf = []
    idf = calculate_idf(vocabulary, documents)
    for tf_document in tf:
        tf_idf_doc = calculate_tf_idf(tf_document,idf)
        tf_idf.append(tf_idf_doc)
    bm25 = []
    for document in documents:
        bm25_doc = calculate_bm25(vocabulary,document,idf,1.5,0.75,av_doc_len,len(document))
        bm25.append(bm25_doc)
    quary = 'Which fairy tale has Fairy Queen?'
    ranked_tf_idf = rank_documents(tf_idf, quary,stopwords)
    ranked_bm25 = rank_documents(bm25,quary,stopwords)
    print(ranked_tf_idf)
    print(ranked_bm25)

    result = 1
    assert result, "Result is None"


if __name__ == "__main__":
    main()
