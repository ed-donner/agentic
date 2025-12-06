# LLM Engineering including Agentic AI Project

## Hands-on with LLMs and Agents

![Hands on LLM Engineering](assets/handson.jpg)

Welcome to the code to accompany the Hands-on LLM Engineering Live Event

### A note before you begin

I'm here to help you be most successful with your learning! If you hit any snafus, please do reach out by emailing me direct (ed@edwarddonner.com). It's always great to connect with people on LinkedIn - you'll find me here:  
https://www.linkedin.com/in/eddonner/

If you'd like to go more deeply into LLMs and Agents:  
- I have intensive online courses that cover this material, and tons more, with juicy commercial projects. An 8 week journey into all things LLM engineering, including RAG and fine-tuning. A 6 week adventure into Agentic AI. A 4 week deep dive into deploying AI for Production on the cloud with AIOps. And a briefing for leaders and founders on building a valuable AI business. [This post explains my courses and curriculum](https://edwarddonner.com/2025/05/28/connecting-my-courses-become-an-llm-expert-and-leader/). Please do get in touch if you decide to take any of them.
- I'm running a number of [Live Events](https://edwarddonner.com/2025/11/11/ai-live-event/) with O'Reilly and Pearson

## Pre-Setup: running Ollama locally with Open-Source

Before the full setup, try installing Ollama so you can see results immediately!
1. Download and install Ollama from https://ollama.com noting that on a PC you might need to have administrator permissions for the install to work properly
2. On a PC, start a Command prompt / Powershell (Press Win + R, type `cmd`, and press Enter). On a Mac, start a Terminal (Applications > Utilities > Terminal).
3. Run `ollama run llama3.2` or for smaller machines try `ollama run llama3.2:1b` - **please note** steer clear of Meta's latest model llama3.3 because at 70B parameters that's way too large for most home computers!  
4. If this doesn't work, you may need to run `ollama serve` in another Powershell (Windows) or Terminal (Mac), and try step 3 again
5. And if that doesn't work on your box, I've set up this on the cloud. This is on Google Colab, which will need you to have a Google account to sign in, but is free:  https://colab.research.google.com/drive/1-_f5XZPsChvfU1sJ0QqCePtIuc55LSdu?usp=sharing

## Setup instructions

Hopefully I've done a decent job of making these guides bulletproof - but please contact me right away if you hit roadblocks:

Full setup instructions are [here](setup/SETUP-new.md)

### An important point on API costs (which are optional! No need to spend if you don't wish)

During this example project, I'll suggest you try out the leading models at the forefront of progress, known as the Frontier models. These services have some charges, but I'll keep cost minimal - like, a few cents at a time. And I'll provide alternatives if you'd prefer not to use them.

Please do monitor your API usage to ensure you're comfortable with spend; I've included links below. There's no need to spend anything more than a couple of dollars for the entire course. Some AI providers such as OpenAI require a minimum credit like \$5 or local equivalent; we should only spend a fraction of it, and you'll have plenty of opportunity to put it to good use in your own projects. But it's not necessary in the least; the important part is that you focus on learning.

### Free alternative to Paid APIs

Here is an alternative if you'd rather not spend anything on APIs:  
Any time that we have code like:  
`openai = OpenAI()`  
You can use this as a direct replacement:  
`openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')`

Below is a full example:

```python
# You need to do this one time on your computer
!ollama pull llama3.2

from openai import OpenAI
MODEL = "llama3.2"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response.choices[0].message.content)
```

### The most important part

The best way to learn is by **DOING**. I don't type all the code during the workshop; I execute it for you to see the results. You should work through afterwards, running each cell, inspecting the objects to get a detailed understanding of what's happening. Then tweak the code and make it your own.

### Monitoring API charges

You can keep your API spend very low throughout this course; you can monitor spend at the OpenAI dashboard [here](https://platform.openai.com/usage).

Please do message me or email me at ed@edwarddonner.com if this doesn't work or if I can help with anything. I can't wait to hear how you get on.
