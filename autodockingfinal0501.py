import subprocess
import time
import gc  # 导入垃圾回收模块

# 待执行的文件列表
file_list = ["a{:03d}.txt".format(i) for i in range(131,261)]

for file in file_list:
    command = ["./QuickVina2-GPU-2-1", "--config", f"./RIP3K/RIPK3/commandtxt/{file}"]

    print(f"Executing command: {' '.join(command)}")

    # 开始执行命令，并将标准输出和标准错误流合并到一起
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # 获取命令执行的输出
    output, _ = process.communicate()

    # 输出命令执行的结果
    print(output)

    print("Command execution completed.")

    # 关闭子进程
    process.kill()

    # 手动触发垃圾回收
    gc.collect()

    # 等待120秒
    time.sleep(60)
