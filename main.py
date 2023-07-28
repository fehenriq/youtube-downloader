import os
from pytube import YouTube
from tkinter import messagebox, ttk
from ttkthemes import ThemedTk


def download_audio():
    url = url_entry.get()

    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        name = f"{yt.title}.mp3"

        if not os.path.exists("audios"):
            os.makedirs("audios")

        status_label.config(text="Baixando a música:\n" + name)

        download_dir = "audios/"

        download_path = os.path.join(download_dir, name)
        audio_stream.download(output_path=download_dir)
        downloaded_file = os.path.join(download_dir, audio_stream.default_filename)

        os.rename(downloaded_file, download_path)

        messagebox.showinfo(
            "Download concluído", "O download foi concluído com sucesso!"
        )
        status_label.config(text="Download concluído!")

    except Exception as e:
        messagebox.showerror("Erro", "Ocorreu um erro durante o download: " + str(e))
        status_label.config(text="Ocorreu um erro durante o download!")


root = ThemedTk(theme="adapta")
root.title("Downloader de música do YouTube")
root.set_theme(themebg=True, theme_name="adapta")

style = ttk.Style()
style.configure("big.TButton", font=("Helvetica", 14))
style.configure("big.TLabel", font=("Helvetica", 12))
style.configure("small.TLabel", font=("Helvetica", 9))

window_width = 550
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

url_label = ttk.Label(
    root, text="Cole o link da música que deseja baixar:", style="big.TLabel"
)
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=70)
url_entry.pack(pady=5)

download_button = ttk.Button(
    root, text="Baixar", command=download_audio, style="big.TButton"
)
download_button.pack(pady=10)

status_label = ttk.Label(root, text="", style="small.TLabel")
status_label.pack(pady=5)

root.mainloop()
