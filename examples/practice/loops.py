# i = 0
# while i < 5:
#     print(i)
#     i = i + 1

# for i in range(1, 10000):
#     print("I love you")

# -----


embedding_objects = [
    {"original": "braske", "embedding": 1.12}, 
    {"original":"bananas", "embedding": 0.87}, 
    {"original": "obuolys", "embedding": 1.87}
    ]

list2 = [embedding_object["original"] for embedding_object in embedding_objects]
print(list2)

