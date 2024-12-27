import sys
import datetime
import os

args = sys.argv[1:]

now = datetime.datetime.now()
title = ''.join(args)
date_str = now.strftime('%Y%m%d')

os.mkdir(f"./static/images/{date_str}")

template = """+++
title = "{}"
date = {}

[taxonomies]
tags = []
+++

<!-- more -->

{{{{ image(src="/images/{}/dummy.jpg", alt="Dummy") }}}}
"""

with open(f"content/{date_str}.md", 'w+') as f:
    f.write(template.format(title, now.strftime('%Y-%m-%d'), date_str))
