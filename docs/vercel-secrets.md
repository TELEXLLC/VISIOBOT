# Vercel API Tokens & Project ID

To use the automated environment variable workflow, you need:

## 1. VERCEL_TOKEN

- Go to [Vercel Account Settings > Tokens](https://vercel.com/account/tokens)
- Click "Create Token"
- Name it (e.g. `github-actions`), copy and save it.

## 2. VERCEL_PROJECT_ID

- Go to your project on Vercel Dashboard.
- Click **Settings**.
- Scroll down to **General** > **Project ID**.
- Copy the long alphanumeric Project ID.

## 3. Add to GitHub Secrets

Add both `VERCEL_TOKEN` and `VERCEL_PROJECT_ID` as repository secrets:
- Go to your repo → Settings → Secrets → Actions → New repository secret

Set:
- `VERCEL_TOKEN`
- `VERCEL_PROJECT_ID`

Now your workflow can authenticate and set environment variables on Vercel securely.

---
