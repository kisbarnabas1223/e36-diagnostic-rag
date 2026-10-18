🚗 BMW E36 AI Diagnosztikai Asszisztens (Lokális RAG)

Egy teljesen offline, saját gépen futó AI asszisztens, ami a BMW E36 gyári szervizkönyve alapján ad pontos diagnosztikai és szerelési tippeket.



💡 Miért csináltam?

Szerettem volna a gyakorlatban is kipróbálni az AI Engineering (konkrétan a RAG - Retrieval-Augmented Generation) alapjait. Ahelyett, hogy egy 1154 oldalas angol PDF-ben keresgélnék a Ctrl+F-fel, a lokális gép dolgozik helyettem.



🛠️ Tech Stack 

Nyelv: Python 3.11

Vektor Adatbázis: FAISS (Facebook AI Similarity Search)

Szövegdarabolás: LangChain (PyMuPDFLoader, RecursiveCharacterTextSplitter)

Embedding Modell: HuggingFace BAAI/bge-m3 (A nyers szöveg vektorokká alakítása)

LLM: Ollama + Qwen2.5:7b lokálisan futtatva.



⚙️ Hogyan működik?

A projekt két fő szkriptből áll:

ingest.py:  Beolvassa a docs/ mappában lévő PDF-eket, logikai darabokra vágja őket, matematikai vektorokká alakítja, és elmenti a faiss_index mappába. Csak egyszer kell lefuttatni.

diagnose.py: Bekéri a hibakódot vagy tünetet, a FAISS adatbázisból kikeresi a 3 leginkább passzoló gyári bekezdést, majd ezt odaadja a Qwen modellnek, hogy fogalmazza meg a pontos választ.



🚀 Telepítés és Futtatás

1. Előfeltételek:

Python 3.11 telepítve.

Ollama letöltve és futtatva.

A Qwen modell letöltése terminálból.

2. Környezet beállítása:

**Repo klónozása és belépés**
```bash
git clone https://github.com/kisbarnabas1223/e36-diagnostic-rag.git
cd e36-diagnostic-rag
```

**Virtuális környezet (venv) létrehozása és aktiválása**
```bash
python -m venv venv
source venv/Scripts/activate # Windowson (Bash)
```

**Függőségek telepítése**
```bash
pip install -r requirements.txt
```

3. Adatbázis építése: Tedd be a szervizkönyv PDF-eket a docs/ mappába, majd:
```bash
python ingest.py
```


4. Kérdezz-Felelek indítása:

python diagnose.py




⚠️ Ismert limitációk

Mivel egy kisebb, 7 milliárd paraméteres (7B) modellt használ a rendszer, a magyar nyelvű műszaki fordítások (pl. Volt és Ohm megkülönböztetése) olykor pontatlanok lehetnek. A maximális mérnöki precizitás érdekében a kód jelenleg az angol nyelvű lekérdezésre van optimalizálva.

Készült hobbiból és tanulási célzattal.