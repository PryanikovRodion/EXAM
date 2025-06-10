
from fastapi import FastAPI
import uvicorn
import tkinter as tk
import multiprocessing as mp

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_gui():
    root = tk.Tk()
    root.title("Simple GUI")
    tk.Label(root, text="Hello, this is a simple GUI!").pack()
    return root

def main():
    # Запуск сервера FastAPI в отдельном процессе через строку "main:app"
    server_process = mp.Process(
        target=uvicorn.run,
        args=("main:app",),
        kwargs={"host": "127.0.0.1", "port": 8000, "reload": False}
    )
    server_process.start()

    # Создание и запуск GUI
    root = create_gui()
    root.mainloop()
    # Завершение процесса сервера при закрытии GUI
    server_process.terminate()
    server_process.join()
    print("Server process terminated.")

if __name__ == "__main__":
    main()