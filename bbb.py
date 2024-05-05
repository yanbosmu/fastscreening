def extract_and_sort_zinc_strings(filename):
    zinc_strings = {}
    with open(filename, 'r') as file:
        prev_value = None
        for line in file:
            line = line.strip()
            if line.startswith("REMARK VINA RESULT:"):
                try:
                    prev_value = float(line.split()[3])
                except (ValueError, IndexError):
                    continue
            elif line.startswith("REMARK  Name = ZINC"):
                if prev_value is not None:
                    zinc_strings[line.split()[-1]] = prev_value
    
    sorted_zinc_strings = sorted(zinc_strings.items(), key=lambda x: x[1])
    return sorted_zinc_strings

def write_to_file(sorted_zinc_strings, output_filename):
    with open(output_filename, 'w') as output_file:
        for zinc_string, value in sorted_zinc_strings:
            output_file.write(f"{zinc_string}  {value}\n")

filename = "/home/yanbosmu/Bioinfo/PharmacoNet-main/RIPK3_inhibitor/1/finalresultfinal10.txt"  # 替换为你的文件路径
output_filename = "/home/yanbosmu/Bioinfo/PharmacoNet-main/RIPK3_inhibitor/1/result_10_a.txt"  # 替换为输出文件路径
sorted_zinc_strings = extract_and_sort_zinc_strings(filename)
write_to_file(sorted_zinc_strings, output_filename)
print("结果已写入到", output_filename)

