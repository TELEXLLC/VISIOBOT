# Discord Interactions Endpoint and Main Iframe URLs

## Discord Interactions Endpoint URLs

Set these in your Discord Developer Portal under **Interactions Endpoint URL** depending on the platform you deploy to:

- **Vercel Production:**  
  `https://visiobot.vercel.app/api/interactions`

- **Vercel Preview:**  
  `https://visiobot-git-main-telexs-projects.vercel.app/api/interactions`
  
  `https://visiobot-erhawlrrh-telexs-projects.vercel.app/api/interactions`

- **Netlify (replace with your actual Netlify domain if different):**  
  `https://visiobot.netlify.app/api/interactions`

---

## Main Iframe Path & URLs

Use these for embedding your main application as an iframe:

- **Vercel Production:**  
  - **Path:** `/`
  - **URL:** `https://visiobot.vercel.app/`

- **Vercel Preview:**  
  - **Path:** `/`
  - **URL:** `https://visiobot-git-main-telexs-projects.vercel.app/`  
    `https://visiobot-erhawlrrh-telexs-projects.vercel.app/`

- **Netlify:**  
  - **Path:** `/`
  - **URL:** `https://visiobot.netlify.app/`

---

## Example Table

| Platform             | Interactions Endpoint URL                        | Main Iframe Path | Main Iframe URL                           |
|----------------------|--------------------------------------------------|------------------|-------------------------------------------|
| Vercel Production    | https://visiobot.vercel.app/api/interactions     | /                | https://visiobot.vercel.app/              |
| Vercel Preview #1    | https://visiobot-git-main-telexs-projects.vercel.app/api/interactions | / | https://visiobot-git-main-telexs-projects.vercel.app/ |
| Vercel Preview #2    | https://visiobot-erhawlrrh-telexs-projects.vercel.app/api/interactions | / | https://visiobot-erhawlrrh-telexs-projects.vercel.app/ |
| Netlify              | https://visiobot.netlify.app/api/interactions    | /                | https://visiobot.netlify.app/             |

---

**Deploy an `/api/interactions` handler on all platforms, and set the Interactions Endpoint URL on Discord.**