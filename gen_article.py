import sys
import datetime
import os

args = sys.argv[1:]

now = datetime.datetime.now()
title = ' '.join(args) if args else 'New Article'
date_str = now.strftime('%Y%m%d')

img_dir = os.path.join("public", "images", date_str)
os.makedirs(img_dir, exist_ok=True)
with open(os.path.join(img_dir, ".keep"), "w") as f:
    pass

template = f"""---
title: "{title}"
date: {now.strftime('%Y-%m-%d')}
tags: []
---

<!-- more -->

![Dummy](/images/{date_str}/dummy.jpg)
"""

article_path = os.path.join("src", "content", "blog", f"{date_str}.md")
with open(article_path, "w", encoding="utf-8") as f:
    f.write(template)

print(f"Created article: {article_path}")
print(f"Created image directory: {img_dir}")
