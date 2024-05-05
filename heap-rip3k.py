import os
import heapq

# 创建一个临时文件夹来存放分块文件
tmp_dir = 'tmp_files'
os.makedirs(tmp_dir, exist_ok=True)

def sorted_rules(x):
    try:
        temp = x.split()[2]
    except:
        # 如果数据不符合规范，返回负无穷
        return float('-inf')
    try:
        return float(temp)
    except:
        # 如果数据不符合规范，返回负无穷
        return float('-inf')


# 读取所有txt文件中的数据，并将数据分成多个分块文件
def create_chunk_files():
    chunk_num = 0
    heap = []
    for root, dirs, files in os.walk('/home/yanbosmu/Bioinfo/PharmacoNet-main/RIPK3_inhibitor'):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                    print(os.path.join(root, file))
                    lines = sorted(lines, key=sorted_rules, reverse=True)
                    heap.extend(lines)
                    if len(heap) > 50000:  # 每个chunk包含不超过50000条数据
                        chunk_num += 1
                        with open(f'{tmp_dir}/chunk_{chunk_num}.txt', 'w') as chunk_file:
                            for line in heap:
                                chunk_file.write(line)
                        heap = []

    if heap:
        chunk_num += 1
        with open(f'{tmp_dir}/chunk_{chunk_num}.txt', 'w') as chunk_file:
            for line in heap:
                chunk_file.write(line)

# 使用堆排序查找前10%和前1%的数据
def extract_top_data():
    heap = []
    all_data = []
    result_file_10 = open('top_10_percent_sorted.txt', 'w')
    result_file_1 = open('top_1_percent_sorted.txt', 'w')
    chunkfile = os.listdir(tmp_dir)
    for file in chunkfile:  # 遍历所有分块文件
        with open(f'{tmp_dir}/{file}', 'r') as chunk_file:
            lines = chunk_file.readlines()
            for line in lines:
                # heapq.heappush(heap, line)
                all_data.append(line)
    
    enum_list = []
    for i, line in enumerate(all_data):
        try:
            temp = line.split()[2]
        except:
            continue
        try:
            enum_list.append((-float(temp), i))
        except:
            continue
    
    for each in enum_list:
        heapq.heappush(heap, each)

    total_rows = len(heap)
    top_10_percent = int(total_rows * 0.1)
    top_1_percent = int(total_rows * 0.01)

    for i in range(top_10_percent):
        # result_file_10.write(heapq.heappop(heap))
        temp = heapq.heappop(heap)
        if i < top_1_percent:
            result_file_1.write(all_data[temp[1]])
        result_file_10.write(all_data[temp[1]])

    result_file_10.close()
    result_file_1.close()

# 创建分块文件
create_chunk_files()

# 提取并排序前10%和前1%的数据
extract_top_data()

print("Top 10% and Top 1% data sorted and extracted successfully.")
