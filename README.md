**8-Week Practical Course: Application Programming with GEN-AI and Python**

# Lecture Plan:

## Lecture time: 17:30 - 19:55

## 17:30 - 18:00 - Feedback + homework review

## 18:00 - 18:50 - Theory in python + some examples

## 18:50 - 19:00 - Break

## 19:00 - 19:45 - Theory about GEN-AI

## 19:45 - 19:55 - Summarize

## **Week 1: Python Foundations & Environment Setup**

### **Day 1: Course Introduction & Environment Setup**

- Course overview, objectives, goals.
- Python installation & PATH setup.
- Virtual Environments: `venv`/`uv`.
- IDE Setup: VSCode basics, extensions.
- "Hello, World!".

### **Day 2: Python Basics**

- Data Types: Numbers, Strings, Booleans.
- Data Structures: Lists, Tuples, Dictionaries, Sets.
- Control Flow: `if`/`elif`/`else`, `for`/`while`.
- Debugging Intro: `print`, tracebacks, IDE debugger.

### **Day 3: Python Essentials for GEN-AI**

- Functions: `def`, arguments, return, scope.
- Error Handling: `try...except`.
- Modules & Packages: `import`, stdlib (`os`, `math`), install (`uv`).
- Code Style: PEP 8, modularity.
- **Lab:** Text manipulation utility functions.

### **Day 4: Working with Libraries & Data**

- HTTP Basics: Methods, status codes.
- `requests` Library: API calls, responses.
- `json` Library: Parsing (`loads()`) & serialization (`dumps()`).
- Intro Data Handling: `numpy` arrays, file I/O.
- **Lab:** Fetch & process API data; optional file saving.

### **Day 5: Introduction to APIs & Basic Application Building**

- API Concepts: REST, API keys.
- App Structure: CLI design.
- **Lab:** Build CLI app calling API based on user input.

---

## **Week 2: Introduction to Generative AI & API Integration**

### **Day 1: What Is Generative AI?**

- Definition, history, concepts (LLMs, prompts, tokens).
- Major models/players (OpenAI, Google).
- Ethics: Bias, misuse.
- Demo: Text/image generation (ChatGPT, Midjourney).

### **Day 2: REST APIs & Introduction to FastAPI**

- RESTful API review.
- Intro FastAPI: Features, setup (`uvicorn`).
- Path Operations: Routes (`@app.get`/`@app.post`), path/query params.
- Request Body: Pydantic validation.
- **Lab:** Simple FastAPI "Hello World" API; explore Swagger UI.

### **Day 3: Working with OpenAI's GPT APIs**

- OpenAI Platform: Models (GPT-4/3.5), pricing.
- API Key Management & Security.
- OpenAI Python Library: Install (`uv add openai`), usage.
- Chat Completions API: `openai.chat.completions.create`, roles.
- Key Params: `model`, `messages`, `temperature`, `max_tokens`.
- **Lab:** Python script using GPT API for prompts/responses.

### **Day 4: OpenAI Models: Capabilities, Limitations & Prompting**

- Model Capabilities/Limitations (cutoff, hallucinations).
- Prompt Engineering Basics: Context, format, zero/few-shot.
- Intro: Tools/Function Calling.
- Intro: Assistants API (stateful).
- **Lab:** Experiment with prompt engineering; optional function calling.

### **Day 5: Integrating OpenAI with FastAPI**

- App Structure: FastAPI + OpenAI.
- Secure API Key Handling: Env vars (`python-dotenv`).
- API Endpoint (`/generate`): Takes prompt, calls OpenAI.
- Return Response: JSON format.
- **Lab:** FastAPI endpoint taking prompt, calling OpenAI, returning response.

---

## **Week 3: Google Gemini & UI with Streamlit**

### **Day 0: Vibe coding tutorial (Cursor and Copilot)**

- Intro AI code assistants: Cursor, Copilot.
- Setup, basic usage (chat, code gen).
- AI pair programming tips.

### **Day 1: Exploring Google AI Studio & Vertex AI**

- Google AI Ecosystem: Vertex AI overview.
- Google AI Studio: Web-based Gemini prototyping.
- Gemini Models: Pro, Flash.
- Hands-on: Prompting, params, safety settings in AI Studio.
- **Lab:** Use AI Studio for text tasks (generate, summary, Q&A) with Gemini.

### **Day 2: Programming with the Google Gemini API**

- Google AI Python SDK: Install (`uv add google-generativeai`), setup.
- Authentication: API keys.
- API Calls: `GenerativeModel.generate_content`.
- Streaming Responses: Handling chunks.
- **Lab:** Python script using Gemini API for text generation (incl. streaming).

### **Day 3: Introduction to Streamlit for UI Development**

- Streamlit Basics: Rapid UI, execution model, caching.
- Core Widgets: Text (`st.write`), input (`st.text_input`, `st.button`), layout (`st.columns`, `st.sidebar`).
- Data Display: DataFrames (`st.dataframe`), basic charts.
- **Lab:** Build simple Streamlit app with various widgets/layout.

### **Day 4: Building Streamlit Chatbots with Gemini**

- Chat UI: `st.chat_input`, `st.chat_message`.
- State Management: `st.session_state` for history.
- Integration: Connect Streamlit I/O to Gemini API.
- Workflow: Input -> History -> API call -> Display -> History.
- **Lab:** Simple Streamlit chatbot using `st.session_state` & Gemini API.

### **Day 5: Project Work & Review**

- Project work time.
- Instructor Q&A.
- Review Week 3: Gemini API, Streamlit, state management.
- Discussion: Challenges, ideas.

---

## **Week 4: Introduction to Retrieval-Augmented Generation (RAG)**

### **Day 1: What is RAG? Core Concepts & Use Cases**

- Problem: LLM limitations (cutoff, hallucinations).
- RAG Concept: Retrieve info, then generate.
- Architecture: Retriever + Generator (LLM).
- Benefits: Grounding, factual consistency, domain knowledge.
- Use Cases: Chatbots, Q&A on private data, summarization.
- **Activity:** Brainstorm RAG applications.

### **Day 2: RAG Implementation with Langchain**

- Intro LangChain: Orchestration (Components, Chains).
- RAG Components: Loaders, Splitters, Embeddings, Vector Stores, Retrievers, LLMs.
- `RetrievalQA` Chain: Basic RAG Q&A.
- **Lab:** Simple LangChain RAG: Load -> Split -> Retrieve -> Generate (OpenAI/Gemini).

### **Day 3: Embeddings & Vector Databases**

- Embeddings: Semantic representation (OpenAI, Sentence Transformers).
- Vector Stores: Storing embeddings (e.g., `Chroma`).
- LangChain Integration: Using `Chroma`.
- **Lab:** Enhance RAG: Embed -> Store in ChromaDB -> Retrieve via similarity.

### **Day 4: Improving RAG Performance**

- RAG Challenges: Retrieval/generation quality.
- Text Splitting Strategies: Impact of chunking.
- Retrieval Techniques: MMR, metadata filtering, compression.
- **Lab:** Experiment with splitting/retrieval methods in LangChain RAG.

### **Day 5: Integrating RAG with Streamlit**

- Combine Weeks 3 & 4: Streamlit UI for RAG.
- Workflow: Streamlit input -> RAG Chain -> Streamlit output.
- State Handling: `st.session_state` for RAG chat history.
- **Lab:** Streamlit app using RAG pipeline for Q&A on docs (show answer & context).

---

## **Week 5: Open Source Models & Fine-Tuning**

### **Day 1: Introduction to Hugging Face**

- Hugging Face Hub: Models, datasets, Spaces.
- Transformers Library: Concepts, pipeline usage.
- Loading pre-trained models/tokenizers.
- Basic tasks: Text generation, classification via `transformers`.
- **Lab:** Use `transformers` pipeline for text gen & sentiment analysis.

### **Day 2: Running Models Locally with Ollama & LM Studio**

- Ollama: Run LLMs locally via CLI.
- Installation & setup.
- Running models (Llama 3, Mistral).
- LM Studio: GUI for local LLMs.
- Comparison: Ollama vs. LM Studio.
- **Lab:** Install Ollama, run model via CLI; optional LM Studio exploration.

### **Day 3: Interacting with Ollama via Python**

- Ollama Python Library: Install (`uv add ollama`).
- Connect to running Ollama instance.
- Generate text/chat via library.
- Streaming responses.
- Integrate local models into Python apps (FastAPI/Streamlit).
- **Lab:** Python script using `ollama` lib to interact with local model.

### **Day 4: Fine-Tuning Theory**

- What is Fine-Tuning?: Adapting pre-trained models.
- Why Fine-Tune?: Better niche performance, domain adaptation.
- Full vs. PEFT: Concepts, pros/cons.
- Data Prep: Instruction datasets (prompt/response).

### **Day 5: Fine-Tuning in Action with Unsloth & Kaggle/Colab**

- Unsloth: Faster LoRA/QLoRA fine-tuning library.
- Environment: Kaggle/Colab GPUs.
- Data Formatting: HuggingFace dataset selection.
- Fine-tuning Script: Unsloth + `transformers` SFTTrainer.
- Running the job.
- Basic inference/testing.
- **Lab:** Fine-tune small OS model (e.g., Mistral-7B) using Unsloth on Kaggle/Colab.

---

## **Week 6: Multimodal Models**

### **Day 1: Vision Models (Image Understanding)**

- Intro Multimodality: Combining text, images, audio.
- Vision Models: Captioning, VQA.
- APIs/Libraries: Gemini Vision, OpenAI Vision API, HF `transformers`.
- **Lab:** Use Vision API (e.g., Gemini Pro) for image description/Q&A.

### **Day 2: Multimodal Reasoning**

- Reasoning Across Modalities: Text + image tasks.
- Examples: Explain visual jokes, follow visual instructions.
- Prompting techniques.
- **Lab:** Experiment with text+image prompts for reasoning (Gemini/GPT-4V).

### **Day 3: Image Generation Models**

- Text-to-Image: Diffusion model concepts.
- Models & APIs: Stable Diffusion, DALL-E 3, Imagen.
- Prompting: Style, content, negative prompts.
- **Lab:** Generate images via API (DALL-E) or local setup (Diffusers).

### **Day 4: Audio Models**

- Speech-to-Text (STT): Transcription (OpenAI Whisper).
- Text-to-Speech (TTS): Synthesis (Google TTS, OpenAI TTS).
- APIs/Libraries for audio.
- **Lab:** Use Whisper API/lib for transcription; TTS API/lib for speech generation.

### **Day 5: Project - Vision Analysis Application**

- Integrating Vision Models: Simple app using vision.
- Idea: Streamlit app for image upload -> analysis -> display.
- Project work time & Q&A.
- **Lab:** Build basic app (CLI/Streamlit) with vision analysis.

---

## **Week 7: AI Agents**

### **Day 1: Introduction to AI Agents**

- What are Agents?: LLMs that reason, plan, use tools.
- Core Concepts: Reasoning loop (Observe, Think, Act), planning, memory.
- Architectures: ReAct, Plan-and-Execute.
- Frameworks Overview: LangChain Agents, OpenAI Assistants.

### **Day 2: Agents and Tools**

- Why Tools?: Extend agent capabilities (search, code, APIs).
- Defining Tools: Functions for agents.
- Tool Selection & Invocation.
- Framework Integration: Using tools.
- **Lab:** Create simple tool (calculator) & integrate with basic agent.

### **Day 3: Model Context Protocol (MCP) Introduction**

- What is MCP?: Standard protocol for model/tool interaction.
- Core Concepts: Resources, Prompts, Tools, Sampling.
- Benefits: Interoperability (models, clients, tools).
- How it works: Client <-> Server (STDIO, SSE).
- Overview: SDKs (Python/TS), integrations (Cursor).
- **Lab:** Explore MCP docs/SDKs; optionally set up simple server or connect client.

### **Day 4: OpenAI Agents SDK**

- Overview: Lightweight multi-agent framework.
- Core Concepts: Agents (instructions, tools), Handoffs, Guardrails, Tracing.
- Runner & Loop: `Runner.run()` execution.
- Defining Tools: `@function_tool` decorator.
- Compatibility: OpenAI Chat Completions format.
- **Lab:** Install SDK (`uv add openai-agents`), run examples (hello world, tool, handoffs).

### **Day 5: Project - Simple Research Agent**

- Goal: Agent researches topic using web search tool.
- Components: LLM, Agent Framework, Search Tool.
- Workflow: Prompt -> Plan -> Search -> Synthesize -> Response.
- **Lab:** Implement basic research agent (LangChain/Assistants) + search tool.

---

## **Week 8: Enterprise System Development with Python and FastAPI**

### **Day 1: Advanced FastAPI & REST API Standards**

- FastAPI Recap: Dependency Injection, Background Tasks, Routers.
- REST Design Principles: Naming, methods, status codes, HATEOAS.
- **Lab:** Refactor FastAPI examples using `APIRouter`.

### **Day 2: Database Integration with MongoDB & FastAPI**

- NoSQL Intro: Document DBs (MongoDB).
- MongoDB Basics: Docs, Collections, CRUD.
- Integration: FastAPI + `PyMongo`.
- Mapping: Pydantic <-> MongoDB.
- Async DB operations.
- **Lab:** Connect FastAPI to MongoDB; implement CRUD for a resource.

### **Day 3: Automated Testing with Pytest**

- Importance of Testing.
- Testing Pyramid: Unit, Integration, E2E.
- Intro `pytest`: Functions, assertions, fixtures.
- Unit Testing: Service layer, utils.
- Integration Testing: Layer interactions (Service + Repo).
- Endpoint Testing: `TestClient` for simulated HTTP.
- **Lab:** Write unit & integration/endpoint tests using `pytest` & `TestClient`.

### **Day 4: Containerization with Docker & Basic AWS Deployment**

- Intro Docker: Containers vs. VMs, `Dockerfile` basics.
- Containerizing FastAPI: `Dockerfile`, build images.
- Docker Compose: Multi-container setups (app + DB).
- Cloud Concepts: AWS services (EC2, ECR, RDS/DocDB, ECS/Fargate).
- Basic Deployment: Push to ECR, run on EC2/App Runner.
- **Lab:** Create `Dockerfile`, build image, optionally run locally; discuss basic AWS deployment.

### **Day 5: Recap and steps for further learning**

- **Recap:** Review key concepts (Python, FastAPI, DBs, Docker, Cloud Basics).
- **Further Learning Suggestions for AI Engineers:**
