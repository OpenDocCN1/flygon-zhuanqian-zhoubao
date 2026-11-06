# 用 Cursor 把公号代运营的批量插图难题自动化

给多家👸号做代运营时，最让人头疼的并不是写稿，而是稿子写好后怎么配图、怎么排版。手工找图、复制链接、调间距，效率低还容易出错。最近我用 Cursor 复盘并落地了一套自动化流程，插图和排版一次性跑通，省掉了重复劳动。

大致做法可以拆成四个环节：先把每篇素材对应的配图地址整理到一个独立的 txt；再通过脚本把这些地址转成排版平台可识别的 HTML 形式；随后在 96 编辑器里做还原与模板套用，这一环参考了猫哥的思路；最后运行程序，弹出图形操作界面，指定好目录即可批量执行。

运行后会看到可视化面板，需要填入三类路径：文章存放目录、图片地址存放目录、处理结果输出目录。系统会依据文件名自动寻找对应关系，文稿和图片清单同名即视为一对。插入时只统计非空段落，按段落间隔均匀分布图位，避免扎堆。单篇候选图片较多时，默认随机抽取 3 到 5 张，保持阅读节奏。

整批任务可以同时处理，日志区会实时反馈匹配成功、匹配失败以及每篇的处理状态，不用再人工逐项核对。多个文档也能一次性完成，输出为可直接导入的 markdown 格式。

文末附上可直接复用的脚本源码，按需下载使用即可。

![](img/5355e558625b6b0139162ea99f54705e.png)
import os

import random

import tkinter as tk

from tkinter import filedialog, ttk, messagebox

def insert_images_into_text(text_file_path, image_links_file_path, output_file_path):

try:

# 读取文章内容，保持原有格式

with open(text_file_path, 'r', encoding='utf-8') as f:

text_content = f.read()

# 读取图片链接并去重

with open(image_links_file_path, 'r', encoding='utf-8') as f:

image_links = []

used_links = set()

for line in f:

link = line.strip()

if link and link not in used_links:

image_links.append(link)

used_links.add(link)

# 随机选取3-5张图片

if len(image_links) > 5:

num_images = random.randint(3, 5)

image_links = random.sample(image_links, num_images)

elif len(image_links) > 3:

num_images = random.randint(3, len(image_links))

image_links = random.sample(image_links, num_images)

# 如果图片数量小于等于3，保持所有图片

# 将文章分割成段落，保持原有的换行符

paragraphs = text_content.split('\n')

# 计算插入位置

# 只计算非空段落的数量来确定图片位置

non_empty_paragraphs = [i for i, p in enumerate(paragraphs) if p.strip()]

total_paragraphs = len(non_empty_paragraphs)

total_images = len(image_links)

insert_positions = []

if total_images > 0:

step = total_paragraphs / (total_images + 1)

for i in range(total_images):

pos = non_empty_paragraphs[int(step * (i + 1))]

if pos >= len(paragraphs):

break

insert_positions.append(pos)

# 插入图片

final_content = []

image_index = 0

for i, paragraph in enumerate(paragraphs):

final_content.append(paragraph)

if i in insert_positions and image_index < len(image_links):

final_content.append('') # 图片前的空行

final_content.append(image_links[image_index])

final_content.append('') # 图片后的空行

image_index += 1

# 写入新文件

with open(output_file_path, 'w', encoding='utf-8') as f:

f.write('\n'.join(final_content))

return "success"

except Exception as e:

return f"error: {str(e)}"

class ImageInserterGUI:

def __init__(self, root):

self.root = root

self.root.title("文章图片插入工具")

self.root.geometry("800x600")

# 创建主框架

self.main_frame = ttk.Frame(root, padding="10")

self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# 文件夹选择区域

self.create_folder_selection()

# 日志显示区域

self.create_log_area()

# 执行按钮

self.create_execute_button()

def create_folder_selection(self):

# 文章文件夹选择

ttk.Label(self.main_frame, text="文章文件夹:").grid(row=0, column=0, sticky=tk.W, pady=5)

self.articles_path = tk.StringVar()

ttk.Entry(self.main_frame, textvariable=self.articles_path, width=60).grid(row=0, column=1, pady=5)

ttk.Button(self.main_frame, text="浏览", command=lambda: self.browse_folder(self.articles_path)).grid(row=0, column=2, padx=5, pady=5)

# 图片链接文件夹选择

ttk.Label(self.main_frame, text="图片链接文件夹:").grid(row=1, column=0, sticky=tk.W, pady=5)

self.images_path = tk.StringVar()

ttk.Entry(self.main_frame, textvariable=self.images_path, width=60).grid(row=1, column=1, pady=5)

ttk.Button(self.main_frame, text="浏览", command=lambda: self.browse_folder(self.images_path)).grid(row=1, column=2, padx=5, pady=5)

# 输出文件夹选择

ttk.Label(self.main_frame, text="输出文件夹:").grid(row=2, column=0, sticky=tk.W, pady=5)

self.output_path = tk.StringVar()

ttk.Entry(self.main_frame, textvariable=self.output_path, width=60).grid(row=2, column=1, pady=5)

ttk.Button(self.main_frame, text="浏览", command=lambda: self.browse_folder(self.output_path)).grid(row=2, column=2, padx=5, pady=5)

def create_log_area(self):

# 创建日志显示区域

log_frame = ttk.LabelFrame(self.main_frame, text="处理日志", padding="5")

log_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

self.log_text = tk.Text(log_frame, height=20, width=80)

self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)

scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

self.log_text['yscrollcommand'] = scrollbar.set

def create_execute_button(self):

# 创建执行按钮

ttk.Button(self.main_frame, text="开始处理", command=self.execute_process).grid(row=4, column=0, columnspan=3, pady=10)

def browse_folder(self, string_var):

folder_path = filedialog.askdirectory()

if folder_path:

string_var.set(folder_path)

def log(self, message):

self.log_text.insert(tk.END, message + "\n")

self.log_text.see(tk.END)

self.root.update()

def execute_process(self):

# 检查路径是否都已选择

if not all([self.articles_path.get(), self.images_path.get(), self.output_path.get()]):

messagebox.showerror("错误", "请选择所有必要的文件夹路径")

return

# 清空日志

self.log_text.delete(1.0, tk.END)

try:

result = match_and_insert_images(

self.articles_path.get(),

self.images_path.get(),

self.output_path.get(),

log_callback=self.log

)

messagebox.showinfo("完成", result)

except Exception as e:

messagebox.showerror("错误", str(e))

def match_and_insert_images(articles_folder, images_folder, output_folder, log_callback=print):

try:

if not os.path.exists(output_folder):

os.makedirs(output_folder)

# 获取所有文章文件

article_files = {}

log_callback("文章文件列表：")

for file in os.listdir(articles_folder):

if file.endswith('.txt'):

name = os.path.splitext(file)[0]

article_files[name] = os.path.join(articles_folder, file)

log_callback(f" - {name}")

# 获取所有图片链接文件

image_files = {}

log_callback("\n图片链接文件列表：")

for file in os.listdir(images_folder):

if file.endswith('.txt'):

name = os.path.splitext(file)[0]

image_files[name] = os.path.join(images_folder, file)

log_callback(f" - {name}")

# 显示匹配结果

log_callback("\n成功匹配的文件：")

matched_files = set(article_files.keys()) & set(image_files.keys())

for name in matched_files:

log_callback(f" - {name}")

log_callback("\n未匹配的文章文件：")

unmatched_articles = set(article_files.keys()) - set(image_files.keys())

for name in unmatched_articles:

log_callback(f" - {name}")

log_callback("\n未匹配的图片链接文件：")

unmatched_images = set(image_files.keys()) - set(article_files.keys())

for name in unmatched_images:

log_callback(f" - {name}")

# 匹配文件并处理

processed_count = 0

for name in matched_files:

output_file = os.path.join(output_folder, f"{name}.md")

# 调用原有的插入图片函数

result = insert_images_into_text(

article_files[name],

image_files[name],

output_file

)

if result == "success":

processed_count += 1

log_callback(f"成功处理: {name}")

else:

log_callback(f"处理失败: {name}, 错误: {result}")

return f"完成处理 {processed_count} 个文件"

except Exception as e:

return f"错误: {str(e)}"

if name == "__main__":

root = tk.Tk()

app = ImageInserterGUI(root)

root.mainloop()

# 脚本链接：