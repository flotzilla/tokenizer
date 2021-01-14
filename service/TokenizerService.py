from nltk.tokenize import WordPunctTokenizer


class TokenizeService:

    def split(self, text: str):
        return WordPunctTokenizer().tokenize(text)

    def split(self, data: []) -> []:
        resp = []
        tokenizer = WordPunctTokenizer()
        for d in data:
            resp.append(tokenizer.tokenize(d))

        return resp
