# Dataset Files

## ?? Download Instructions

Due to GitHub's file size limitations, large data files are not included in this repository.

### Required Files (Total: ~800MB)

Place the following files in this folder:

1. **features_df.csv** (631 MB)
2. **labeled_data.csv** (164 MB)  
3. **classes_df.csv**
4. **evaluation_results.pkl**
5. **y_test.pkl**
6. **test_anomalies.pkl**
7. **blockchain_data.pkl**
8. **bft_data.pkl**
9. **feature_cols.pkl**

### Download Options

#### Option 1: Google Drive (Recommended)
Download from: [Google Drive Link - Add your link here]

#### Option 2: Kaggle Dataset
```bash
pip install kaggle
kaggle datasets download -d ellipticco/elliptic-data-set
```

#### Option 3: Generate from Notebook
Run `notebook/blockchain_analysis.ipynb` and execute Cell 13 to export all files.

### Verification

After downloading, verify all files are present:
```bash
ls data/
```

You should see 9 data files plus this README.

---

**Note:** This project works without downloading files if you just want to view the code structure.


