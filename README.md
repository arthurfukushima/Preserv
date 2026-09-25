# Preserv Consultoria Ambiental

One-page corporate site for **Preserv Consultoria Ambiental** (environmental consulting for industry, agribusiness and commerce in Paraná), built with [Astro](https://astro.build).

**Live site:** https://preservambientalpr.com.br

## Structure

```text
src/pages/index.astro   the whole page: company data, services, FAQ, markup
src/styles/global.css   design tokens and styles
src/assets/hero.png     hero image (optimized at build time by Astro)
docs/clientrequest.md   original client briefing
docs/feedback/          client voice notes (.ogg, git-ignored) + transcripts (.md)
scripts/transcribe.py   transcribes the voice notes locally
```

Company data (phone, e-mail, address, hours) and the services and FAQ lists are at the top of `index.astro`. Items marked `TODO cliente` are waiting on the client.

## Commands

| Command           | Action                                  |
| :---------------- | :-------------------------------------- |
| `npm install`     | Install dependencies                    |
| `npm run dev`     | Dev server at `localhost:4321`          |
| `npm run build`   | Build to `./dist/`                      |
| `npm run preview` | Preview the build locally               |

## Client audio feedback

1. Drop the voice notes in `docs/feedback/`.
2. `pip install faster-whisper` (once), then `python scripts/transcribe.py`. It writes a Portuguese `.md` next to each audio file. It runs offline on the CPU.
3. Read the transcripts and apply the changes. Check names and numbers by ear, since Whisper can mishear them.

## Deploy

Every push to `main` builds and publishes to GitHub Pages through `.github/workflows/deploy.yml`. The custom domain is set by `public/CNAME` (DNS: four `A` records to GitHub Pages, `www` CNAME to `arthurfukushima.github.io`).
