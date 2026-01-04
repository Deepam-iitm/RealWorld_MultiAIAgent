# RealWorld Multi-AI Agent System using LangGraph & MCP

This project demonstrates a **real-world multi-AI agent architecture** built using **LangGraph** and **MCP (Model Context Protocol)**.  
It showcases how autonomous agents can interact with external tools, APIs, and system-level automation to solve practical tasks.

---

## 🚀 Project Overview

The repository contains multiple MCP-powered agents that can:

- 🌦️ Fetch real-time weather information using public APIs  
- 📓 Automatically open Google Colab and inject Python code  
- 🔗 Be orchestrated together using LangGraph workflows  
- 🤖 Act as real-world tool-using AI agents instead of just chatbots  

---

## 🧠 Architecture

- **LangGraph** → Agent orchestration & flow control  
- **MCP Servers** → Tool exposure as callable agent actions  
- **FastMCP** → Lightweight MCP server framework  
- **External APIs & OS Automation** → Real-world interaction  

---

## 🛠️ Agents & Tools

### 1️⃣ Weather Agent
- Fetches real-time weather using **Open-Meteo API**
- Input: City name
- Output: Temperature and wind speed

### 2️⃣ Colab Automation Agent
- Opens Google Colab automatically
- Pastes Python code into the first notebook cell
- Executes the cell without creating extra cells
- Uses:
  - `pyautogui`
  - `pyperclip`
  - `webbrowser`

---

## 📂 Project Structure

* weather_server.py # MCP server for weather tool
* colab_server.py # MCP server for Colab automation
* requirements.txt # Python dependencies
* langgraph_workflow.ipynb # LangGraph orchestration demo
* README.md

## 🧪 Steps to Use
1. Create the virtual environment and activate it
 * `python -m venv venv` 
 * `venv\Scripts\activate`

2. Install the requirements.txt
  * `pip install -r requirements.txt`

3. Get the your API KEYS and initialize them.
   
4. Run the weather_server.py and colab_server.py
  * `python weather_server.py` 
  * `python colab_server.py`
  
5. Select the kernel in notebook and start running the cells.
