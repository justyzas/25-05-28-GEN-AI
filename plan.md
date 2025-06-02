# **Week 1: Python Foundations & Environment Setup**

---

## 📅 **Day 1**

### 🔹 Topics Covered:
- Introduction — About the instructor
- Overview of the course
- Installation and setup of:
  - **Visual Studio Code**
  - **Python**
  - **Git**

---

### 🧠 Key Terms

- **Generative AI (Artificial Intelligence)**  
  AI that can **create new content** — such as text, images, code, audio, or video — rather than just analyze data.

- **LLM (Large Language Model)**  
  A type of AI trained on **massive amounts of text** to predict and generate **human-like language**.

- **Platform**  
  A set of **tools, services, infrastructure, and environments** used to develop, deploy, and manage AI applications.

---

## 📅 **Day 2**

### 🔹 Topics Covered:
- Recap of Day 1
- Introduction to:
  - **Git** (technology for version control)
  - **GitHub** (platform for hosting code)

---

### 🛠️ Git Commands

- ```git clone <URL>```  
  Clones a remote repository to your local machine. Use only once for initial setup.

- ```git checkout <CommitID>```  
  Switches to a previous version of the code using a commit ID.

- ```git checkout main```  
  Returns to the latest version on the main branch.

- ```git pull```  
  Pulls the latest code from the remote repository if it has been set up.

---

### 💻 Practice Topics

- Creating commits and pushing code to GitHub
- Python Basics:
  - **Variables**
  - **User input with `input()`**
  - **Conditional statements (`if`, `elif`, `else`)**

### [Homework](https://github.com/justyzas/25-05-28-GEN-AI/blob/main/homework/2025-05-29.MD)

## 📅 **Day 3**

- Questions and Recap of Day 2
- Python operations with strings, numbers, introduction to lists

- Discussing about GEN AI models
- Gen AI models limitations

#### 🔮 1. **Hallucination (Making Things Up)**
- Gen AI models may **generate content that sounds plausible but is completely false**.
- This includes:
  - Incorrect facts
  - Fake references
  - Made-up URLs or studies
- ⚠️ Critical in fields like medicine, law, or academia.

#### 📅 2. **Lack of Real-Time or Recent Knowledge**
- Most models are trained on **static data** with a **knowledge cutoff** (e.g., GPT-4 is trained up to late 2023).
- They **do not access the internet** by default.
- This makes them **unreliable for breaking news, live events, or up-to-date info**.

---

#### 🧠 3. **No True Understanding or Reasoning**
- LLMs **do not think or understand** like humans.
- They generate text based on **patterns and probabilities**, not logic or comprehension.
- They may fail at:
  - Multi-step logical problems
  - Understanding ambiguous input
  - Reasoning about cause and effect

---

#### 🧾 4. **Memory and Context Limitations**
- Models have a **maximum context length** (e.g., 4k, 8k, 128k tokens).
- If you input too much text, earlier content may be **truncated or forgotten**.
- They do **not persist memory** between sessions unless designed with tools like memory APIs or databases.

#### 🌍 5. **Bias and Toxicity**
- Models are trained on **internet-scale data**, which includes **biases, stereotypes, and harmful language**.
- They may:
  - Reflect societal biases
  - Reinforce stereotypes
  - Generate offensive or inappropriate output if not carefully prompted or filtered

### 6. It may fail on very simple and specific tasks, for example, counting 'r's in word "strawberry"

### 7. It may fail in image generation while trying to add some text. Characters may seem distorted.

### 8. Hosting LLM may seem very expensive in resources

## 🤖 **AI Model Types**

---

### 🧠 1. **Vision LLMs**

#### 🔍 What They Do:
- Process and understand **images or visual input**.
- Combine **language + vision** to answer questions about pictures, describe images, or interact **multimodally**.

#### 📌 Typical Tasks:
- **Image captioning**: “Describe this image.”
- **Visual question answering**: “What’s the man holding in the picture?”
- **Multimodal interaction**: “Read the text in this screenshot and explain it.”

#### 🧪 Examples in Ollama:
- `llava`, `bakllava`, `gpt-4o` (if supported), `blip`, `clip`

#### ⚙️ How They Differ:
- Expect an **image as input**, alongside or instead of text.
- Cannot be used meaningfully for **language-only tasks** like embeddings.

---

### 🛠️ 2. **Tools LLMs**

#### 🔍 What They Do:
LLMs configured to work with **external tools**, like:
- Calculators  
- Web search  
- Code execution  
- APIs  

#### 📌 Typical Tasks:
- “What’s 1249123 divided by 7.3?” → Calls a **calculator tool**
- “Get the current weather in Berlin” → Calls a **weather API**
- **Agent workflows** (multi-step reasoning)

#### 🧪 Examples in Ollama:
- Tool-using variants of LLMs integrated with:
  - **LangChain**
  - **AutoGPT-like flows**
  - **Function-calling models**

#### ⚙️ How They Differ:
- They don’t “know” the answers — they **perform actions or call helpers**.
- May rely on **additional code or environment**.
  - Ollama **doesn’t handle tool execution** natively — it **serves the LLM**; the toolchain is external.

- **Ollama model installation** and **running** on **local machine**
