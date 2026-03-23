import os
from dotenv import load_dotenv
from google import genai

# 1. 載入環境變數
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. 初始化客戶端
client = genai.Client(api_key=api_key)

# 3. 執行簡單測試
try:
    print("正在連線至 Gemini API...")
    response = client.models.generate_content(
                model="gemini-1.5-flash",
                        contents="請回答：測試成功！"
                            )
    print("-" * 20)
    print("API 回應內容：")
    print(response.text)
    print("-" * 20)
except Exception as e:
    print(f"錯誤訊息：{e}")