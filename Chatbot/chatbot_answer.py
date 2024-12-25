import json
import nltk
from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

with open('data.json', 'r', encoding='utf-8') as dosya:
    veriler = json.load(dosya)

durak_kelimeler = stopwords.words("turkish")

def metni_temizle(metin):
    kelimeler = word_tokenize(metin.lower())
    temiz_kelime = [kelime for kelime in kelimeler if kelime not in durak_kelimeler and kelime.isalnum()]
    return " ".join(temiz_kelime)

def cevap_ver(metin):
    temiz_soru = metni_temizle(metin)

    en_iyi_eslesme = None
    en_iyi_skor = 0
    for veri in veriler.values():
        for soru in veri['soru']:
            temiz_soru_karşılaştır = metni_temizle(soru)

            benzerlik_skoru = fuzz.token_sort_ratio(temiz_soru, temiz_soru_karşılaştır)

            if benzerlik_skoru > en_iyi_skor:
                en_iyi_skor = benzerlik_skoru
                en_iyi_eslesme = veri['cevap'][0]

    if en_iyi_skor > 70:
        return en_iyi_eslesme
    else:
        return "Üzgünüm, bunu anlayamadım."
