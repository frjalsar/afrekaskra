import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  base: '/',
  plugins: [
    vue(),
  ],
  build: {
    assetsDir: 'assets',
    rollupOptions: { // Split node_modules into separate chunks
      output:{
          manualChunks(id) {
              if (id.includes('node_modules')) {
                  return id.toString().split('node_modules/')[1].split('/')[0].toString();
              }
          }
      }
  }
  },
  resolve: {
    alias: {
      //vue: '@vue/compat',
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
