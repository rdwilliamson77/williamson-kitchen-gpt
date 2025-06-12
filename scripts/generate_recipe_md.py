import os
import yaml
from pathlib import Path

# Directories
SOURCE_DIR = Path("recipes")
OUTPUT_DIR = Path("recipes_rendered")
OUTPUT_DIR.mkdir(exist_ok=True)

INDEX_FILE = Path("index.md")

def generate_markdown(data):
    front_matter = {
        "title": data.get("title"),
        "layout": "recipe",
        "slug": data.get("slug"),
        "cuisine": data.get("cuisine"),
        "category": data.get("category"),
        "servings": data.get("servings"),
        "time": data.get("time"),
        "narrative": data.get("personal_notes"),
        "ingredients": data.get("ingredients"),
        "instructions": data.get("instructions"),
        "notes": data.get("notes"),
    }
    yaml_front = yaml.dump(front_matter, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{yaml_front}\n---\n"

# List to hold recipes for index
recipe_links = []

# Process each YAML file in the recipes folder
for yaml_file in SOURCE_DIR.glob("*.yaml"):
    print(f"Processing: {yaml_file.name}")
    try:
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        slug = data.get("slug") or data["title"].lower().replace(" ", "-")
        output_path = OUTPUT_DIR / f"{slug}.md"

        with open(output_path, "w", encoding="utf-8") as out:
            out.write(generate_markdown(data))

        recipe_links.append((data.get("title"), slug))
        print(f"✅ Rendered: {output_path.name}")

    except Exception as e:
        print(f"❌ Skipped {yaml_file.name}: {e}")

# Sort and write index.md
recipe_links.sort()
index_content = """---
layout: page
title: Home
---

<link rel="stylesheet" href="/assets/css/style.css">

# 🍽️ Welcome to the Williamson Family Kitchen

This is a living cookbook. Explore recipes, organized by type and flavor.

## 📖 Recipes

""" + "\n".join([f"- [{title}](/recipes/{slug}/)" for title, slug in recipe_links])

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(index_content)

print("✅ index.md updated.")
