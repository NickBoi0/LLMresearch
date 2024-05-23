from demo_openai import OpenAI

client = OpenAI(
    api_key="KEY HERE"
)

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://www.frommers.com/system/media_items/attachments/000/868/461/s980/Frommers-New-York-City-Getting-Around-1190x768.jpg?1647177178",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])