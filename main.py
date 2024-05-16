import bas32,Affine,Rail
import tkinter as tk
from sympy import isprime
from tkinter import messagebox
from tkinter import ttk

def encrypt():
    text =''
    algorithm_name =''
    key1 = int(key_entry1.get())
    key2 = int(key_entry2.get())
    text = plaintext_entry.get()
    selected_algorithm = algorithm.get()
    if selected_algorithm == "affine cipher" :
        if key1 > 2 and isprime(key1):
            algorithm_name = Affine.affine_encryption(text,key1,key2)
        else:
            algorithm_name = "the number should be coprime with 26"
    elif selected_algorithm == "Rail_fence cipher":
        if(key1 < len(text) and key1 >= 2):
            algorithm_name = Rail.encryption(key1,text)
        else:
            messagebox.showinfo("hint","Enter key [2-%s]: " % (len(text) - 1))
            reset()
            algorithm_name="none"
        
    elif selected_algorithm == "base32 cipher":
        algorithm_name = bas32.base32_encode(text)
    else:
        algorithm_name = "None"
    encrypted_text.set(algorithm_name)


def decrypt():
    text =''
    algorithm_name =''
    key1 = int(key_entry1.get())
    key2 = int(key_entry2.get())
    text = plaintext_entry.get()
    selected_algorithm = algorithm.get()
    if selected_algorithm == "affine cipher":
        algorithm_name = Affine.affine_decryption(text,key1,key2)
    elif selected_algorithm == "Rail_fence cipher":
        algorithm_name = Rail.railfence(text,key1)
    elif selected_algorithm == "base32 cipher":
        algorithm_name = bas32.base32_decode(text)
    else:
        algorithm_name = "None"
    text = encrypted_text.get()
    encrypted_text.set(algorithm_name)

def reset():
    algorithm.set("")
    key_entry1.delete(0, tk.END)
    key_entry1.insert(0, '0')
    key_entry2.delete(0, tk.END)
    key_entry2.insert(0, '0')
    plaintext_entry.delete(0, tk.END)
    encrypted_text.set("")


root = tk.Tk()
root.title("Encryption & Decryption Algorithms")
root.geometry("800x400")


algorithm_frame = tk.Frame(root)
algorithm_frame.pack(pady=10)

algorithm_label = tk.Label(algorithm_frame, text="Choose Your Algorithm:")
algorithm_label.pack(anchor='w')

algorithm = tk.StringVar()

algorithm_combobox = ttk.Combobox(algorithm_frame, textvariable=algorithm)
algorithm_combobox['values'] = ("affine cipher", "Rail_fence cipher", "base32 cipher")
algorithm_combobox.pack(anchor='w')


plaintext_label = tk.Label(root, text="Text:")
plaintext_label.pack()
plaintext_entry = tk.Entry(root)
plaintext_entry.pack()

key_label1 = tk.Label(root, text="Key 1:")
key_label1.pack()
key_entry1 = tk.Entry(root)
key_entry1.pack()
key_entry1.insert(0, '0')


key_label2 = tk.Label(root, text="Key 2:")
key_label2.pack()
key_entry2 = tk.Entry(root)
key_entry2.pack()
key_entry2.insert(0, '0')


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt)
encrypt_button.pack(side=tk.LEFT, padx=5)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt)
decrypt_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(side=tk.BOTTOM, padx=10, pady=10)

encrypted_text_label = tk.Label(root, text="Result:")
encrypted_text_label.pack()
encrypted_text = tk.StringVar()
encrypted_text_entry = tk.Entry(root, textvariable=encrypted_text)
encrypted_text_entry.pack()
root.mainloop()