import docx2txt
my_text = docx2txt.process("Why_Blockchain_is_relevant_to_product_management.docx")

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(my_text))