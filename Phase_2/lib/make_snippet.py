def make_snippet(str):
    if len(str) > 5:

        word = str.split(" ")
        first_five = word[:5]
        snippet = (" ").join(first_five)
        return snippet + "..."
    
    else:
        return str
