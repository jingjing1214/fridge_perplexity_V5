import requests

def ask_perplexity(api_key, user_input):
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "pplx-7b-chat",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    res = requests.post(url, headers=headers, json=payload)
    try:
        return res.json()["choices"][0]["message"]["content"]
    except:
        return "❌ 回覆失敗，請確認 API Key 是否正確或稍後再試。"