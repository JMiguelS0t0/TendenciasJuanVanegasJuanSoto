/** @type {import('tailwindcss').Config} */
import { screens as _screens } from 'tailwindcss/defaultTheme'
export const content = ['./src/**/*.{js,jsx,ts,tsx}']
export const theme = {
  screens: {
    xs: '475px',
    ..._screens
  },
  extend: {
    height: {
      100: '30rem'
    },
    colors: {
      main: '#183253',
      subMain: '#07b8db',
      text: '#f2f9fa',
      border: '#e8edee',
      textGray: '#A0A0A0',
      dry: '#f8fafa',
      greyed: '#f3f6f7'
    }
  }
}
export const plugins = []
