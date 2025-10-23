import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pyimzml.ImzMLParser import ImzMLParser
import threading
import os

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

# ---------------------------- GUI Class -----------------------------
class MSIExtractApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MSI2Profiler-GUI")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f2f5")

        self.filepath = ""
        self.my_spectra = []
        self.df = None

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=6, relief="flat", background="#007acc", foreground="white")
        style.configure("TLabel", background="#f0f2f5")

        self.build_ui()

    def build_ui(self):
        ttk.Button(self.root, text="Load imzML File", command=self.load_imzml).pack(pady=10)
        self.class_entry = self.labeled_entry("Class Name")
        self.mz_min_entry = self.labeled_entry("Min m/z")
        self.mz_max_entry = self.labeled_entry("Max m/z")
        self.bin_entry = self.labeled_entry("Bin Size")

        self.normalize_var = tk.BooleanVar()
        self.log_var = tk.BooleanVar()
        ttk.Checkbutton(self.root, text="Normalize", variable=self.normalize_var).pack()
        ttk.Checkbutton(self.root, text="Log Transform", variable=self.log_var).pack()

        ttk.Button(self.root, text="Generate Matrix", command=self.start_processing).pack(pady=10)
        ttk.Button(self.root, text="Plot Average Spectrum", command=self.show_avg_spectrum).pack()
        ttk.Button(self.root, text="Export as CSV", command=self.export_csv).pack()
        ttk.Button(self.root, text="Export as Excel", command=self.export_excel).pack()

        ttk.Separator(self.root, orient='horizontal').pack(fill='x', pady=15)
        ttk.Button(self.root, text="Import CSV/XLSX to Concatenate", command=self.import_and_concat_files).pack()
        ttk.Button(self.root, text="Export Concatenated Data", command=self.export_combined).pack()

        self.progress = ttk.Progressbar(self.root, orient='horizontal', length=400, mode='determinate')
        self.progress.pack(pady=10)

    def labeled_entry(self, label):
        ttk.Label(self.root, text=label).pack()
        entry = ttk.Entry(self.root)
        entry.pack()
        return entry

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
                self.progress['value'] = (idx + 1) / total * 100
                self.root.update_idletasks()

            messagebox.showinfo("Success", f"{len(self.my_spectra)} spectra loaded.")
            self.progress['value'] = 0
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.progress['value'] = 0

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

    def show_avg_spectrum(self):
        if self.df is not None:
            plot_average_spectra(self.df)
        else:
            messagebox.showwarning("Warning", "No matrix generated yet.")

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
            f = filedialog.asksaveasfilename(defaultextension=".csv")
            if f:
                self.df.to_csv(f, index=False)
                messagebox.showinfo("Export", "Combined file saved.")
        else:
            messagebox.showwarning("Warning", "No data to export.")

# ---------------------------- Launch App -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MSIExtractApp(root)
    root.mainloop()
