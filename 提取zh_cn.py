import os
import zipfile
import shutil

# 设置：你的 jar 文件所在的目录
source_dir = "." 
# 设置：提取出的 json 保存的目录
output_dir = "./All_Languages"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

count = 0
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".jar"):
            jar_path = os.path.join(root, file)
            try:
                with zipfile.ZipFile(jar_path, 'r') as jar:
                    for name in jar.namelist():
                        # 查找所有包含 zh_cn.json 的路径
                        if name.endswith("zh_cn.json"):
                            # 提取文件，为了防止文件名冲突，加上原 jar 包的名字前缀
                            file_name = f"{os.path.splitext(file)[0]}_{os.path.basename(name)}"
                            dest_path = os.path.join(output_dir, file_name)
                            with jar.open(name) as source, open(dest_path, "wb") as target:
                                shutil.copyfileobj(source, target)
                            count += 1
                            print(f"已提取: {name} from {file}")
            except Exception as e:
                print(f"无法处理文件 {file}: {e}")

print(f"\n提取完成！共找到并提取了 {count} 个汉化文件，存放在 {output_dir} 文件夹中。")