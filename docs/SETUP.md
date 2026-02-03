# GitHub Pages Setup Guide

## Enabling GitHub Pages

To make this site publicly accessible, follow these steps:

1. Go to your repository settings: `https://github.com/ShantiDraconis/indus-operational-mathematics/settings`
2. Navigate to **Pages** in the left sidebar
3. Under **Source**, select:
   - Branch: `main` (or your default branch)
   - Folder: `/docs`
4. Click **Save**
5. Your site will be published at: `https://shantidraconis.github.io/indus-operational-mathematics/`

## Verification

Once enabled, GitHub Pages typically takes a few minutes to build and deploy. You can check the deployment status:

1. Go to the **Actions** tab in your repository
2. Look for the "pages-build-deployment" workflow
3. Once complete, your site should be live

## Custom Domain (Optional)

If you want to use a custom domain:

1. In repository settings, under **Pages**
2. Enter your custom domain in the **Custom domain** field
3. Follow GitHub's DNS configuration instructions

## Content Updates

Any changes pushed to the `/docs` directory on your default branch will automatically trigger a rebuild and update the live site.

## Key Features Implemented

✅ **Defensive Messaging**: Clear statement that this is NOT phonetic decipherment
✅ **Conceptual Focus**: Emphasizes operational system, not linguistic translation
✅ **Modern Analogies**: JSON, workflow, status log, ledger
✅ **Core Diagram**: ENTITY → QUALIFIED → COUNTED → CLOSED
✅ **"What This Is NOT"**: Preemptive clarifications
✅ **Appropriate Language**: Uses "functions as", "models", "implements" (not "means" or "translates")
✅ **No Technical Details**: No sign lists, frequency tables, or formal models exposed
✅ **Three-Layer Access**: Public overview, academic methodology, technical access via links
✅ **FAQ Section**: Addresses common questions and potential criticisms
✅ **Master Phrase**: "The Indus script encodes states, quantities, and validation — not stories or speech."

## Site Structure

```
docs/
├── index.html      # Main homepage
├── style.css       # Styling
└── _config.yml     # Jekyll configuration
```

## Maintenance

Keep the public-facing documentation:
- ✅ Clear and concise
- ✅ Visual and conceptual
- ✅ Defensive against criticism
- ✅ Free of detailed technical content

Technical content belongs in:
- The full monograph
- Zenodo datasets
- Private repository sections (not in `/docs`)
