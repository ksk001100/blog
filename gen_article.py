import sys
import datetime

args = sys.argv[1:]

now = datetime.datetime.now()
title = ''.join(args)

template = """+++
title = "{}"
date = {}

[taxonomies]
tags = []
+++

<!-- more -->

{{{{ image(src="/images/", alt="Dummy") }}}}
"""

with open(f"content/{now.strftime('%Y%m%d.md')}", 'w+') as f:
    f.write(template.format(title, now.strftime('%Y-%m-%d')))
