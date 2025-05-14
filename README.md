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

## 📂 Example Datasets

Sample datasets are included for testing and exploration:



├── Bruker_data/
├── Waters_data/
├── DIA-NN_data/
├── Maxquant_data/
├── Tabular_data_multi_omics/
    ├── Binary_classes/
│       ├── toy_lipidomics_tumor_aggressiveness.csv
│       ├── toy_proteomics_tumor_aggressiveness.csv
│       ├── toy_rnaseq_tumor_aggressiveness.csv
│       └── toy_metabolomics_tumor_aggressiveness.csv
    ├── Multi_classes/
│       ├── toy_lipidomics_tumor_necrosis_healthy.csv
│       ├── toy_proteomics_tumor_necrosis_healthy.csv
│       ├── toy_rnaseq_tumor_necrosis_healthy.csv
│       └── toy_metabolomics_tumor_necrosis_healthy.csv
├── Survival_data/
Tabular data contain 3 dataset (lipids ions), proteins and RNAseq)

---

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
