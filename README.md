Group Members:
Ibrahim
Muath
Ruby
Sam
Our Chosen Stack:
How to run locally:
Setup (Supabase keys via env vars):



 Build & Deployment

 Live Site
https://campus-campanion-13.netlify.app/

 Build Configuration
- Build command: none (static site, no build step)
- Publish directory: . (root)
- Branch: main

- Hosted on Netlify (free tier)
- Connected to GitHub via Netlify Git integration
- Auto-deploys on every push to main

No environment variables required for the current static deployment.

If Supabase integration is added later, set the following in
Netlify → Site settings → Environment variables:
- SUPABASE_URL
- SUPABASE_ANON_KEY

1. Clone: git clone https://github.com/Muath923/ApplicationAppGroup13.git
2. Open index.html in any browser, or
3. Run a local server: python -m http.server 8000
