
import os
import yaml
from pathlib import Path

# Directories
SOURCE_DIR = Path("recipes")
OUTPUT_DIR = Path("recipes_rendered")
OUTPUT_DIR.mkdir(exist_ok=True)

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

# Process each YAML file in the recipes folder
for yaml_file in SOURCE_DIR.glob("*.yaml"):
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    slug = data.get("slug") or data["title"].lower().replace(" ", "-")
    output_path = OUTPUT_DIR / f"{slug}.md"

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(generate_markdown(data))
