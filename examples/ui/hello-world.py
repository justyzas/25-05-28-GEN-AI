import streamlit as st



# Suteikia paprasto teksto
st.write("Hello world")

# Pavadinimams, headingams:
st.title("Vairuotojų appsas")

# MD (markdown) formatas
st.markdown("""## 🧠 Next Steps (Ideas)

Markdown formatas yra **rich text** formatavimo standartas, leidžiantis mums rašyti *turtingą tekstą*. Turtingas tekstas pasižymi:
            
- Galimybėmis sudaryti paryškinimus, pasvirimus, pabraukimus
- Galimybėmis kurti sąrašus, kaip ir šis kurį skaitote
            
```html
<p>
    This is a paragraph with **markdown bold** which will be ignored.
    This is the next line but there was no break tag so it is on the same line.
</p>
```
   ##### Heading 5
   #### Heading 4
   ### Heading 3
   ## Heading 2
   # Heading 1         
- Chunking larger documents and inserting them
- Ranking results based on metadata filters
- Adding response generation using OpenAI completions
- Exporting and importing vector data (e.g., `.json`, `.txt`, `.csv`)
- Building a simple Streamlit or Flask UI""")

with st.form(key="registracijos_forma"):
# Tekstinė įvestis
    vp = st.text_input(label="Vardas, pavardė", )
    address1 = st.text_input(label="Adresas 1")
    address2 = st.text_input(label="Adresas 2")
    city = st.text_input(label="Miestas")

    # Skaičiaus įvestis
    age = st.number_input(label="Amzius", step=1 )
    
    progress = 0
    if vp != "":
        progress+=20
    if address1 != "":
        progress+=20
    if address2 != "":
        progress+=20
    if city != "":
        progress+=20
    if age != 0:
        progress+=20

    st.progress(progress, text="Registracijos progresas")

    submit = st.form_submit_button(label="Išsiūsti")
    if submit:
        st.info("☑️ Forma sėkmingai išsiūsta!")
        st.success("☑️ Forma sėkmingai išsiūsta!")
        st.warning("☑️ Forma sėkmingai išsiūsta!")
        st.error("☑️ Forma sėkmingai išsiūsta!")

if submit:
    st.markdown(f"""## Gauti duomenys:    
        - {vp}
        - {address1}
        - {address2}
        - {city}
        - {age}""")

# feedback įvestis
ivertinimas = st.feedback("stars")

# kondicinis užkrovimas
if ivertinimas != None:
    st.markdown(f"""
    Pasirinktas įvertinimas yra: **{ivertinimas}**
    """)


user_input = st.chat_input(placeholder="Your message")
print(user_input)

