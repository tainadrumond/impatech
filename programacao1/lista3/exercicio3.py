def get_vogals(text: str):
    VOGALS = ['a', 'e', 'i', 'o', 'u']
    vogals_in_text = []
    for vogal in VOGALS:
        if vogal in text:
            vogals_in_text.append(vogal)
            continue
    return vogals_in_text

print(get_vogals('A gata Lara com a rata Sara.'))