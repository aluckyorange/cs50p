content = input("Input: ")

vowels = ["a", "e", "i", "o", "u", 
          "A", "E", "I", "O", "U"]
new_content = ""
for ch in content:
    if ch in vowels:
        continue
    new_content += ch

print(f"Output: {new_content}")