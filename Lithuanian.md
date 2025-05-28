**8 Savaičių Praktinis Kursas: Taikomųjų Programų Kūrimas su GEN-AI ir Python**

---

## **1 Savaitė: Python Pagrindai ir Aplinkos Paruošimas**

### **1 Diena: Kurso Įvadas ir Aplinkos Paruošimas**
- Kurso apžvalga, tikslai.
- Python diegimas ir PATH konfigūravimas.
- Virtualios Aplinkos: `venv`/`uv` naudojimas.
- IDE Sąranka: VSCode pagrindai, plėtiniai.
- ChatGPT, Vibe coding intro.

### **2 Diena: Python Pagrindai**
- Duomenų Tipai: Skaičiai, Eilutės, Loginės reikšmės.
- Duomenų Struktūros: Sąrašai, Kortežai, Žodynai, Aibės.
- Valdymo Srautai: `if`/`elif`/`else`, `for`/`while`.
- Derinimo Įvadas: `print`, atsekimo informacija, IDE derintuvas.

### **3 Diena: Python Būtiniausi Dalykai GEN-AI**
- Funkcijos: `def`, argumentai, grąžinamos reikšmės, apimtis.
- Klaidų Apdorojimas: `try...except`.
- Moduliai ir Paketai: `import`, standartinė biblioteka (`os`, `math`), diegimas (`uv`).
- Kodo Stilius: PEP 8, moduliarumas.
- **Praktika:** Teksto manipuliavimo pagalbinės funkcijos.

### **4 Diena: Darbas su Bibliotekomis ir Duomenimis**
- HTTP Pagrindai: Metodai, būsenos kodai.
- `requests` Biblioteka: API užklausos, atsakymai.
- `json` Biblioteka: Analizė (`loads()`) ir serializavimas (`dumps()`).
- Duomenų Tvarkymo Įvadas: `numpy` masyvai, darbas su failais.
- **Praktika:** Gauti ir apdoroti API duomenis; pasirinktinai išsaugoti failuose.

### **5 Diena: Įvadas į API ir Pagrindinių Programų Kūrimas**
- API Koncepcijos: REST, API raktai.
- Programos Struktūra: CLI dizainas.
- **Praktika:** Sukurti CLI programą, kuri kviečia API pagal vartotojo įvestį.

---

## **2 Savaitė: Įvadas į Generatyvųjį DI ir API Integracija**

### **1 Diena: Kas yra Generatyvusis DI?**
- Apibrėžimas, istorija, koncepcijos (LLM, užklausos, žetonai).
- Pagrindiniai modeliai/veikėjai (OpenAI, Google).
- Etika: Šališkumas, piktnaudžiavimas.
- Demo: Teksto/vaizdo generavimas (ChatGPT, Midjourney).

### **2 Diena: REST API ir Įvadas į FastAPI**
- RESTful API apžvalga.
- Įvadas į FastAPI: Savybės, sąranka (`uvicorn`).
- Kelio Operacijos: Maršrutai (`@app.get`/`@app.post`), kelio/užklausos parametrai.
- Užklausos Kūnas: Pydantic validacija.
- **Praktika:** Paprasta FastAPI „Hello World“ API; tyrinėti Swagger UI.

### **3 Diena: Darbas su OpenAI GPT API**
- OpenAI Platforma: Modeliai (GPT-4/3.5), kainodara.
- API Raktų Valdymas ir Saugumas.
- OpenAI Python Biblioteka: Diegimas (`uv add openai`), naudojimas.
- Pokalbių Užbaigimo API: `openai.chat.completions.create`, rolės.
- Pagrindiniai Parametrai: `model`, `messages`, `temperature`, `max_tokens`.
- **Praktika:** Python scenarijus, naudojantis GPT API užklausoms/atsakymams.

### **4 Diena: OpenAI Modeliai: Galimybės, Apribojimai ir Užklausų Kūrimas**
- Modelio Galimybės/Apribojimai (žinių riba, haliucinacijos).
- Užklausų Inžinerijos Pagrindai: Kontekstas, formatas, zero/few-shot.
- Įvadas: Įrankiai/Funkcijų kvietimas.
- Įvadas: Asistentų API (būsenos palaikymas).
- **Praktika:** Eksperimentuoti su užklausų inžinerija; pasirinktinai funkcijų kvietimas.

### **5 Diena: OpenAI Integravimas su FastAPI**
- Programos Struktūra: FastAPI + OpenAI.
- Saugus API Raktų Tvarkymas: Aplinkos kintamieji (`python-dotenv`).
- API Galinis Taškas (`/generate`): Priima užklausą, kviečia OpenAI.
- Atsakymo Grąžinimas: JSON formatas.
- **Praktika:** FastAPI galinis taškas, priimantis užklausą, kviečiantis OpenAI, grąžinantis atsakymą.

---

## **3 Savaitė: Google Gemini ir UI su Streamlit**

### **0 Diena: „Vibe coding“ pamoka (Cursor ir Copilot)**
- Įvadas į DI kodo asistentus: Cursor, Copilot.
- Sąranka, pagrindinis naudojimas (pokalbiai, kodo generavimas).
- DI porinio programavimo patarimai.

### **1 Diena: Google AI Studio ir Vertex AI Tyrinėjimas**
- Google DI Ekosistema: Vertex AI apžvalga.
- Google AI Studio: Gemini prototipų kūrimas internetu.
- Gemini Modeliai: Pro, Flash.
- Praktika: Užklausų kūrimas, parametrai, saugos nustatymai AI Studio.
- **Praktika:** Naudoti AI Studio teksto užduotims (generavimas, santrauka, Q&A) su Gemini.

### **2 Diena: Programavimas su Google Gemini API**
- Google AI Python SDK: Diegimas (`uv add google-generativeai`), sąranka.
- Autentifikacija: API raktai.
- API Kvietimai: `GenerativeModel.generate_content`.
- Srautiniai Atsakymai: Fragmentų tvarkymas.
- **Praktika:** Python scenarijus, naudojantis Gemini API teksto generavimui (įskaitant srautinį).

### **3 Diena: Įvadas į Streamlit UI Kūrimui**
- Streamlit Pagrindai: Greitas UI, vykdymo modelis, kešavimas.
- Pagrindiniai Valdikliai: Tekstas (`st.write`), įvestis (`st.text_input`, `st.button`), išdėstymas (`st.columns`, `st.sidebar`).
- Duomenų Rodymas: Duomenų rėmai (`st.dataframe`), paprastos diagramos.
- **Praktika:** Sukurti paprastą Streamlit programą su įvairiais valdikliais/išdėstymu.

### **4 Diena: Streamlit Pokalbių Robotų Kūrimas su Gemini**
- Pokalbių UI: `st.chat_input`, `st.chat_message`.
- Būsenos Valdymas: `st.session_state` istorijai.
- Integracija: Sujungti Streamlit I/O su Gemini API.
- Eiga: Įvestis -> Istorija -> API kvietimas -> Rodymas -> Istorija.
- **Praktika:** Paprastas Streamlit pokalbių robotas naudojant `st.session_state` ir Gemini API.

### **5 Diena: Projekto Darbas ir Peržiūra**
- Projekto darbo laikas.
- Instruktoriaus Q&A.
- 3 Savaitės peržiūra: Gemini API, Streamlit, būsenos valdymas.
- Diskusija: Iššūkiai, idėjos.

---

## **4 Savaitė: Įvadas į Retrieval-Augmented Generation (RAG)**

### **1 Diena: Kas yra RAG? Pagrindinės Koncepcijos ir Panaudojimo Atvejai**
- Problema: LLM apribojimai (žinių riba, haliucinacijos).
- RAG Koncepcija: Gauti info, tada generuoti.
- Architektūra: Ieškiklis + Generatorius (LLM).
- Privalumai: Įžeminimas, faktinis nuoseklumas, srities žinios.
- Panaudojimo Atvejai: Pokalbių robotai, Q&A su privačiais duomenimis, santraukos.
- **Veikla:** Generuoti RAG taikymo idėjas.

### **2 Diena: RAG Įgyvendinimas su Langchain**
- Įvadas į LangChain: Orkestravimas (Komponentai, Grandinės).
- RAG Komponentai: Įkrovikliai, Skaidytojai, Įterpiniai, Vektorinės Saugyklos, Ieškikliai, LLM.
- `RetrievalQA` Grandinė: Pagrindinis RAG Q&A.
- **Praktika:** Paprastas LangChain RAG: Įkelti -> Skaldyti -> Ieškoti -> Generuoti (OpenAI/Gemini).

### **3 Diena: Įterpiniai ir Vektorinės Duomenų Bazės**
- Įterpiniai: Semantinė reprezentacija (OpenAI, Sentence Transformers).
- Vektorinės Saugyklos: Įterpinių saugojimas (pvz., `Chroma`).
- LangChain Integracija: Naudojant `Chroma`.
- **Praktika:** Patobulinti RAG: Įterpti -> Saugoti ChromaDB -> Ieškoti pagal panašumą.

### **4 Diena: RAG Našumo Gerinimas**
- RAG Iššūkiai: Paieškos/generavimo kokybė.
- Teksto Skaldymo Strategijos: Skaidymo įtaka.
- Paieškos Technikos: MMR, metaduomenų filtravimas, suspaudimas.
- **Praktika:** Eksperimentuoti su skaldymo/paieškos metodais LangChain RAG.

### **5 Diena: RAG Integravimas su Streamlit**
- Sujungti 3 ir 4 Savaites: Streamlit UI RAG.
- Eiga: Streamlit įvestis -> RAG Grandinė -> Streamlit išvestis.
- Būsenos Tvarkymas: `st.session_state` RAG pokalbių istorijai.
- **Praktika:** Streamlit programa, naudojanti RAG dokumentų Q&A (rodyti atsakymą ir kontekstą).

---

## **5 Savaitė: Atviro Kodo Modeliai ir Koregavimas (Fine-Tuning)**

### **1 Diena: Įvadas į Hugging Face**
- Hugging Face Hub: Modeliai, duomenų rinkiniai, Spaces.
- Transformers Biblioteka: Koncepcijos, pipeline naudojimas.
- Iš anksto apmokytų modelių/tokenizatorių įkėlimas.
- Pagrindinės užduotys: Teksto generavimas, klasifikavimas per `transformers`.
- **Praktika:** Naudoti `transformers` pipeline teksto generavimui ir nuotaikų analizei.

### **2 Diena: Modelių Vykdymas Lokaliai su Ollama ir LM Studio**
- Ollama: Vykdyti LLM lokaliai per CLI.
- Diegimas ir sąranka.
- Modelių (Llama 3, Mistral) vykdymas.
- LM Studio: GUI lokaliam LLM.
- Palyginimas: Ollama vs. LM Studio.
- **Praktika:** Įdiegti Ollama, paleisti modelį per CLI; pasirinktinai tyrinėti LM Studio.

### **3 Diena: Sąveika su Ollama per Python**
- Ollama Python Biblioteka: Diegimas (`uv add ollama`).
- Prisijungti prie veikiančio Ollama.
- Generuoti tekstą/pokalbį per biblioteką.
- Srautiniai atsakymai.
- Integruoti lokalius modelius į Python programas (FastAPI/Streamlit).
- **Praktika:** Python scenarijus, naudojantis `ollama` biblioteką sąveikai su lokaliu modeliu.

### **4 Diena: Koregavimo (Fine-Tuning) Teorija**
- Kas yra Koregavimas?: Iš anksto apmokytų modelių adaptavimas.
- Kodėl Koreguoti?: Geresnis nišinis našumas, srities adaptacija.
- Pilnas vs. PEFT: Koncepcijos, privalumai/trūkumai.
- Duomenų Paruošimas: Instrukcijų rinkiniai (užklausa/atsakymas).

### **5 Diena: Koregavimas Praktikoje su Unsloth ir Kaggle/Colab**
- Unsloth: Greitesnio LoRA/QLoRA koregavimo biblioteka.
- Aplinka: Kaggle/Colab GPU.
- Duomenų Formatavimas: HuggingFace rinkinio pasirinkimas.
- Koregavimo Scenarijus: Unsloth + `transformers` SFTTrainer.
- Vykdyti užduotį.
- Pagrindinis išvadų darymas/testavimas.
- **Praktika:** Koreguoti mažą OS modelį (pvz., Mistral-7B) naudojant Unsloth Kaggle/Colab.

---

## **6 Savaitė: Multimodaliniai Modeliai**

### **1 Diena: Vaizdo Modeliai (Vaizdų Supratimas)**
- Įvadas į Multimodaliumą: Teksto, vaizdų, garso derinimas.
- Vaizdo Modeliai: Aprašymas, VQA.
- API/Bibliotekos: Gemini Vision, OpenAI Vision API, HF `transformers`.
- **Praktika:** Naudoti Vision API (pvz., Gemini Pro) vaizdų aprašymui/Q&A.

### **2 Diena: Multimodalinis Samprotavimas**
- Samprotavimas Tarp Modalų: Teksto + vaizdo užduotys.
- Pavyzdžiai: Aiškinant vizualius juokelius, sekant vaizdines instrukcijas.
- Užklausų kūrimo technikos.
- **Praktika:** Eksperimentuoti su teksto+vaizdo užklausomis samprotavimui (Gemini/GPT-4V).

### **3 Diena: Vaizdų Generavimo Modeliai**
- Tekstas į Vaizdą: Difuzijos modelių koncepcijos.
- Modeliai ir API: Stable Diffusion, DALL-E 3, Imagen.
- Užklausos: Stilius, turinys, neigiamos užklausos.
- **Praktika:** Generuoti vaizdus per API (DALL-E) arba lokaliai (Diffusers).

### **4 Diena: Garso Modeliai**
- Kalbos Atpažinimas (STT): Transkripcija (OpenAI Whisper).
- Teksto Įgarsinimas (TTS): Sintezė (Google TTS, OpenAI TTS).
- API/Bibliotekos garsui.
- **Praktika:** Naudoti Whisper API/lib transkripcijai; TTS API/lib kalbos generavimui.

### **5 Diena: Projektas - Vaizdo Analizės Programa**
- Integruoti Vaizdo Modelius: Paprasta programa su vaizdo galimybėmis.
- Idėja: Streamlit programa vaizdo įkėlimui -> analizė -> rodymas.
- Projekto darbo laikas ir Q&A.
- **Praktika:** Sukurti bazinę programą (CLI/Streamlit) su vaizdo analize.

---

## **7 Savaitė: DI Agentai**

### **1 Diena: Įvadas į DI Agentus**
- Kas yra Agentai?: LLM, kurie samprotauja, planuoja, naudoja įrankius.
- Pagrindinės Koncepcijos: Samprotavimo ciklas (Stebėti, Galvoti, Veikti), planavimas, atmintis.
- Architektūros: ReAct, Planuoti-ir-Vykdyti.
- Sistemų Apžvalga: LangChain Agents, OpenAI Assistants.

### **2 Diena: Agentai ir Įrankiai**
- Kodėl Įrankiai?: Išplėsti agentų galimybes (paieška, kodas, API).
- Įrankių Apibrėžimas: Funkcijos agentams.
- Įrankių Pasirinkimas ir Kvietimas.
- Sistemos Integracija: Naudojant įrankius.
- **Praktika:** Sukurti paprastą įrankį (skaičiuotuvą) ir integruoti su agentu.

### **3 Diena: Modelio Konteksto Protokolo (MCP) Įvadas**
- Kas yra MCP?: Standartinis protokolas modelių/įrankių sąveikai.
- Pagrindinės Koncepcijos: Resursai, Užklausos, Įrankiai, Mėginių ėmimas.
- Privalumai: Sąveikumas (modeliai, klientai, įrankiai).
- Kaip veikia: Klientas <-> Serveris (STDIO, SSE).
- Apžvalga: SDK (Python/TS), integracijos (Cursor).
- **Praktika:** Tyrinėti MCP dok./SDK; pasirinktinai sukurti paprastą serverį arba prijungti klientą.

### **4 Diena: OpenAI Agents SDK**
- Apžvalga: Lengvas kelių agentų sistemų karkasas.
- Pagrindinės Koncepcijos: Agentai (instrukcijos, įrankiai), Perdavimai, Apsaugos, Sekimas.
- Vykdyklė ir Ciklas: `Runner.run()` vykdymas.
- Įrankių Apibrėžimas: `@function_tool` dekoratorius.
- Suderinamumas: OpenAI Pokalbių Užbaigimo formatas.
- **Praktika:** Įdiegti SDK (`uv add openai-agents`), paleisti pavyzdžius (hello world, įrankis, perdavimai).

### **5 Diena: Projektas - Paprastas Tyrimų Agentas**
- Tikslas: Agentas tiria temą naudodamas žiniatinklio paieškos įrankį.
- Komponentai: LLM, Agentų Sistema, Paieškos Įrankis.
- Eiga: Užklausa -> Planas -> Paieška -> Sintezė -> Atsakymas.
- **Praktika:** Įgyvendinti bazinį tyrimų agentą (LangChain/Assistants) + paieškos įrankį.

---

## **8 Savaitė: Įmonių Sistemų Kūrimas su Python ir FastAPI**

### **1 Diena: Pažangus FastAPI ir REST API Standartai**
- FastAPI Apžvalga: Priklausomybių Įterpimas, Fono Užduotys, Maršrutizatoriai.
- REST Dizaino Principai: Pavadinimai, metodai, būsenos kodai, HATEOAS.
- **Praktika:** Refaktorizuoti FastAPI pavyzdžius naudojant `APIRouter`.

### **2 Diena: Duomenų Bazės Integracija su MongoDB ir FastAPI**
- NoSQL Įvadas: Dokumentų DB (MongoDB).
- MongoDB Pagrindai: Dokumentai, Kolekcijos, CRUD.
- Integracija: FastAPI + `PyMongo`.
- Atvaizdavimas: Pydantic <-> MongoDB.
- Asinchroninės DB operacijos.
- **Praktika:** Sujungti FastAPI su MongoDB; įgyvendinti CRUD resursui.

### **3 Diena: Automatizuotas Testavimas su Pytest**
- Testavimo Svarba.
- Testavimo Piramidė: Vienetiniai, Integraciniai, E2E.
- Įvadas į `pytest`: Funkcijos, tvirtinimai, priedai (fixtures).
- Vienetinis Testavimas: Serviso sluoksnis, pagalbinės funkcijos.
- Integracinis Testavimas: Sluoksnių sąveika (Servisas + Repozitorija).
- Galinio Taško Testavimas: `TestClient` simuliuotoms HTTP užklausoms.
- **Praktika:** Rašyti vienetinius ir integracinius/galinio taško testus naudojant `pytest` ir `TestClient`.

### **4 Diena: Konteinerizavimas su Docker ir Pagrindinis AWS Diegimas**
- Įvadas į Docker: Konteineriai vs. VM, `Dockerfile` pagrindai.
- FastAPI Konteinerizavimas: `Dockerfile`, kurti atvaizdus.
- Docker Compose: Kelių konteinerių sąrankos (programa + DB).
- Debesijos Koncepcijos: AWS paslaugos (EC2, ECR, RDS/DocDB, ECS/Fargate).
- Pagrindinis Diegimas: Įkelti į ECR, paleisti EC2/App Runner.
- **Praktika:** Sukurti `Dockerfile`, atvaizdą, pasirinktinai paleisti lokaliai; aptarti pagrindinį AWS diegimą.

### **5 Diena: Apibendrinimas ir tolesnio mokymosi žingsniai**
- **Apibendrinimas:** Apžvelgti pagrindines sąvokas (Python, FastAPI, DBs, Docker, Cloud Basics).
- **Tolesnio Mokymosi Pasiūlymai DI Inžinieriams:** 