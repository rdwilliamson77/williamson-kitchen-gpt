# 🥘 Williamson Kitchen GPT

**A structured, conversational, and living family cookbook.**  
This project blends heirloom recipes, personal stories, metadata, and automation to preserve and share the Williamson family’s culinary legacy—designed to scale and grow for generations.

---

## 📁 Repo Contents

This repository includes:

- ✅ YAML-formatted family recipes with rich metadata
- 🎙️ Voice notes, written memories, and cultural context
- 🧠 Structured index and schema for GPT and automation
- 📸 Linked images and optional media
- 📘 Long-term roadmap for web, print, and voice applications

---

## 🗂 Folder Structure

| Folder | Purpose |
|--------|---------|
| `recipes/` | All recipe files in YAML format, one per file |
| `images/` | Supporting photos, named by slug (e.g. `chicken-piccata.jpg`) |
| `voice-notes/` | Optional audio notes or stories for individual recipes |
| `story_fragments/` | Written memories, rituals, or background lore |
| `techniques/` | Shared instructions like "make a roux" or "butterfly a chicken" |
| `metadata/` | Shared data: tags, substitutions, master template |
| `gpt-logic/` | Prompts, responses, and config files for GPT tuning |
| `exports/` | Cookbook drafts, PDFs, EPUBs, print-ready versions |
| `archive/` | Retired recipes or prior versions no longer in rotation |

---

## 🧬 Schema & Metadata

- The schema is defined in [`recipe_template.yaml`](./recipe_template.yaml)
- This template governs all recipes and is indexed by [`update_index.py`](./update_index.py)
- Fields include contextual metadata (story, contributor), structural data (tags, layout), and future-proof elements (style_class, display_order)

---

## 🎯 Project Goal

To create a **scalable and personal digital cooking companion**—a family-first GPT that can:

- Teach and guide home cooks with personal nuance
- Preserve culinary heritage with stories, voice, and taste
- Scale to support 100+ recipes, linked media, and intelligent search
- Export to **print** and **web** using consistent, style-aware formats

This is not just a recipe repo. It’s a family memoir in code.

---

*Maintained by Ryan Williamson. GPT-ready. Print-ready. Family-ready.*