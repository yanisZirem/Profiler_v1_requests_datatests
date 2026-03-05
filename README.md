# Profiler v1.2 — Open Multi-Omics Analysis Platform

> **Where Omics Meet Clarity**  
> Developed by [PRISM U1192 Laboratory](https://www.inserm.fr/en/research-inserm/prism-u1192/), Université de Lille — Protected by INSERM Transfert

[🌐 Try Profiler Live](https://prism-profiler.univ-lille.fr/) &nbsp;·&nbsp;
[💻 Profiler Desktop](https://github.com/yanisZirem/prism-profiler) &nbsp;·&nbsp;
[📦 Test Datasets](https://github.com/yanisZirem/Profiler_v1_requests_datatests) &nbsp;·&nbsp;
[📄 Publication](https://doi.org/10.1093/bioinformatics/btaf644)

---

**Profiler** is a free, open, web-based platform for end-to-end multi-omics data analysis, from raw instrument files to publication-ready figures and biological interpretation. No programming required.


---

## Citation

If you use **Profiler** in your research, please cite:

> **Zirem, Y., Ledoux, L., Fournier, I., & Salzet, M.**  
> *Profiler: an open web platform for multi-omics analysis.*  
> **Bioinformatics**, Oxford University Press, 2025.  
> DOI: [10.1093/bioinformatics/btaf644](https://doi.org/10.1093/bioinformatics/btaf644)  
> PMID: [41324558](https://pubmed.ncbi.nlm.nih.gov/41324558/)

---

## What's New in v1.2

| Feature | Details |
|---|---|
| **GSEA enrichment** | Gene Set Enrichment Analysis from any output — volcano, heatmap, Venn/UpSet — joining ORA across 100+ databases |
| **Regression modeling** | ML and MLP for continuous targets (R², RMSE, residual plots, cross-validation) |
| **Longitudinal analysis** | Mixed-effects models, trajectory plots, repeated-measures stats (`Subject_ID` + `Time`) |
| **HTML report generation** | One-click self-contained export of all session plots, tables, and metrics |
| **SHAP / LIME improved** | Beeswarm, bar, force plots; sample-level and global explanations |
| **Raw data conversion** | Bruker `.d`, Waters `.raw`, Thermo Fisher → `.mzML` / `.mzXML` directly in the sidebar |

---

## Features

### Raw Data Conversion
Convert raw mass spectrometry files from major vendors directly in Profiler's sidebar — no external tool (e.g. MSConvert) required.

Supported: **Bruker** `.d` · **Waters** `.raw` · **Thermo Fisher** `.raw` → `.mzML` · `.mzXML` · `.mzDB` · `.mz5`

---

### Multi-Omics Support
Load and analyse data from any omics layer — all in one platform, no format conversion needed.

| Omics type | Supported parsers / formats |
|---|---|
| **Proteomics** | MaxQuant `proteinGroups.txt`, DIA-NN `pg_matrix.tsv`, Spectronaut, FragPipe, PEAKS, Perseus, Proteome Discoverer, Progenesis |
| **Metabolomics** | MetaboAnalyst, XCMS, MZmine, generic CSV (m/z + retention time) |
| **Lipidomics** | Generic CSV, LipidSearch output |
| **Transcriptomics** | DESeq2, edgeR, Salmon, kallisto, featureCounts, STAR, HTSeq |
| **Mass Spectrometry Imaging** | MSI2Profiler CSV output (from imzML, MALDI-MSI, DESI-MSI) |
| **Generic** | Any CSV / TSV / XLSX with a `Class` column |

Auto-detection of format, sample columns and software origin on upload. The `_meta` column system allows embedding clinical or batch metadata directly in the data file.

---

### Data Lab — QC & Exploration
Instant dataset overview before any analysis:

- Missing value heatmap & per-sample % report
- Feature distribution plots & CV analysis
- Isolation Forest outlier detection
- Class balance visualisation (SMOTE / ADASYN ready)
- Sample rename, edit & metadata management (`_meta` columns)

---

### Preprocessing Pipeline
A complete, ordered preprocessing workflow with data-driven auto-suggestions:

- **Imputation:** KNN, median, min/2
- **Normalisation:** log₂, Z-score, quantile, robust
- **Batch correction:** ComBat (NeuroCombat)
- **Variance filtering:** configurable threshold
- **Class balancing:** SMOTE, ADASYN
- **Post-QC validation dashboard**

---

### Data Visualisation
Every plot is fully interactive (Plotly) — zoom, pan, hover, lasso selection, export at publication resolution (PNG · SVG · PDF @2×).

- PCA · UMAP · t-SNE with class overlays
- Hierarchical clustering heatmap (Ward, complete, average…)
- Correlation matrix & cosine similarity heatmap
- Violin, boxplot, density distributions
- Signal profile (multi-feature line plot)

---

### Differential Analysis & Biomarker Discovery

- **Volcano plot** — binary and multi-class, interactive, configurable thresholds
- Statistical tests: t-test, Wilcoxon, Mann-Whitney, ANOVA, Kruskal-Wallis
- FDR correction: Benjamini-Hochberg, Bonferroni, Holm
- Heatmap of significant features with clustering
- **Venn & UpSet plots** — exclusive and shared feature sets across conditions
- Feature boxplots per group with significance bars
- Direct export of significant feature lists → enrichment module

---

### AI Modeling — Classification & Regression *(v1.2)*

**Classification:**
- Random Forest, XGBoost, SVM, Gradient Boosting, k-NN
- Logistic Regression, PLS-DA
- MLP (Deep Learning) — configurable layers, dropout, early stopping
- Cross-validation, hyperparameter tuning, ROC curves, confusion matrices

**Regression** *(new in v1.2):*
- Linear Regression, Random Forest Regressor, XGBoost Regressor, MLP
- R², RMSE, MAE metrics; residual plots; cross-validation

**Explainability:**
- SHAP: beeswarm, bar, force plots (sample-level & global)
- LIME: sample-level and global feature importance

**Deployment:**
- Export trained models as `.pkl`
- Real-time prediction on new unseen samples

---

### ORA + GSEA Pathway Enrichment *(v1.2)*

- **GSEA** *(new in v1.2)* — ranked gene set enrichment from any Profiler output
- **ORA** — over-representation analysis
- **100+ databases:** GO BP · MF · CC, Reactome, KEGG, WikiPathways, DrugBank, MSigDB, DisGeNET and more (via gseapy)
- **Auto-import** from volcano plots, heatmap clusters, Venn/UpSet exclusive sets, or manual paste
- Visualisations: bar plot, dot plot, heatmap, gene–pathway network

---

### Survival Analysis

- Kaplan–Meier estimator per group with confidence intervals
- Log-rank test with p-value annotation
- Cox proportional hazards model with forest plot of hazard ratios
- Risk stratification from continuous features
- Survival table & at-risk annotations

---

### Longitudinal Analysis *(v1.2)*

Dedicated module for repeated-measures and time-series omics data.  
Load a dataset with `Subject_ID` and `Time` columns to:

- Visualise molecular trajectories per feature and per subject
- Compare group-level dynamics with confidence intervals
- Run repeated-measures ANOVA and mixed-effects models
- Perform time-point pairwise comparisons
- Compatible with all omics types

---

### HTML Report Generation *(v1.2)*

Generate a complete, self-contained HTML report at any point in your session:

- All interactive Plotly figures embedded
- Statistical tables, model metrics, enrichment results
- Auto-generated table of contents
- Works offline — no server, no dependencies
- Timestamped and branded with Profiler + PRISM

---

## Test Datasets

All test datasets are open on GitHub: [yanisZirem/Profiler_v1_requests_datatests](https://github.com/yanisZirem/Profiler_v1_requests_datatests)

```
Profiler_v1_requests_datatests/
│
├── MaxQuant_data/                    # proteinGroups.txt — LFQ, auto-parsed
├── DIA-NN_data/                      # report.pg_matrix.tsv — DIA proteomics
├── Bruker_data/                      # Raw .d folders → convert in Profiler sidebar
├── Waters_data/                      # Raw .raw folders → convert in Profiler sidebar
│
├── Tabular_data_multi_omics/
│   ├── Binary_classes/               # Aggressive vs NonAggressive (4 omics types)
│   │   ├── toy_proteomics_tumor_aggressiveness.csv
│   │   ├── toy_metabolomics_tumor_aggressiveness.csv
│   │   ├── toy_lipidomics_tumor_aggressiveness.csv
│   │   └── toy_rnaseq_tumor_aggressiveness.csv
│   └── Multi_classes/                # Tumor vs Necrosis vs Healthy (4 omics types)
│       ├── toy_proteomics_tumor_necrosis_healthy.csv
│       ├── toy_metabolomics_tumor_necrosis_healthy.csv
│       ├── toy_lipidomics_tumor_necrosis_healthy.csv
│       └── toy_rnaseq_tumor_necrosis_healthy.csv
│
├── Survival_data/
│   ├── clinical_and_LipidsMarkers.csv   # Clinical variables + lipid markers (Cox model)
│   └── statuts_patients.csv             # Pre-processed data for Kaplan–Meier analysis
│
└── data_for_peerReview_paper/        # Exact datasets used in Bioinformatics 2025 figures
```

> **Tabular CSVs** (Binary & Multi-class): upload directly into Profiler — the `Class` column is auto-detected.  
> **Raw instrument data** (Bruker / Waters): convert to `.mzML` / `.mzXML` using the **Data Conversion** tab in Profiler's sidebar — no external tool needed.

---

## Additional Tool: MSI2Profiler

**MSI2Profiler** is a companion desktop tool for preprocessing Mass Spectrometry Imaging data.

- Load `.imzML` files from MALDI-MSI and DESI-MSI experiments
- Normalise spectra (TIC, Median, RMS), bin m/z features, concatenate ROIs
- Export a Profiler-ready CSV matrix for immediate statistical analysis

Download directly from the [Profiler homepage](https://prism-profiler.univ-lille.fr).

```bash
python MSI2profiler.py
# Dependencies: pip install pandas numpy plotly pyimzml
```

Full instructions: [MSI2Profiler README](https://github.com/yanisZirem/prism-profiler/blob/main/Additional_tools/MSI2Profiler/MSI2Profiler%20README.md)

---

## Who Should Use Profiler?

- 🔬 **Researchers** needing reproducible, end-to-end omics workflows
- 🧑‍⚕️ **Clinicians** exploring biomarkers and survival outcomes
- 🎓 **Students & bioinformaticians** learning omics data science methods
- 🏛️ **Core facilities** seeking robust, shareable analytical pipelines

---

## Getting Started

1. Go to [https://prism-profiler.univ-lille.fr/](https://prism-profiler.univ-lille.fr/)
2. Upload a dataset from the [test repository](https://github.com/yanisZirem/Profiler_v1_requests_datatests) or your own data
3. Follow the pipeline: QC → Preprocessing → Visualisation → Modeling → Enrichment → HTML Report

✅ No installation — fully browser-based  
✅ No account required  
✅ Free and open access

---

## Tech Stack

- **Python** · **Streamlit**
- **scikit-learn** · **XGBoost** · **TensorFlow** (MLP)
- **pandas** · **numpy** · **scipy** · **statsmodels**
- **plotly** · **lifelines** (survival)
- **gseapy** (GSEA + ORA)
- **shap** · **lime**
- **NeuroCombat** (ComBat batch correction)
- **imbalanced-learn** (SMOTE / ADASYN)
- Custom modules for omics parsing, format detection, modeling and reporting

---

## Authors & Contact

**Yanis Zirem**, PhD Candidate (2025)  
📧 yanis.zirem@univ-lille.fr

Supervised by:
- **Prof. Michel Salzet** — michel.salzet@univ-lille.fr
- **Prof. Isabelle Fournier** — isabelle.fournier@univ-lille.fr

**PRISM U1192 Laboratory** — Protéomique, Réponse Inflammatoire, Spectrométrie de Masse  
INSERM — Université de Lille

Protected by **INSERM Transfert** — APP/IDDN.FR2.0013.0300044.0005.S6.C7.20258.0009.312301

---

> *Profiler — Empowering researchers to transform omics data into discovery.*
