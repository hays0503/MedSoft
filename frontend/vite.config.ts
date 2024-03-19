import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import scss from 'scss'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // root: resolve(__dirname, 'src'),
  resolve: {
    alias: {
      '@components': resolve('./src/components'),
      '@utils': resolve('./src/utils'),
      '@pages': resolve('./src/pages'),
      '@assets': resolve('./src/assets'),
      '@img': resolve('./public'),
      '@utility': resolve('./src/utility'),
    }
  },
  // build: {
  //   outDir: '../dist'
  // },
  // server: {
  //   port: 8080
  // },
  css: {
    preprocessorOptions: {
      scss: {
        implementation: scss,
      },
    },
  },
  test: {
    environment: 'jsdom',
    globals: true    
  }
})