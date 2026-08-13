---
name: AgenciArena
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#defcff'
  on-tertiary: '#00363a'
  tertiary-container: '#00f1ff'
  on-tertiary-container: '#006a70'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#79f5ff'
  tertiary-fixed-dim: '#00dbe8'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 72px
    fontWeight: '800'
    lineHeight: 80px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style
The design system is built for a creative powerhouse that balances Chilean grit with international refinement. The brand personality is authoritative, bold, and high-impact, driven by the philosophy "Creativity from simplicity."

The visual style is a blend of **Minimalism** and **High-Contrast Modernism**. It leverages expansive dark space to allow vibrant accents to pop, creating a premium "gallery" feel. The interface should feel heavy and grounded, avoiding unnecessary flourishes in favor of structural integrity and clarity. The emotional response is one of confidence and professional excellence.

## Colors
This design system utilizes a high-contrast dark mode palette. 

- **Primary:** Vibrant Yellow (#FFD700) is used exclusively for calls to action, active states, and critical brand highlights. It represents the "Arena" (sand) and energy.
- **Background:** The absolute base is a deep charcoal (#121212) to ensure maximum contrast for the yellow accents and white typography.
- **Surface Tiers:** Use a slightly lighter gray (#1E1E1E) for cards and containers to create subtle depth without breaking the dark aesthetic.
- **Typography:** Use pure white (#FFFFFF) for headlines to maintain authority. Scale down to medium and low-contrast grays for secondary information to establish a clear information hierarchy.

## Typography
The typography is the primary driver of the "Impact and Authority" requirement. 

- **Headlines:** Use **Montserrat** with heavy weights (700-800). Keep letter spacing tight on large displays to create a blocky, architectural feel.
- **Body:** Use **Hanken Grotesk** for its contemporary, clean, and highly legible qualities. It provides a sharp contrast to the aggressive headlines.
- **Labels:** Small labels and overlines should use Hanken Grotesk in uppercase with increased letter spacing to provide a sophisticated, technical touch to the layout.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy on desktop to maintain a premium, editorial look, while transitioning to a fluid model on mobile.

- **Desktop:** 12-column grid with a 1280px max-width. Large outer margins (64px) are used to breathe air into the "Simple" philosophy.
- **Mobile:** 4-column grid with 20px margins.
- **Rhythm:** All spacing (padding, margins, gaps) must be multiples of the 8px base unit. Use generous vertical padding (80px - 120px) between sections to emphasize the minimalist aesthetic and separate creative concepts effectively.

## Elevation & Depth
In this dark-themed system, depth is achieved through **Tonal Layers** and extremely **Ambient Shadows**.

- **Layers:** Objects closer to the user are rendered in lighter shades of gray (Surface #1E1E1E).
- **Shadows:** Avoid harsh black shadows. Use soft, diffused shadows with a large blur radius (20px-40px) and low opacity (0.4) to create a subtle lift.
- **Interactions:** Hover states on interactive cards should see a slight elevation increase and a subtle border highlight in the primary yellow color to signal focus.

## Shapes
To maintain a "Premium and Professional" look, the shape language is strictly **Soft (0.25rem)**.

Avoid fully rounded or pill-shaped buttons as they lean too casual. The subtle rounding on corners removes the "harshness" of pure brutalism while keeping the structural authority of the layout intact. Large containers and hero images should follow this same corner radius for consistency.

## Components
- **Buttons:** Primary buttons use a solid #FFD700 background with black text. Secondary buttons use a transparent background with a 1px white or yellow border. Transitions should be fast (200ms) and linear.
- **Cards:** Surface color #1E1E1E. Use 24px internal padding. Content should be left-aligned to maintain the professional, structured feel.
- **Inputs:** Darker background than the surface (#121212) with a subtle 1px border. The border should turn Primary Yellow on focus.
- **Chips:** Small, rectangular tags with low-contrast gray backgrounds and bold white text for categorization without distracting from the main CTA.
- **Lists:** Use simple dividers (1px, #2A2A2A) and generous vertical spacing between items.
- **Navigation:** Minimalist top bar with a glassmorphism effect (backdrop-blur: 10px) to allow content to scroll underneath while maintaining legibility.