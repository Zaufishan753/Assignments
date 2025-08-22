

def groupAnagram(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())
word=["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(word))
