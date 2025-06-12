from langchain.prompts import PromptTemplate

# template creation
template = PromptTemplate.from_template("Translate '{text}' to French")

# template usage
prompt1 = template.format(text="Hello, how are you?")
prompt2 = template.format(text="My name is Milana, what's yours?")
prompt3 = template.format(text="Im Andrius")

# result:
print(prompt1)
print(prompt2)
print(prompt3)

