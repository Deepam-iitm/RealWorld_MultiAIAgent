import webbrowser
import time
import pyautogui
import pyperclip
import os
from mcp.server.fastmcp import FastMCP

# Initialize MCP
mcp = FastMCP("ColabServer", port=8001)

@mcp.tool()
async def open_and_paste_colab(python_code: str) -> str:
    """
    Opens Google Colab, maximizes, and targets the TOP portion of the first cell
    to avoid triggering the 'Add Code/Text' buttons.
    """
    try:
        # 1. Clean the clipboard and set the code
        pyperclip.copy(python_code)
        
        # 2. Open Google Colab
        webbrowser.open("https://colab.new", new=2)

        # 3. Wait for stabilization
        print("Waiting 18 seconds for Colab stabilization...")
        time.sleep(18) 

        # 4. GET SCREEN SPECS
        width, height = pyautogui.size()

        # 5. MAXIMIZE WINDOW
        if os.name == 'nt':  # Windows
            pyautogui.hotkey('win', 'up')
        else:  # Mac
            pyautogui.hotkey('ctrl', 'command', 'f')
        time.sleep(1)

        # 6. STAGE 1: THE TARGETED CLICK
        target_x = width / 2
        target_y = height * 0.29 
        
        print(f"Clicking at {target_x}, {target_y}...")
        
        # Single click to focus the window
        pyautogui.click(target_x, target_y) 
        time.sleep(0.5)
        
        # Single click to focus the cell (Removed double-click to prevent extra cells)
        pyautogui.click(target_x, target_y)
        time.sleep(1)

        # 7. STAGE 2: FORCE ENTRY
        # Using 'Enter' ensures the cursor is active inside the text box
        pyautogui.press('esc')
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.5)

        # 8. STAGE 3: THE PASTE
        print("Pasting code...")
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')

        # RUN THE CELL
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('enter')
        
        return "Successfully injected code. No extra cells created."

    except Exception as e:
        return f"Automation failed: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")