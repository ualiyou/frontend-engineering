import DefaultTheme from 'vitepress/theme';
import type { Theme } from 'vitepress';
import './custom.css';

// ponytail: default theme plus a stylesheet. No component overrides until a
// page actually needs one.
export default {
  extends: DefaultTheme,
} satisfies Theme;
