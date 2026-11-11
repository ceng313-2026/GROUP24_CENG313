# CENG313 Data Science Project - Eedi: Mining Misconceptions in Mathematics

> **Note:** *Competition closed — evaluated on a held-out split.*

## Team Members
- **Group ID:** GROUP24 (`GROUP24_CENG313`)
- Şevket Berat Tetik - 23118080062 - [@beratetikk](https://github.com/beratetikk)
- Alperen Örene - 23118080006 - [@AlperenOrene](https://github.com/AlperenOrene)

## 1. Competition & Dataset Overview
- **Kaggle Competition:** [Eedi - Mining Misconceptions in Mathematics](https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics)
- **Problem Description:** Predicting the specific mathematical misconception associated with each incorrect distractor option in multiple-choice diagnostic questions, evaluated using **MAP@25**.
- **Dataset Files:**
  * `train.csv`: Diagnostic questions, 4 answer choices (A-D), correct answer label, and target `MisconceptionId` for each distractor.
  * `test.csv`: Unlabeled test questions for generating top-25 misconception predictions.
  * `misconception_mapping.csv`: Mapping of 2,587 unique `MisconceptionId` values to their natural language descriptions (`MisconceptionName`).
  * `sample_submission.csv`: Required submission format evaluated with **MAP@25**.

## 2. Project Structure
```text
GROUP24_CENG313/
├── README.md
├── requirements.txt
├── .gitignore
├── assignment1_eda_baseline.ipynb
└── src/
    ├── __init__.py
    ├── data.py
    ├── models.py
    └── utils.py
```

## 3. Approach & Methodology
- **Assignment 1 (EDA & Baselines):** Exploratory Data Analysis on question/distractor distributions, missing target analysis, duplicate checks, and text length statistics with written interpretations. Implementation of **Most Frequent (Top 25)**, **CountVectorizer (Bag-of-Words) + Cosine Similarity**, and **TF-IDF + Cosine Similarity** baseline retrieval models.
- **Held-Out Evaluation:** *Competition closed — evaluated on a held-out split.* We hold out **20% of valid labeled distractors from `train.csv`** (`random_state=42`, 874 validation samples) and evaluate models using the official **MAP@25** metric.
- **Assignment 2 (Proposed Solution):** *will be updated*

## 4. Results Comparison & Leaderboard Benchmark
| Model | Validation MAP@25 (20% Held-out Split) | Kaggle Public Score |
| :--- | :---: | :---: |
| Baseline 0 (Most Frequent Top 25) | **0.0363** | N/A (Held-out split) |
| Baseline 1 (BoW / CountVectorizer + Cosine Similarity) | **0.1292** | N/A (Held-out split) |
| Baseline 2 (TF-IDF + Cosine Similarity) | **0.1389** | N/A (Held-out split) |
| Proposed Solution (Assignment 2) | TBD | TBD |

* **Comparison with Top Public Scores:** On the Kaggle competition leaderboard, top deep-learning ensembles score around **0.45 – 0.65+**, whereas simple lexical public baselines score around **0.10 – 0.15**; our TF-IDF baseline (**0.1389**) matches standard lexical baselines but is ~0.30–0.50 points below top leaderboard models due to vocabulary mismatch between raw algebraic expressions and natural language misconception descriptions.

## 5. How to Download the Data & Run the Notebooks
1. **Download the Data:** 
   - Go to the [Kaggle Competition Data Page](https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics/data), accept the competition rules, and download `train.csv`, `test.csv`, `misconception_mapping.csv`, and `sample_submission.csv`.
   - Place the CSV files in the working directory. *Per course rules, raw CSV data files are excluded via `.gitignore` and not committed to the repository.*
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Notebook:**
   - Open `assignment1_eda_baseline.ipynb` in Google Colab or Jupyter Notebook.
   - Ensure the `src/` directory and dataset CSV files are in the working directory, then click **Restart & Run All**.

## 6. Progress Logs
- **Step 1:** Repository created, modular folder structure (`src/`, `requirements.txt`, `.gitignore`) and `README.md` initialized.
- **Step 2:** Implemented data loading, missing value summary, and wide-to-long distractor formatting in `src/data.py`.
- **Step 3:** Implemented visualization utilities and the `MAP@25` evaluation metric in `src/utils.py`; completed Exploratory Data Analysis (EDA) with written interpretations in `assignment1_eda_baseline.ipynb`.
- **Step 4:** Implemented `MostFrequentBaseline` and `TextSimilarityBaseline` (CountVectorizer & TF-IDF) in `src/models.py` and evaluated all baseline models on a 20% held-out validation split.

## 7. Validation & Submission History
| Date | Evaluation Method | Description | Score (MAP@25) |
| :--- | :--- | :--- | :---: |
| 11 Nov 2026 | Held-out Split (20%) | Assignment 1 Most Frequent (Top 25) Baseline | 0.0363 |
| 11 Nov 2026 | Held-out Split (20%) | Assignment 1 CountVectorizer + Cosine Similarity Baseline | 0.1292 |
| 11 Nov 2026 | Held-out Split (20%) | Assignment 1 TF-IDF + Cosine Similarity Baseline | 0.1389 |
