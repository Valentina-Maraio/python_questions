def read_numbers_and_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            data = [(int(line.split()[0]), line.split()[1].strip()) for line in lines if line.split()[0].isdigit()]
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def create_pyramid(data):
    sorted_data = sorted(data, key=lambda x: x[0])
    
    current_num = 0
    row = 1
    last_numbers_and_words = []

    while current_num < len(sorted_data):
        row_data = sorted_data[current_num:current_num + row]
        last_numbers_and_words.append(row_data[-1])  # Store the last number and word of each row
        current_num += row
        row += 1

    for number, word in last_numbers_and_words:
        print(f"{number} {word}")


if __name__ == "__main__":
    file_path = "./coding_qual_input.txt"  # Replace with your actual file name

    data = read_numbers_and_words_from_file(file_path)

    if data:
        create_pyramid(data)