import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pyimzml.ImzMLParser import ImzMLParser
import threading

# ---------------------------- Spectrum Binning Function -----------------------------
def matrix_class_binned(my_spectra, class_name="Class", bin_size=0.1, mz_min=600, mz_max=1000, normalize=False, log_transform=False):
    bin_edges = np.arange(mz_min, mz_max + bin_size, bin_size)
    bin_centers = np.round((bin_edges[:-1] + bin_edges[1:]) / 2, 2)
    n_bins = len(bin_centers)
    n_spectra = len(my_spectra)
    intensity_matrix = np.zeros((n_spectra, n_bins), dtype=np.float32)

    for i, spectrum in enumerate(my_spectra):
        mz_values, intensities, _ = spectrum
        bin_indices = np.digitize(mz_values, bin_edges) - 1
        for b_idx, intensity in zip(bin_indices, intensities):
            if 0 <= b_idx < n_bins:
                intensity_matrix[i, b_idx] += intensity

    if normalize:
        row_sums = intensity_matrix.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        intensity_matrix = intensity_matrix / row_sums

    if log_transform:
        intensity_matrix = np.log1p(intensity_matrix)

    df = pd.DataFrame(intensity_matrix, columns=bin_centers)
    df.insert(0, "Class", [class_name] * n_spectra)
    return df

# ---------------------------- Plot Function -----------------------------
def plot_average_spectra(data, class_column='Class'):
    fig = go.Figure()
    unique_classes = data[class_column].unique()
    for class_label in unique_classes:
        class_data = data[data[class_column] == class_label].drop(columns=[class_column])
        mean_spectrum = class_data.mean()
        fig.add_trace(go.Scatter(x=mean_spectrum.index, y=mean_spectrum.values, mode='lines', name=f'Class {class_label}'))
    fig.update_layout(width=1000, xaxis_title='m/z', yaxis_title='Intensity')
    fig.show()



class MSIExtractApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MSI2Profiler-GUI")
        self.root.geometry("1100x850")  # Fenêtre plus large
        self.root.configure(bg="#f0f2f5")
        self.filepath = ""
        self.my_spectra = []
        self.df = None
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Accent.TButton", background="#1E90FF", foreground="white", font=("Arial", 10, "bold"), padding=10)
        style.map("Accent.TButton", background=[("active", "#0066CC"), ("pressed", "#004499")])
        style.configure("TLabel", background="#f0f2f5", font=("Arial", 10))
        style.configure("TCheckbutton", background="#f0f2f5", font=("Arial", 10))
        self.build_ui()

    def build_ui(self):
        # -------- Description --------
        self.frame_desc = ttk.LabelFrame(self.root, text="About MSI2Profiler")
        self.frame_desc.pack(padx=10, pady=10, fill='both', expand=True)
        desc_text = (
            "MSI2Profiler is an additional desktop tool for Profiler, designed to extract and preprocess Mass Spectrometry Imaging data from imzML files for direct import into Profiler for downstream analysis.\n\n"
            "Features:\n"
            "• Load MSI .imzML files from tissue sections or ROIs\n"
            "• Bin spectra with configurable mass range and bin size\n"
            "• Normalize and log-transform intensities\n"
            "• Export CSV/Excel files ready for Profiler\n"
            "• Visualize average spectra\n"
            "• Concatenate multiple CSV/Excel files"
        )
        desc_label = ttk.Label(
            self.frame_desc,
            text=desc_text,
            justify=tk.LEFT,
            wraplength=1100,
            font=("Arial", 9, "bold"),
            foreground="#333333"
        )
        desc_label.pack(padx=5, pady=5, fill='both', expand=True)

        # -------- Frame principal en deux colonnes --------
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # -------- Colonne de gauche : Chargement et Preprocessing --------
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Chargement
        self.frame_top = ttk.Frame(self.left_frame)
        self.frame_top.pack(pady=10, fill='x')
        ttk.Button(self.frame_top, text="Load imzML File", style="Accent.TButton", command=self.load_imzml).pack()

        # Options de preprocessing
        self.frame_middle = ttk.LabelFrame(self.left_frame, text="Processing Options")
        self.frame_middle.pack(padx=10, pady=10, fill='x')
        ttk.Label(self.frame_middle, text="Class Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.class_entry = ttk.Entry(self.frame_middle)
        self.class_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.frame_middle, text="Min m/z").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.mz_min_entry = ttk.Entry(self.frame_middle)
        self.mz_min_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(self.frame_middle, text="Max m/z").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.mz_max_entry = ttk.Entry(self.frame_middle)
        self.mz_max_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(self.frame_middle, text="Bin Size").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.bin_entry = ttk.Entry(self.frame_middle)
        self.bin_entry.grid(row=3, column=1, padx=5, pady=5)
        self.normalize_var = tk.BooleanVar()
        self.log_var = tk.BooleanVar()
        ttk.Checkbutton(self.frame_middle, text="Normalize", variable=self.normalize_var).grid(row=4, column=0, padx=5, pady=5, sticky="w")
        ttk.Checkbutton(self.frame_middle, text="Log Transform", variable=self.log_var).grid(row=4, column=1, padx=5, pady=5, sticky="w")
        ttk.Button(self.frame_middle, text="Generate Matrix", style="Accent.TButton", command=self.start_processing).grid(row=5, column=0, columnspan=2, pady=10)

        # Boutons d'export et visualisation
        self.frame_bottom_left = ttk.Frame(self.left_frame)
        self.frame_bottom_left.pack(pady=10, fill='x')
        ttk.Button(self.frame_bottom_left, text="Plot Average Spectrum", style="Accent.TButton", command=self.show_avg_spectrum).pack(pady=5)
        ttk.Button(self.frame_bottom_left, text="Export CSV", style="Accent.TButton", command=self.export_csv).pack(pady=5)
        ttk.Button(self.frame_bottom_left, text="Export Excel", style="Accent.TButton", command=self.export_excel).pack(pady=5)

        # -------- Colonne de droite : Concatenation --------
        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.frame_concat = ttk.LabelFrame(self.right_frame, text="Concatenation/Export")
        self.frame_concat.pack(padx=10, pady=10, fill='both', expand=True)
        ttk.Button(self.frame_concat, text="Import CSV/XLSX to Concatenate", style="Accent.TButton", command=self.import_and_concat_files).pack(pady=5)
        ttk.Button(self.frame_concat, text="Export Concatenated Data", style="Accent.TButton", command=self.export_combined).pack(pady=5)

        # -------- Progress Bar --------
        self.progress = ttk.Progressbar(self.root, orient='horizontal', length=500, mode='determinate')
        self.progress.pack(pady=5)
        self.progress_label = ttk.Label(self.root, text="Progress: 0%")
        self.progress_label.pack()

        # Configuration de la grille pour que les colonnes s'étirent
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

    # [Le reste de tes méthodes reste identique]

    # ---------------------------- File Loading -----------------------------
    def load_imzml(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("imzML files", "*.imzML")])
        if not self.filepath:
            return
        threading.Thread(target=self._parse_imzml).start()

    def _parse_imzml(self):
        try:
            parser = ImzMLParser(self.filepath)
            total = len(parser.coordinates)
            self.my_spectra = []

            for idx, (x, y, z) in enumerate(parser.coordinates):
                mzs, intensities = parser.getspectrum(idx)
                self.my_spectra.append([mzs, intensities, (x, y, z)])
                progress_pct = int((idx + 1) / total * 100)
                self.progress['value'] = progress_pct
                self.progress_label.config(text=f"Progress: {progress_pct}%")
                self.root.update_idletasks()

            messagebox.showinfo("Success", f"{len(self.my_spectra)} spectra loaded.")
            self.progress['value'] = 0
            self.progress_label.config(text="Progress: 0%")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.progress['value'] = 0
            self.progress_label.config(text="Progress: 0%")

    # ---------------------------- Processing -----------------------------
    def start_processing(self):
        threading.Thread(target=self.generate_matrix).start()

    def generate_matrix(self):
        try:
            class_name = self.class_entry.get()
            mz_min = float(self.mz_min_entry.get())
            mz_max = float(self.mz_max_entry.get())
            bin_size = float(self.bin_entry.get())
            normalize = self.normalize_var.get()
            log_transform = self.log_var.get()

            self.progress.start(10)
            self.df = matrix_class_binned(
                self.my_spectra, class_name, bin_size, mz_min, mz_max, normalize, log_transform
            )
            self.progress.stop()
            messagebox.showinfo("Matrix Generated", f"{self.df.shape[0]} spectra and {self.df.shape[1]-1} bins.")
        except Exception as e:
            messagebox.showerror("Processing Error", str(e))
            self.progress.stop()

    # ---------------------------- Plot -----------------------------
    def show_avg_spectrum(self):
        if self.df is not None:
            plot_average_spectra(self.df)
        else:
            messagebox.showwarning("Warning", "No matrix generated yet.")

    # ---------------------------- Export -----------------------------
    def export_csv(self):
        if self.df is not None:
            f = filedialog.asksaveasfilename(defaultextension=".csv")
            if f:
                self.df.to_csv(f, index=False)
                messagebox.showinfo("Export", "CSV file saved.")
        else:
            messagebox.showwarning("Warning", "No data to export.")

    def export_excel(self):
        if self.df is not None:
            f = filedialog.asksaveasfilename(defaultextension=".xlsx")
            if f:
                self.df.to_excel(f, index=False)
                messagebox.showinfo("Export", "Excel file saved.")
        else:
            messagebox.showwarning("Warning", "No data to export.")

    # ---------------------------- Concatenate -----------------------------
    def import_and_concat_files(self):
        files = filedialog.askopenfilenames(filetypes=[("Data files", "*.csv *.xlsx")])
        if not files:
            return
        try:
            df_list = []
            for f in files:
                if f.endswith(".csv"):
                    df_list.append(pd.read_csv(f))
                elif f.endswith(".xlsx"):
                    df_list.append(pd.read_excel(f))
            self.df = pd.concat(df_list, axis=0, ignore_index=True)
            messagebox.showinfo("Import Success", f"{len(files)} files imported and concatenated.")
        except Exception as e:
            messagebox.showerror("Import Error", str(e))

    def export_combined(self):
        if self.df is not None:
            f = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
            if f:
                if f.endswith(".csv"):
                    self.df.to_csv(f, index=False)
                else:
                    self.df.to_excel(f, index=False)
                messagebox.showinfo("Export", f"Concatenated data saved to {f}.")
        else:
            messagebox.showwarning("Warning", "No concatenated data to export. Import files first.")

# ---------------------------- Launch App -----------------------------
if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = MSIExtractApp(root)
    root.mainloop()
