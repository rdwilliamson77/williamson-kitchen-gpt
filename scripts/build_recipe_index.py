from pathlib import Path
import yaml
import datetime
import csv

# Paths
recipes_dir = Path("recipes")
index_yaml_file = Path("recipe_index.yaml")
index_csv_file = Path("recipe_index.csv")
index_log_file = Path("recipe_index.log")
index_md_file = Path("recipe_index.md")

DEFAULT_FIELDS = {
    "category": "main",
    "cuisine": "",
    "emotional_tags": [],
    "personal_notes": "",
    "story_ref": "",
    "image": "",
    "voice_note": "",
    "status": "draft",
    "collection": "",
    "created": "",
    "last_updated": "",
    "contributor": "Ryan Williamson",
    "related_recipes": []
}

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception:
        return {}

def generate_index():
    index = []
    logs = []
    today_str = datetime.date.today().isoformat()

    for recipe_file in recipes_dir.glob("*.yaml"):
        data = load_yaml(recipe_file)
        if not data or 'slug' not in data:
            logs.append(f"⚠️ Missing slug or unreadable file: {recipe_file.name}")
            continue

        entry = {
            "slug": data.get("slug"),
            "title": data.get("title", data.get("slug", "Untitled")),
            "category": data.get("category", DEFAULT_FIELDS["category"]),
            "cuisine": data.get("cuisine", DEFAULT_FIELDS["cuisine"]),
            "tags": data.get("tags", []),
            "emotional_tags": data.get("emotional_tags", DEFAULT_FIELDS["emotional_tags"]),
            "personal_notes": data.get("personal_notes", DEFAULT_FIELDS["personal_notes"]),
            "story_ref": data.get("story_ref", DEFAULT_FIELDS["story_ref"]),
            "image": data.get("image", f"images/{data.get('slug', 'unknown')}.jpg"),
            "voice_note": data.get("voice_note", f"audio/{data.get('slug', 'unknown')}.m4a"),
            "status": data.get("status", DEFAULT_FIELDS["status"]),
            "collection": data.get("collection", DEFAULT_FIELDS["collection"]),
            "created": data.get("created", today_str),
            "last_updated": today_str,
            "contributor": data.get("contributor", DEFAULT_FIELDS["contributor"]),
            "related_recipes": data.get("related_recipes", DEFAULT_FIELDS["related_recipes"]),
        }

        # Log missing fields
        for key in DEFAULT_FIELDS:
            if key not in data:
                logs.append(f"⚠️ {recipe_file.name} missing field: {key}")

        index.append(entry)

    # Sort
    index.sort(key=lambda x: x["title"].lower())

    # Write YAML
    with open(index_yaml_file, "w") as f:
        yaml.dump(index, f, sort_keys=False)

    # Write CSV
    with open(index_csv_file, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=index[0].keys())
        writer.writeheader()
        writer.writerows(index)

    # Write Log
    with open(index_log_file, "w") as f:
        f.write("\n".join(logs))

    # Write Markdown
    with open(index_md_file, "w") as f:
        f.write("# 📘 Recipe Index\n\n")
        f.write(f"Last updated: `{today_str}`\n\n")
        f.write("| Title | Slug | Category | Cuisine | Status | Tags |\n")
        f.write("|-------|------|----------|---------|--------|------|\n")
        for item in index:
            f.write(f"| {item['title']} | `{item['slug']}` | {item['category']} | {item['cuisine']} | {item['status']} | {', '.join(item['tags'])} |\n")

    print(f"✅ YAML index written to {index_yaml_file}")
    print(f"📄 CSV written to {index_csv_file}")
    print(f"📝 Log written to {index_log_file}")
    print(f"📘 Markdown index written to {index_md_file}")

if __name__ == "__main__":
    generate_index()
