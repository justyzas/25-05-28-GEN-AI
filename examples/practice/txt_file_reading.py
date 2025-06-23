from rich import print
with open(file="data.txt", encoding="utf-8") as f:
    file_data = f.read()


list_of_texts = [line for line in file_data.split("\n") if line!=""]
print(list_of_texts)