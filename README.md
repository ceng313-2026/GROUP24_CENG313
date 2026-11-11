# CENG313 Data Science Project - Eedi: Mining Misconceptions in Mathematics

## Team Members
- Şevket Berat Tetik 23118080062 @beratetikk
- Alperen Örene 23118080006 @Alperenorene

## 1. Competition & Dataset Overview
- **Kaggle Competition:** [Eedi - Mining Misconceptions in Mathematics](https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics)
- **Problem Description:** Predicting the specific mathematical misconception associated with each incorrect distractor option in multiple-choice diagnostic questions.
- **Dataset Files:**
  * `train.csv`: Diagnostic questions, 4 answer choices (A-D), correct answer label, and target `MisconceptionId` for each distractor.
  * `test.csv`: Unlabeled test questions for generating top-25 misconception predictions.
  * `misconception_mapping.csv`: Mapping of 2,587 unique `MisconceptionId` values to their natural language descriptions (`MisconceptionName`).
  * `sample_submission.csv`: Required submission format evaluated with **MAP@25**.

## 2. Project Structure
```text
GROUP24_CENG313/
├── README.md
├── assignment1_eda_baseline.ipynb
├── assignment2_solution.ipynb
└── src/
    ├── data.py
    ├── models.py
    └── utils.py
```

## 3. Approach & Methodology
- **Assignment 1 (EDA & Baselines):** Exploratory Data Analysis on question/distractor distributions, missing target analysis, and text length statistics. Implementation of **Most Frequent (Top 25)**, **CountVectorizer (Bag-of-Words) + Cosine Similarity**, and **TF-IDF + Cosine Similarity** baseline retrieval models. Since the competition is closed, models are evaluated using an **80%-20% held-out validation split** (874 validation samples) with the **MAP@25** metric.
- **Assignment 2 (Proposed Solution):** *will be updated*

## 4. Results Comparison
| Model | Validation MAP@25 (Held-out Split) | Kaggle Public Score |
| :--- | :---: | :---: |
| Baseline 0 (Most Frequent Top 25) | **0.0363** | N/A (Held-out split) |
| Baseline 1 (BoW / CountVectorizer + Cosine Similarity) | **0.1292** | N/A (Held-out split) |
| Baseline 2 (TF-IDF + Cosine Similarity) | **0.1389** | N/A (Held-out split) |
| Proposed Solution (Assignment 2) | TBD | TBD |

## 5. How to Run the Notebooks
1. Open `assignment1_eda_baseline.ipynb` or `assignment2_solution.ipynb` in Google Colab.
2. Ensure the `src/` directory and Kaggle CSV files are in the working directory.
3. Run all cells sequentially from top to bottom.

## 6. Progress Logs
- **Step 1:** Repository created, initial modular folder structure (`src/`) and `README.md` initialized.
- **Step 2:** Implemented data loading, missing value summary, and wide-to-long distractor formatting in `src/data.py`.
- **Step 3:** Implemented visualization utilities and the `MAP@25` evaluation metric in `src/utils.py`; completed Exploratory Data Analysis (EDA) in `assignment1_eda_baseline.ipynb`.
- **Step 4:** Implemented `MostFrequentBaseline` and `TextSimilarityBaseline` (CountVectorizer & TF-IDF) in `src/models.py` and evaluated all baseline models on a 20% held-out validation split.

## 7. Validation & Submission History
| Date | Evaluation Method | Description | Score (MAP@25) |
| :--- | :--- | :--- | :---: |
| 11 Nov 2026 | Held-out Split (20%) | Assignment 1 Most Frequent (Top 25) Baseline | 0.0363 |
| 11 Nov 2026 | Held-out Split (20%) | Assignment 1 CountVectorizer + Cosine Similarity Baseline | 0.1292 |
| 11 Nov 2026 | Held-out Split (20%) | Assignment 1 TF-IDF + Cosine Similarity Baseline | 0.1389 |
