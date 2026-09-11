import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://ksk.works',
  integrations: [sitemap()],
  markdown: {
    shikiConfig: {
      theme: 'ayu-dark',
      wrap: true,
    },
  },
});
