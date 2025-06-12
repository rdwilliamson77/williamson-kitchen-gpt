import os
import yaml

SOURCE_DIR = "recipes"
OUTPUT_DIR = "_recipes_rendered"
INDEX_FILE = "index.md"

# Make sure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_yaml_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"⚠️ Skipping {path}: {e}")
        return None

def render_markdown(recipe):
    lines = []
    if "title" in recipe:
        lines.append(f"# {recipe['title']}")
    else:
        lines.append("# Untitled Recipe")

    if "ingredients" in recipe:
        lines.append("\n## Ingredients")
        for item in recipe.get("ingredients", []):
            lines.append(f"- {item}")

    if "instructions" in recipe:
        lines.append("\n## Instructions")
        for idx, step in enumerate(recipe.get("instructions", []), 1):
            lines.append(f"{idx}. {step}")

    if "notes" in recipe:
        lines.append("\n## Notes")
        for note in recipe.get("notes", []):
            lines.append(f"- {note}")

    return "\n".join(lines)

def write_markdown_file(slug, content):
    path = os.path.join(OUTPUT_DIR, f"{slug}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Rendered: {path}")

def build_index(pages):
    lines = ["# 🍴 Family Recipes\n"]
    for slug, title in sorted(pages):
        lines.append(f"- [{title}](_recipes_rendered/{slug})")
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"📚 Updated index: {INDEX_FILE}")

def main():
    pages = []
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".yaml"):
            slug = os.path.splitext(filename)[0]
            path = os.path.join(SOURCE_DIR, filename)
            recipe = load_yaml_file(path)
            if recipe:
                markdown = render_markdown(recipe)
                write_markdown_file(slug, markdown)
                title = recipe.get("title", slug.replace("-", " ").title())
                pages.append((slug, title))

    build_index(pages)

if __name__ == "__main__":
    main()
