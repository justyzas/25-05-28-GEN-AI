from ddgs import DDGS
from rich import print

results = DDGS().text("rekvizitai vz lt ", max_results=5)
print(results)
print(f"found {len(results)} results")
