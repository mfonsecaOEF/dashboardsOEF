# Streamlit dashboard — shareable team view

Interactive dashboard for **mitigation (GPC)** and **adaptation (CCRA)** data-coverage comparison.

Teammates do **not** need this repo locally once the app is deployed — they only need the URL.

## Local run

```bash
cd data_coverage/streamlit_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

## Share with the team (Streamlit Community Cloud)

Hosted from this repo: [mfonsecaOEF/dashboardsOEF](https://github.com/mfonsecaOEF/dashboardsOEF).

1. Ensure `data_coverage/` is pushed to GitHub (`main` or your deploy branch).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. **New app** → select **mfonsecaOEF/dashboardsOEF**.
4. Set:
   - **Main file path:** `data_coverage/streamlit_app/app.py`
   - **Python version:** 3.11+ recommended
   - **App URL** (optional custom slug)
5. Deploy. Copy the URL to the team.

## What the app shows

| View | Content |
|---|---|
| Overview | Mitigation vs adaptation scores side-by-side |
| Mitigation | Leaderboard + GPC sector readiness matrix + country drill-down |
| Adaptation | Leaderboard + CCRA theme matrix + country drill-down |

## Data inputs

Reads only the comparison CSVs (no secrets):

- `../mitigation/comparison/01_…` … `05_…`
- `../adaptation/comparison/01_…` … `05_…` (+ theme matrix `03b`)

Re-run / redeploy after regenerating comparison layers.
