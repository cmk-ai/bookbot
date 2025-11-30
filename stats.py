def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_all_words(file_path):
    book_content = get_book_text(file_path)
    all_words = book_content.split()
    return all_words

def get_num_words(all_words):
    num_words = len(all_words)
    return num_words

def get_char_count(all_words):
    all_char_count = {}
    for word in all_words:
        for letr in word.lower():
            if letr in all_char_count:
                all_char_count[letr] += 1
            else:
                all_char_count[letr] = 1
    return all_char_count


def get_sorted_dict(all_char_count):
    return dict(sorted(all_char_count.items(), key=lambda item: item[1], reverse=True))


