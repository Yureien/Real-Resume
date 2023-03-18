import { default as adapterCloudflare } from '@sveltejs/adapter-cloudflare';
import { default as adapterStatic } from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/kit/vite';

const adapter = process.env.USE_CLOUDFLARE
	? adapterCloudflare({
			routes: {
				include: ['/*'],
				exclude: ['<all>']
			}
	  })
	: adapterStatic({
			pages: 'build',
			strict: true
	  });

if (!process.env.USE_CLOUDFLARE) console.log('Building static site');
else console.log('Building for Cloudflare Pages');

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),
	kit: {
		adapter
	}
};

export default config;
