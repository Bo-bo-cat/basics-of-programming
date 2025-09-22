#most_common_letter(text) Oshovska DEF 
def most_common_letter(text: str) -> str:
   text = text.replace("","")
   if not text:
      return None
   
   return max(text, key=text.count)

print(most_common_letter("original"))
print(most_common_letter("color"))
