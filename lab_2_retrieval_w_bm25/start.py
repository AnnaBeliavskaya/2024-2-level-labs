"""
Laboratory Work #2 starter
"""
# pylint:disable=too-many-locals, unused-argument, unused-variable, too-many-branches, too-many-statements, duplicate-code
from lab_2_retrieval_w_bm25.main import (build_vocabulary, calculate_bm25, calculate_idf,
                                         calculate_tf, calculate_tf_idf, rank_documents,
                                         remove_stopwords, tokenize)


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
            documents.append(file.read())
    with open("assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    av_doc_len = sum(len(document) for document in documents) / len(documents)
    preprocessed_documents = []
    for doc in documents:
        tokenized_doc = tokenize(doc)
        if not isinstance(tokenized_doc, list):
            return
        preprocessed_doc = remove_stopwords(tokenized_doc, stopwords)
        if not isinstance(preprocessed_doc, list):
            return
        preprocessed_documents.append(preprocessed_doc)
    vocabulary = build_vocabulary(preprocessed_documents)
    tf = []
    for document in preprocessed_documents:
        if not isinstance(document, str):
            return
        tf_doc = calculate_tf(vocabulary, document)
        if not isinstance(tf_doc, list):
            return
        tf.append(tf_doc)
    tf_idf = []
    if not isinstance(vocabulary, list):
        return
    idf = calculate_idf(vocabulary, preprocessed_documents)
    if not isinstance(idf, list):
        return
    for tf_document in tf:
        tf_idf_doc = calculate_tf_idf(tf_document, idf)
        tf_idf.append(tf_idf_doc)
    bm25 = []
    for document in preprocessed_documents:
        bm25_doc = calculate_bm25(vocabulary,document,idf,1.5,0.75,av_doc_len,len(document))
        bm25.append(bm25_doc)
    query = 'Which fairy tale has Fairy Queen?'
    ranked_tf_idf = rank_documents(tf_idf, query, stopwords)
    ranked_bm25 = rank_documents(bm25, query, stopwords)

    result = ranked_bm25
    assert result, "Result is None"



if __name__ == "__main__":
    main()
