import os
import yaml

RECIPE_DIR = "recipes"
FIELDS_TO_RENDER = ["title", "ingredients", "instructions", "notes"]

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
        for item in recipe["ingredients"]:
            lines.append(f"- {item}")

    if "instructions" in recipe:
        lines.append("\n## Instructions")
        for idx, step in enumerate(recipe["instructions"], 1):
            lines.append(f"{idx}. {step}")

    if "notes" in recipe:
        lines.append("\n## Notes")
        for note in recipe["notes"]:
            lines.append(f"- {note}")

    return "\n".join(lines)

def write_markdown_file(yaml_filename, markdown_content):
    base_name = os.path.splitext(yaml_filename)[0]
    md_path = os.path.join(RECIPE_DIR, f"{base_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"✅ Rendered {md_path}")

def main():
    for filename in os.listdir(RECIPE_DIR):
        if filename.endswith(".yaml"):
            path = os.path.join(RECIPE_DIR, filename)
            recipe = load_yaml_file(path)
            if recipe:
                markdown = render_markdown(recipe)
                write_markdown_file(filename, markdown)

if __name__ == "__main__":
    main()
