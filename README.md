# Profiler: Interactive Web Platform for Omics Data Analysis

> **Where Omics Meet Clarity**  
> Developed by [PRISM U1192 Laboratory](https://www.inserm.fr/en/research-inserm/prism-u1192/), Université de Lille  
> Protected by INSERM Transfert

[🌐 Try Profiler Live](https://prism-profiler.univ-lille.fr/)

Profiler is a next-generation, web-based platform for **multi-omics data analysis**, designed to simplify complex workflows and make advanced analytics accessible to all researchers, regardless of programming expertise.

Created by **Yanis Zirem (PhD Candidate, 2025)** under the guidance of **Prof. Michel Salzet** and **Prof. Isabelle Fournier**, Profiler bridges artificial intelligence, statistics, and intuitive visualization to deliver meaningful biological insights.

---

## Why Profiler?

🔍 Biomedical research generates *huge volumes* of omics data, from genes to metabolites.  
❗ The problem? Analysis bottlenecks due to complexity, software limitations, or coding expertise gaps.  
✅ The solution: **Profiler**, a smart, modular, and user-friendly web app that guides users from raw files to biological interpretation.

---

## 🌟 Key Features

## From Raw Files to Biological Insight
Profiler provides a complete end-to-end workflow : 

### Multi-Omics Compatibility
Handle proteomics, metabolomics, lipidomics, genomics, and transcriptomics datasets — all in one platform.

### Raw Data Conversion
Supports formats from major vendors (Bruker, Thermo, Waters) with conversion to open standards: `mzML`, `mzXML`, `mzDB`, `mz5`.

### Intuitive Preprocessing
Normalize, filter, bin, and impute missing values without writing a single line of code.

### AI & Statistical Integration
Train over 25 machine learning models, use deep learning, and apply classical tests — no switching between tools.

### Biomarker Discovery & Explainability
Reveal predictive features using **SHAP**, **LIME**, volcano plots, clustering, and more.

### Survival Analysis
Built-in tools for **Kaplan-Meier** curves, **Cox regression**, and clinical outcomes.

### Smart Recommendations
Let Profiler suggest the best preprocessing steps and statistical strategies based on your dataset.

### Pathway Enrichment Analysis
Explore biological pathways and functional annotation for deeper interpretation.

### Wizard Mode
Automated workflows for real-time predictions or guided post-hoc analysis.

### High-Performance Backend
Profiler is engineered for **speed** and **scalability**, ideal for large-scale omics projects.

---

## Additional Tools

### MSI2profiler: Mass Spectrometry Imaging Data Extractor for Profiler

`MSI2profiler.py` is a standalone desktop application developed with Tkinter to extract and bin spectra from MSI files (imzML format). It generates labeled CSV/Excel files ready for analysis in Profiler.

**Features:** 
- Load MSI .imzML files from whole tissue sections or regions of interest (ROIs)
- Bin spectra intensities over a selectable mass range with configurable bin size
- Normalize and optionally log-transform intensities.
- Export processed data as labeled CSV or Excel files.
- Visualize average spectra interactively to verify extraction consistency and detect errors
- Reuse the workflow for multiple ROIs
- Concatenate multiple CSV/Excel files into a single dataset for tabular import into Profiler

**To run:**

```bash
python MSI2profiler.py
```
Make sure to have dependencies installed: pip install pandas numpy plotly pyimzml

## 📂 Example Datasets

Sample datasets are included for testing and exploration:

```

├── Bruker_data/                    # Raw mass spectrometry data (zipped) from Bruker instruments  
├── Waters_data/                   # Raw mass spectrometry data (zipped) from Waters instruments  
├── DIA-NN_data/                   # DIA-NN processed output files (report.pg_matrix.tsv)  
├── Maxquant_data/                 # MaxQuant output files (proteinGroups.txt)  
├── Tabular_data_multi_omics/      # Cleaned and structured multi-omics datasets   
│   ├── Binary_classes/  
│   │   ├── toy_lipidomics_tumor_aggressiveness.csv      # Simulated lipidomics data (Aggressive vs NonAggressive)  
│   │   ├── toy_proteomics_tumor_aggressiveness.csv      # Simulated proteomics data 
│   │   ├── toy_rnaseq_tumor_aggressiveness.csv          # Simulated RNA-seq count data  
│   │   └── toy_metabolomics_tumor_aggressiveness.csv    # Simulated metabolomics profiles  
│   ├── Multi_classes/  
│   │   ├── toy_lipidomics_tumor_necrosis_healthy.csv    # Simulated lipidomics data (3-class Tumor, Necrosis and healthy samples)  
│   │   ├── toy_proteomics_tumor_necrosis_healthy.csv    # Simulated proteomics data (3-class)  
│   │   ├── toy_rnaseq_tumor_necrosis_healthy.csv        # Simulated RNA-seq (3-class)  
│   │   └── toy_metabolomics_tumor_necrosis_healthy.csv  # Simulated metabolomics (3-class)  
├── Survival_data/  
│   ├── clinical_and_LipidsMarkers.csv         # Clinical variables + lipid markers for Cox modeling  
│   └── statuts_patients.csv                  # Pre-processed survival data for Kaplan–Meier analysis  
```
---
**Note:** The Tools/ folder contains the MSI2profiler.py application along with any necessary scripts or utilities for MSI data processing.

## Who Should Use Profiler?

- 🔬 Researchers needing reproducible, end-to-end omics workflows  
- 🧑‍⚕️ Clinicians exploring biomarkers and survival outcomes  
- 🎓 Students & bioinformaticians learning data science methods  
- Core facilities seeking robust, shareable analytical pipelines  

---

## Getting Started

1. Visit: [https://prism-profiler.univ-lille.fr/](https://prism-profiler.univ-lille.fr/)
2. Upload a dataset (use the samples provided or your own)
3. Dive into preprocessing, modeling, visualization, and more!

✅ No installation required — fully browser-based with privacy-preserving execution.

---

## 🛠️ Tech Stack

Built with:
- **Python**
- **Streamlit**
- **scikit-learn**
- **pandas**
- **plotly**
- **lifelines**
- **Tensorflow**
- Custom modules for omics parsing, modeling, visualization, and statistical analysis

---

## 📘 Documentation

>A comprehensive PDF manual and full user guide available inside the app: tooltips, guided walkthroughs, and contextual help.

---

## 🤝 Contributing

We welcome contributions! You can help by:
- Submitting example datasets
- Suggesting features or improvements
- Reporting bugs via GitHub issues

---

## 👥 Authors

**Yanis Zirem**, PhD Candidate (2025)  
📧 yanis.zirem@univ-lille.fr

Supervised by:
- **Prof. Michel Salzet** (michel.salzet@univ-lille.fr)  
- **Prof. Isabelle Fournier** (isabelle.fournier@univ-lille.fr)

[PRISM U1192 Laboratory](https://www.inserm.fr/en/research-inserm/prism-u1192/), INSERM – Université de Lille

---

## 📄 License & IP Notice

**Profiler is proprietary software** developed by the PRISM U1192 Laboratory and protected by **INSERM Transfert**.

- **All rights reserved**
- Reproduction, modification, or distribution is prohibited without prior written consent
- For licensing inquiries, contact the authors

---

> *Profiler: Empowering researchers to transform omics data into discovery.*
