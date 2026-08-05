import DefaultTheme from 'vitepress/theme';
import type { Theme } from 'vitepress';
import { h } from 'vue';
import './custom.css';

// ponytail: one slot override, rendered with `h()` so the dedication needs no
// separate .vue file. `layout-top` is the slot the default theme already offsets
// every fixed element against (--vp-layout-top-height), so the bar costs no
// layout surgery. Add a component when it grows past a sentence.
export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'layout-top': () =>
        h('div', { class: 'dedication' }, [
          h('span', { class: 'dedication-mark' }, '❦'),
          'In memory of ',
          h(
            'a',
            {
              class: 'dedication-name',
              href: 'https://fa.wikipedia.org/wiki/%D8%B5%D8%A7%D8%A8%D8%B1_%D8%B1%D8%A7%D8%B3%D8%AA%DB%8C%E2%80%8C%DA%A9%D8%B1%D8%AF%D8%A7%D8%B1',
              target: '_blank',
              rel: 'noreferrer',
              title: 'صابر راستی‌کردار — ویکی‌پدیای فارسی',
            },
            'Saber Rastikerdar',
          ),
          h('span', { class: 'dedication-long' }, ' — creator of '),
          h('span', { class: 'dedication-short' }, ' · '),
          h(
            'a',
            {
              href: 'https://github.com/rastikerdar/vazirmatn',
              target: '_blank',
              rel: 'noreferrer',
            },
            'Vazirmatn',
          ),
          h(
            'span',
            { class: 'dedication-long' },
            ', the open typeface he gave the Persian web and asked nothing for.',
          ),
        ]),
    }),
} satisfies Theme;
