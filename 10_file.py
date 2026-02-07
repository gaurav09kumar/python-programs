def read_file_compute_frequency_each_word(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                if word in word_count:
                    word_count[word]+=1
                else:
                    word_count[word] = 1
    return word_count

print(read_file_compute_frequency_each_word("/content/sample_data/file.txt"))
