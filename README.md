# 🇩🇪 GermanyDreams

A modern, dark-themed portfolio and resource hub for international students planning their move to Germany. Built by **Vamshidhar Reddy** — Masters student in Computational Engineering at FAU Erlangen-Nürnberg, content creator, and student life guide.

🔗 **Live Site:** [germanydreams](https://vamshidharre.github.io/Germanydreams/index.html#) 

---

## ✨ What's Inside

| Page | Description |
|------|-------------|
| **Homepage** (`index.html`) | Hero section, content pillars, helpful tools, social links, and newsletter signup |
| **CGPA Calculator** (`calculator.html`) | Convert Indian CGPA/percentage to German grades using the Modified Bavarian Formula |
| **Visa Prep Checklist** (`visa.html`) | Document checklist and common visa interview questions with smart answers |
| **Cost Estimator** (`estimator.html`) | Monthly budget calculator by city, accommodation type, and lifestyle (2026 data) |
| **WG Message Generator** (`wgmessage.html`) | Generate polished German WG application messages that landlords actually reply to |
| **Job Application Tracker** (`jobtracker.html`) | Setup guide for an automated Gmail-to-Google-Sheets job tracker with analytics |
| **AI CV Tailor** (`cvtailor.html`) | AI-powered tool to tailor resumes and cover letters to specific job postings for better interview chances |
| **ATS Score Analyzer** (`atsanalyzer.html`) | Get brutally honest ATS analysis with recruiter-perspective feedback, keyword matching, and actionable improvement tips |
| **Packing & Buying Guide** (`packing.html`) | Master packing checklist with saved progress, India vs Germany price comparison, luggage rules, and buying links |

---

## 🎨 Design System — "Paper & Teal"

`index.html` and `packing.html` share a light, editorial design system in `assets/`:

- `assets/theme.css` — design tokens (surfaces, ink, teal/amber accents), layered
  shadows, typography scale, nav, buttons, cards, CSS flags, animations,
  `prefers-reduced-motion` and print rules
- `assets/site.js` — scroll progress, sticky nav + mobile sheet, staggered scroll
  reveal, mouse-tracked card spotlights, 3D tilt, magnetic buttons, count-up numbers

To roll the system out to another page, link both files and swap the page's
markup onto the shared classes (`.nav`, `.wrap`, `.section`, `.card`, `.btn`, …).

> German and Indian flags are rendered as CSS gradients (`.flag--de` / `.flag--in`),
> not emoji — Windows has no glyph for regional-indicator flag emoji.

---

## 🛠️ Tech Stack

- **HTML5** — Semantic, accessible markup
- **CSS3** — Custom properties, CSS Grid, Flexbox, `:has()`, `color-mix()`, scroll-driven reveals
- **Vanilla JavaScript** — Scroll reveals, magnetic buttons, spotlights, `localStorage` persistence
- **Google Fonts** — Bricolage Grotesque, Instrument Sans, JetBrains Mono (plus Syne / DM Sans on legacy pages)
- **No frameworks. No build tools. No dependencies.** — Just clean, fast, static files

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/vamshidharre/Germanydreams.git
   ```
2. Open `index.html` in your browser — that's it!

No build step, no package manager, no setup required.

---

## 📁 Project Structure

```
GermanyDreams/
├── assets/
│   ├── theme.css       # Shared design system (tokens, components, animations)
│   └── site.js         # Shared interaction layer
├── index.html          # Main landing page
├── packing.html        # Packing & buying guide with saved checklist
├── calculator.html     # CGPA → German grade converter
├── visa.html           # Visa preparation checklist
├── estimator.html      # Cost of living estimator
├── wgmessage.html      # WG message generator
├── jobtracker.html     # Job tracker setup guide
├── cvtailor.html       # AI-powered CV and cover letter tailor
├── atsanalyzer.html    # ATS score analyzer with recruiter feedback
├── Profile_pictur.jpg  # Profile photo
├── IMG_7204corr.JPG    # Additional image asset
├── premium.py          # Premium features script
├── modify.py           # Utility script
├── modify2.py          # Utility script
├── modify_fonts.py     # Font modification script
└── README.md           # This file
```

> `index.html` and `packing.html` use the shared design system. The remaining
> pages still carry their original self-contained dark theme.

---

## 📄 License

© 2026 Vamshidhar Reddy. All rights reserved.

---

## 🤝 Connect

- 🎥 [YouTube](https://www.youtube.com/channel/UCIY3viuqfg8BR9ucyCI2e1w)
- 📸 [Instagram](https://www.instagram.com/germanydreamz)
- 💼 [LinkedIn](https://www.linkedin.com/in/vamshidhar-reddy-7180551a2/)
- 💬 [WhatsApp Community](https://chat.whatsapp.com/C62Bkdk5G0kBMCBquVW1vg)

*Made with ❤️ from Stuttgart 🇩🇪*
