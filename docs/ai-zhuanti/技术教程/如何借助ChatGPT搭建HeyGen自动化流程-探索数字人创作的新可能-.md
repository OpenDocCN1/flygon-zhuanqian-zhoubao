# 如何借助ChatGPT搭建HeyGen自动化流程，探索数字人创作的新可能？
最近，HeyGen在内容创作圈持续升温。无论是抖音上的小和尚视频，还是各种励志、情绪类短片，背后都能看到数字人技术的身影。
不过，HeyGen免费账户提供的额度非常有限，免费 credit 使用完之后，通常只能重新注册账号继续体验。于是，一个自然的问题出现了：能不能让ChatGPT帮忙编写自动化脚本，减少重复操作？
经过一个多小时的反复沟通和调试，我完成了一个v1.0版本。虽然代码还有进一步优化的空间，但用于个人测试已经基本够用。实际运行不到半小时，就成功生成了二十多个账号。
这次经历也说明了一件事：即使没有编程基础，只要能够清晰描述需求，也可以通过自然语言让ChatGPT逐步完成自动化方案。从这个思路继续延伸，还可以尝试：
- 抓取小红书、Twitter等平台上的公开数据；
- 筛选公众号中阅读量达到十万加的文章；
- 批量调用HeyGen制作数字人视频；
- 将多个重复性的内容工作串联成自动化流程。
这些事情听起来复杂，但借助GPT-4、GitHub Copilot以及持续调试，并没有想象中那么难。真正需要投入的，往往是时间、耐心和不断试错的过程。
如果手头没有GPT-4或GitHub Copilot，也可以考虑一些免费的替代工具。例如Code Llama 34B和Replit AI，它们针对代码生成进行了专门优化，在编程场景下表现非常不错。
Code Llama可以通过Poe免费使用，不过目前不支持中文回答；Replit则推出了免费方案，虽然无法像付费版那样创建私有仓库，但对于轻量级开发和个人测试来说，已经基本够用。
下面就以HeyGen自动化注册为例，介绍如何从零开始搭建整套流程。整个过程中，代码主要由GPT生成，我们只需要负责提出需求、复制代码、运行测试并根据报错继续反馈。
## 一、先做需求拆解
开始之前，不要急着直接让ChatGPT写完整脚本。更合理的方式，是先把目标、操作流程和限制条件告诉它，让GPT先分析实现方案。
我们可以要求它回答以下问题：
- 自动化注册需要哪些工具？
- 哪些环节需要人工提供信息？
- 如何模拟浏览器操作？
- 验证码应该通过什么方式获取？
- 邮箱、代理、IP等问题是否需要提前处理？
![](img/zhuanqian_6f775a23c9e58e7c196867445c57b336.png)
根据GPT的分析，一个基础版本通常需要准备两项内容：
1. 使用Selenium等工具模拟浏览器行为；
2. 准备一个可以接收多个注册邮箱验证码的邮件系统。
验证码识别、IP限制、代理切换等问题，暂时可以放到后续阶段处理。如果HeyGen后续加强了风控，或者批量注册过程中出现限制，再考虑增加代理池、验证码识别和异常处理机制。
浏览器自动化部分，可以直接让GPT辅助生成代码。真正需要重点解决的是第二个问题：怎样拥有足够多的邮箱地址？
以Gmail为例，邮箱通常由“前缀+域名”组成，例如：
```text
example@gmail.com
```
如果我们拥有一个自己的域名，就可以建立一个Catch-all邮箱机制。这样，无论邮件发送到该域名下哪个前缀的地址，最终都能被转发到一个指定邮箱中。
因此，下一步的关键就变成了：如何用最低成本搭建自己的域名邮箱转发服务？
![](img/zhuanqian_6fc146098f237aa1bd31b119071b368a.png)
![](img/zhuanqian_cebacbf584d3c78cf8eef75436d6bc1c.png)
![](img/zhuanqian_38087dd6c7d5b966ca0e1a9a12c25baa.png)
通过继续和GPT沟通，可以得到几个重要结论：
- 只要拥有自己的域名，就能配置Catch-all邮箱；
- 发送到`任意前缀@你的域名`的邮件，都可以统一转发到指定邮箱；
- 后续只需要在这个邮箱中搜索HeyGen发送的注册邮件，并提取其中的验证码；
- 邮件转发可以使用ImprovMX、Forward Email等服务完成。
换句话说，整个方案最核心的资源其实只是一个域名。域名、邮件转发、验证码提取和浏览器操作，其余步骤都可以交给GPT协助完成。
## 二、注册域名并配置Catch-all邮箱
域名可以在Cloudflare、NameSilo或其他域名注册平台购买。部分后缀的价格非常低，几块钱就能注册一年。如果之前已经拥有自己的域名，也可以直接使用。
本文以`bardextension.io`为例。
邮件转发服务选择Forward Email。打开官网：
```text
https://forwardemail.net/
```
如果还没有账户，可以直接使用Gmail进行第三方登录。
![](img/zhuanqian_0e436d4e898f80448605966b7dfb5b70.png)
登录后，点击“Add Domain”，将自己的域名填写进去，例如：
```text
bardextension.io
```
![](img/zhuanqian_165eb8e1680e4446f9934ec7ca9a8e60.png)
提交后，页面会进入域名配置向导。
![](img/zhuanqian_ca6d25b308784682f5c757c8221d172a.png)
![](img/zhuanqian_7ffd30a05edb689ac85c07498f4213e3.png)
接下来，需要进入域名注册商的管理后台，根据Forward Email提供的说明修改DNS记录。
其中，MX记录是必须配置的一项。它的作用是把发送到该域名的邮件交给Forward Email处理，再由Forward Email统一转发到指定的Gmail邮箱。
以NameSilo为例，进入域名管理页面，在DNS设置区域填写引导页中提供的解析信息。
![](img/zhuanqian_dcefad6a1e3ebd1907047799de14bd71.png)
![](img/zhuanqian_270be988f9448f73cc5ce53e172e1ab8.png)
DNS记录填写完成后，回到Forward Email的配置页面，点击“Verify”。
![](img/zhuanqian_d86c920bcf3b07f75e44438b62d1d6c6.png)
如果页面显示“Congratulations”，说明域名验证已经成功。
到这里，Catch-all邮箱基本就配置好了。之后，无论邮件发送到：
```text
anything@bardextension.io
test@bardextension.io
random@bardextension.io
```
只要域名解析和转发设置正确，邮件都会进入之前绑定的Gmail邮箱。
可以先发送一封测试邮件，确认转发是否正常。
![](img/zhuanqian_a6525049ff3080ca0880cd277e6aff46.png)
邮箱转发搭建完成后，下一步就是让程序自动读取邮件，并从中找到HeyGen发送的验证码。
## 三、自动读取邮箱验证码
接下来继续向ChatGPT描述需求，让它提供从Gmail获取验证码的方案。
![](img/zhuanqian_0e8a61a160414a696c463bd6501144f8.png)
![](img/zhuanqian_0d7f3644968a6ff432165cb04a27db84.png)
GPT通常会给出两种常见方式：
- 使用Gmail API；
- 使用IMAP协议登录邮箱并搜索邮件。
两种方法都可以实现自动读取邮件。为了降低配置复杂度，这里选择IMAP方案。
首先，让GPT查询Gmail的IMAP配置方法，然后按照说明进入Gmail设置页面。
找到“查看所有设置”，进入“转发和POP/IMAP”相关选项，开启IMAP功能。
![](img/zhuanqian_6d8357917871eed68b0a1675f012b4a2.png)
![](img/zhuanqian_85743a45ab694d1358d89ca55e293fe8.png)
开启后保存设置，Gmail端的IMAP配置就完成了。
接下来，让GPT编写一个程序，用于登录Gmail、搜索HeyGen邮件，并从正文中提取验证码。
![](img/zhuanqian_acbd55721cf7a0cac9ac06e1e7a3ff49.png)
将生成的代码复制到本地运行。
```
import imaplib
import email
from email.header import decode_header
import re
def fetch_verification_code(gmail_user, gmail_password, sender, recipient):
"""
Fetches a six-digit verification code from Gmail using IMAP.
Parameters:
gmail_user (str): Gmail username.
gmail_password (str): Gmail password.
sender (str): Email address of the sender.
recipient (str): Email address of the recipient.
Returns:
str: The six-digit verification code, if found. Otherwise, returns None.
"""
# Connect to Gmail IMAP server
imap_url = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(gmail_user, gmail_password)
# Select the inbox
mail.select('inbox')
# Search for emails from sender to recipient
status, messages = mail.search(None, f'(FROM "{sender}" TO "{recipient}")')
# Check if any messages are found
if status != 'OK':
print("No messages found.")
return None
# Fetch messages
for num in messages[0].split():
typ, data = mail.fetch(num, '(RFC822)')
if typ != 'OK':
print(f"ERROR: Unable to fetch email {num}.")
continue
# Parse the email content
msg = email.message_from_bytes(data[0][1])
if msg.is_multipart():
for part in msg.walk():
content_type = part.get_content_type()
content_disposition = str(part.get("Content-Disposition"))
# Extract body
if "attachment" not in content_disposition and content_type == "text/plain":
body = part.get_payload(decode=True).decode()
# Search for a six-digit code in the email body
code = re.search(r'\b\d{6}\b', body)
if code:
return code.group()
return None
# Example usage
# Note: Replace 'your_username', 'your_password', 'sender@example.com', and 'recipient@example.com'
# with actual values before running this function.
# code = fetch_verification_code('your_username', 'your_password', 'sender@example.com', 'recipient@example.com')
# print(code)
```
第一次运行时，程序一般会要求填写Gmail用户名和密码。用户名就是自己的Gmail地址，但这里的密码不能直接使用日常登录密码。
如果不知道应该填写什么，可以继续向ChatGPT询问。
![](img/zhuanqian_e9f944b944cd4fb2fa15658d0e170088.png)
GPT会提示我们先启用Google账号的两步验证，然后创建应用专用密码。
完成两步验证后，进入Google账号安全设置，找到“应用专用密码”选项。
![](img/zhuanqian_980d1fc6b423e96ef6bf9c9e144af26b.png)
![](img/zhuanqian_1234d2cadc6f5649f858647ab4c5c057.png)
创建应用专用密码时，应用名称可以随意填写，例如：
```text
HeyGen Script
```
这个名称只是用于标记，不会影响程序运行。创建完成后，Google会生成一组专用密码。
将这组密码填写回脚本，而不是使用Gmail的日常登录密码，然后重新运行测试。
如果能够成功登录邮箱并读取HeyGen验证码，说明基础流程已经打通。
最初生成的代码可能查询速度较慢，可以继续要求ChatGPT优化，例如：
- 缩短邮件轮询间隔；
- 只搜索指定发件人；
- 限定邮件主题；
- 仅读取最近几分钟内的邮件；
- 找到验证码后立即停止查询；
- 增加连接失败和超时处理。
![](img/zhuanqian_50c407fb813139d00296d47b515c397b.png)
经过优化后，就可以得到一份相对完整的自动获取邮箱验证码代码。
需要强调的是，自动化注册和批量操作应遵守相关平台的服务条款、法律法规及反滥用规则。更稳妥的做法是将这套方法用于个人测试、自动化学习和合法的内容生产流程，不要用于绕过平台限制或制造违规账号。
从这次实践可以看到，ChatGPT不仅能回答问题，也能参与需求拆解、代码生成、错误排查和功能优化。对于编程基础较弱的人来说，只要把复杂目标拆分成邮箱配置、验证码读取、浏览器操作等多个小模块，就有机会一步步完成原本看似困难的自动化项目。
```
import imaplib
import email
from email.header import decode_header
import re
def fetch_latest_verification_code(gmail_user, gmail_password, sender, recipient):
"""
Fetches a six-digit verification code from the latest 10 unread emails in Gmail using IMAP.
Parameters:
gmail_user (str): Gmail username.
gmail_password (str): Gmail password.
sender (str): Email address of the sender.
recipient (str): Email address of the recipient.
Returns:
str: The six-digit verification code, if found. Otherwise, returns None.
"""
# Connect to Gmail IMAP server
imap_url = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(gmail_user, gmail_password)
# Select the inbox
mail.select('inbox')
# Search for unread emails from sender to recipient in the latest 10 emails
status, messages = mail.search(None, f'(FROM "{sender}" TO "{recipient}" UNSEEN)')
if status != 'OK':
print("No unread messages found.")
return None
# Fetch latest 10 messages
message_numbers = messages[0].split()[-10:]
for num in message_numbers:
typ, data = mail.fetch(num, '(RFC822)')
if typ != 'OK':
print(f"ERROR: Unable to fetch email {num}.")
continue
# Parse the email content
msg = email.message_from_bytes(data[0][1])
if msg.is_multipart():
for part in msg.walk():
content_type = part.get_content_type()
content_disposition = str(part.get("Content-Disposition"))
# Extract body
if "attachment" not in content_disposition and content_type == "text/plain":
body = part.get_payload(decode=True).decode()
# Search for a six-digit code in the email body
code = re.search(r'\b\d{6}\b', body)
if code:
return code.group()
return None
# Example usage
# Note: Replace 'your_username', 'your_password', 'sender@example.com', 'recipient@example.com'
# with actual values before running this function.
# code = fetch_latest_verification_code('your_username', 'your_password', 'sender@example.com', 'recipient@example.com')
# print(code)
```
在弄懂了如何无限申请临时邮箱并即时抓取校验码之后，下一个环节是把这套能力嫁接到 Heygen 的账号创建流程上。
## 让模型产出注册自动化脚本
上一步由 GPT 产出的片段里，拉取校验码的入口函数是 `fetch_verification_code`。基于此，我把 Heygen 前端注册的交互顺序、页面约束等细节再次整理给模型，让它补全一套可直接运行的浏览器自动化实现：
![](img/zhuanqian_fe39ac7249e0c5772b3cf3beb1a76269.png)
把这段实现下放到本地执行，Chrome 确实被唤起并自动进入了账号创建页，但邮箱输入框始终保持空白。原因是什么？我把现场现象和报错日志原样贴回给模型求助：
![](img/zhuanqian_b9be016bb5e4ee732b505c675d271a8e.png)
在确认了目标输入域的定位表达式后，我把这一信息同步给模型。调整后的版本本地试跑，结果除掉人工填写校验码这一步，其余环节全部走通了。
## 融合校验码抓取
此时的流程已经能完成除验证码之外的所有操作，只差把临时邮箱取码的逻辑串进来。做法很直接，把前面用于取码的片段复制进当前脚本即可，形成闭环：
```
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imaplib
import email
from email.header import decode_header
import re
gmail_user = "xxxx@gmail.com"
gmail_password = "xxxxxx"
def fetch_verification_code(sender, recipient, max_messages=10):
"""
Fetches a six-digit verification code from Gmail using IMAP.
Parameters:
gmail_user (str): Gmail username.
gmail_password (str): Gmail password.
sender (str): Email address of the sender.
recipient (str): Email address of the recipient.
Returns:
str: The six-digit verification code, if found. Otherwise, returns None.
"""
# Connect to Gmail IMAP server
imap_url = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(gmail_user, gmail_password)
# Select the inbox
mail.select('inbox')
print("begin search")
# Search for emails from sender to recipient
# status, messages = mail.search(None, '(UNSEEN)', f'(FROM "{sender}")', f'(TO "{recipient}")')
status, messages = mail.search(None, f'(FROM "{sender}" TO "{recipient}")')
print(messages)
# Check if any messages are found
if status != 'OK':
print("No messages found.")
return None
# Fetch messages
messages = messages[0].split()[-max_messages:]
for num in messages:
print(f"Fetching email {num}...")
typ, data = mail.fetch(num, '(RFC822)')
if typ != 'OK':
print(f"ERROR: Unable to fetch email {num}.")
continue
# Parse the email content
msg = email.message_from_bytes(data[0][1])
if msg.is_multipart():
for part in msg.walk():
content_type = part.get_content_type()
content_disposition = str(part.get("Content-Disposition"))
# Extract body
if "attachment" not in content_disposition and content_type == "text/plain":
body = part.get_payload(decode=True).decode()
print(f"body is :{body}")
# Search for a six-digit code in the email body
code = re.search(r'\b\d{6}\b', body)
if code:
return code.group()
return None
# 随机生成邮箱地址
def generate_email(domain, length=10):
characters = string.ascii_letters + string.digits
email_local_part = ''.join(random.choice(characters) for i in range(length))
return email_local_part + "@" + domain
# 随机生成密码
def generate_password(length=12):
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
return password
# 主函数
def main():
email = generate_email("bardextension.io", random.randint(5, 10))
password = generate_password(random.randint(12, 18))
# 初始化 WebDriver
driver = webdriver.Chrome()
driver.get("https://app.heygen.com/login")
try:
# 点击 Sign Up with Email
WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up with Email"))
).click()
print("click sign up with email")
# 输入邮箱地址并发送验证码
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "email"))
).send_keys(email)
driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Send Code')]]").click()
print("send code")
time.sleep(10)
# 假设使用 fetch_verification_code 函数获取验证码
code = fetch_verification_code("no_reply@mail.heygen.com", email)
if(code is None):
print("未获取到验证码，正在重试中")
time.sleep(20)
code = fetch_verification_code("no_reply@mail.heygen.com", email)
# 填写验证码并点击 Next Step
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "code"))
).send_keys(code)
print("code is :", code)
driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Next Step')]]").click()
print("next step")
# 输入密码并完成注册
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "password"))
).send_keys(password)
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "pwdConfirm"))
).send_keys(password)
driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Done')]]").click()
print(f"email: {email}, password: {password}")
# 关闭浏览器
driver.quit()
except Exception as e:
print("发生错误：", e)
driver.quit()
if __name__ == "__main__":
main()
```
再次运行，看得到账号创建流程顺利跑完：
![](img/zhuanqian_36a49b0d97464f61147ed98e1e91ae26.png)
## 批量产出的账号归档
接下来要做的是把每次创建成功的用户名与密码沉淀到同一个 Excel 表里，并支持循环批量执行。我把现有脚本再丢回给模型，请求它扩充持久化与循环能力：
![](img/zhuanqian_befcaef8ab832f5d41791d7ff5ce4e8c.png)
![](img/zhuanqian_3e40d3b0845c457963b6c374afc9207f.png)
跑通之后整体满足预期，不过出现了一个细节问题：当前写法是每累积 5 条就新建一个文件。我想要的是所有记录都写入同一份表格，只是每 5 条触发一次保存动作。于是继续让模型修改写入策略：
![](img/zhuanqian_398cdc7df336c4fa9df84764e2ec3bbf.png)
你有没有想过，用不到两小时的成本，就能让ChatGPT帮你写出一套自动注册脚本？还能顺手收获一大批邮箱资源。今天就把这个过程拆给你看。
一开始，脚本跑完一轮验证后，发现效果完全符合预期。做到这里其实已经算完成了，不过我们还可以再加一些校验逻辑，顺手把自动化痕迹藏起来，让整个流程看起来像是真人操作：
![](img/zhuanqian_532b33b436db6ee747c959a421f53eb0.png)
完整代码长这样：
```
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imaplib
import email
from fake_useragent import UserAgent
import pandas as pd
import re
gmail_user = "xxxxxx@gmail.com"
gmail_password = "xxxxxxxx"
def create_driver():
"""
创建并配置WebDriver。
"""
options = webdriver.ChromeOptions()
# Add arguments for ChromeOptions to make the browser more "real"
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
ua = UserAgent()
user_agent = ua.random
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
return driver
def fetch_verification_code(sender, recipient, max_messages=10):
"""
Fetches a six-digit verification code from Gmail using IMAP.
Parameters:
gmail_user (str): Gmail username.
gmail_password (str): Gmail password.
sender (str): Email address of the sender.
recipient (str): Email address of the recipient.
Returns:
str: The six-digit verification code, if found. Otherwise, returns None.
"""
# Connect to Gmail IMAP server
imap_url = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(gmail_user, gmail_password)
# Select the inbox
mail.select('inbox')
print("begin search")
# Search for emails from sender to recipient
status, messages = mail.search(None, '(UNSEEN)', f'(FROM "{sender}")', f'(TO "{recipient}")')
# status, messages = mail.search(None, f'(FROM "{sender}" TO "{recipient}")')
# Check if any messages are found
if status != 'OK':
print("No messages found.")
return None
# Fetch messages
messages = messages[0].split()[-max_messages:]
for num in messages:
print(f"Fetching email {num}...")
typ, data = mail.fetch(num, '(RFC822)')
if typ != 'OK':
print(f"ERROR: Unable to fetch email {num}.")
continue
# Parse the email content
msg = email.message_from_bytes(data[0][1])
if msg.is_multipart():
for part in msg.walk():
content_type = part.get_content_type()
content_disposition = str(part.get("Content-Disposition"))
# Extract body
if "attachment" not in content_disposition and content_type == "text/plain":
body = part.get_payload(decode=True).decode()
# Search for a six-digit code in the email body
code = re.search(r'\b\d{6}\b', body)
if code:
return code.group()
return None
# 随机生成邮箱地址
def generate_email(domain, length=10):
characters = string.ascii_letters + string.digits
email_local_part = ''.join(random.choice(characters) for i in range(length))
return email_local_part + "@" + domain
# 随机生成密码
def generate_password(length=12):
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
return password
# 主函数
def register_account():
"""
注册单个账号并返回邮箱和密码。
"""
email = generate_email("bardextension.io", random.randint(5, 10))
password = generate_password(random.randint(12, 18))
# 初始化 WebDriver
driver = create_driver()
driver.get("https://app.heygen.com/login")
try:
time.sleep(random.randint(1, 3))
# 点击 Sign Up with Email
WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up with Email"))
).click()
print("click sign up with email")
time.sleep(random.randint(1, 3))
# 输入邮箱地址并发送验证码
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "email"))
).send_keys(email)
driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Send Code')]]").click()
print("send code")
time.sleep(random.randint(5, 10))
# 假设使用 fetch_verification_code 函数获取验证码
code = fetch_verification_code("no_reply@mail.heygen.com", email)
if(code is None):
print("未获取到验证码，正在重试中")
time.sleep(20)
code = fetch_verification_code("no_reply@mail.heygen.com", email)
# 填写验证码并点击 Next Step
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "code"))
).send_keys(code)
time.sleep(random.randint(1, 3))
print("code is :", code)
driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Next Step')]]").click()
print("next step")
# 输入密码并完成注册
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "password"))
).send_keys(password)
WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "pwdConfirm"))
).send_keys(password)
time.sleep(random.randint(1, 3))
driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Done')]]").click()
print(f"email: {email}, password: {password}")
# 关闭浏览器
driver.quit()
return email, password
except Exception as e:
print("发生错误：", e)
driver.quit()
return None, None
def main():
all_accounts = pd.DataFrame()  # 初始化一个空的DataFrame
for _ in range(100):  # 循环100次
email, password = register_account()
if email and password:
new_account = pd.DataFrame({'Email': [email], 'Password': [password]})
all_accounts = pd.concat([all_accounts, new_account], ignore_index=True)
# 每5个账号保存一次
if len(all_accounts) % 2 == 0:
all_accounts.to_excel('all_accounts.xlsx', index=False)
if __name__ == "__main__":
main()
```
实际测试很有意思：把脚本启动后就去忙别的，午休回来一看，账号列表里已经躺了20个新注册的Heygen账号。
但麻烦也来了——每次运行脚本都会弹出一个浏览器窗口，搞得我别的活都干不了。怎么办？继续问ChatGPT呗。它给出的方案是加一个headless（无头）模式，让浏览器在后台默默工作。这下清净了，收工。
来算一笔账：整个折腾过程不到两小时，我们拿到了两样东西：
- 一个功能完整的Heygen自动注册脚本；
- 几乎不限量的个人邮箱，这些邮箱不只服务于Heygen，以后注册其他海外服务也能用。
而付出的成本呢？也就一个多小时的精力，加上一个域名，最便宜的域名十几块就能搞定。
当然，这个脚本还算不上完美。比如它没有可视化操作界面，只能通过命令行启动；再比如它暂时无法注册12积分的账号。不过这类问题，用ChatGPT继续迭代很快就能解决。如果大家有兴趣，欢迎留言，之后我会整理如何用GPT搞定可视化界面和12积分账号的注册。
再分享几个用GPT辅助自动化的实用心得：
- 如果两轮对话下来还没解决问题，别恋战，果断新开一个对话窗口，效率翻倍。
- 如果生成的回答不理想，别急着接受，多点击几次“重新生成答案”，说不定就有惊喜。
最后提醒一句：本文只是展示ChatGPT的一种应用可能，不鼓励任何违反网站协议的行为，所有内容仅供学习和教育使用。