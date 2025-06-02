from pathlib import Path
import yaml
import datetime

# Set the path to the recipes directory and the output index file
recipes_dir = Path("recipes")
index_file = Path("recipe_index.yaml")

# Default values for missing fields
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
    "related_recipes": [],
    "template_variant": "",
    "display_order": None,
    "layout_hints": [],
    "style_class": ""
}

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception:
        return {}

def generate_index():
    index = []
    today_str = datetime.date.today().isoformat()

    for recipe_file in recipes_dir.glob("*.yaml"):
        data = load_yaml(recipe_file)
        if not data or 'slug' not in data:
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
            "template_variant": data.get("template_variant", DEFAULT_FIELDS["template_variant"]),
            "display_order": data.get("display_order", DEFAULT_FIELDS["display_order"]),
            "layout_hints": data.get("layout_hints", DEFAULT_FIELDS["layout_hints"]),
            "style_class": data.get("style_class", DEFAULT_FIELDS["style_class"]),
        }
        index.append(entry)

    with open(index_file, "w") as f:
        yaml.dump(index, f, sort_keys=False)

    print(f"✅ Index updated with {len(index)} recipes.")

if __name__ == "__main__":
    generate_index()