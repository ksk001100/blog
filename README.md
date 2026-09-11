# blog
My tech blog (https://ksk.works) built with [Astro](https://astro.build/).

## Requirements
- Node.js (v20+ recommended)
- npm (or pnpm / yarn)

## Develop
```bash
$ git clone https://github.com/ksk001100/blog
$ cd blog
$ npm install
$ npm run dev
```

Local development server starts at `http://localhost:4321`.

## Create a new article
```bash
$ python gen_article.py <title>
```
This generates:
- Markdown template: `src/content/blog/YYYYMMDD.md`
- Image directory: `public/images/YYYYMMDD/`

## Build
```bash
$ npm run build
```
Production static output is generated in `dist/`.

## Preview production build
```bash
$ npm run preview
```
