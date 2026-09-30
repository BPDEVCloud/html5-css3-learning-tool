# Layouts and Responsiveness

## Why layout matters
Modern webpages must work on mobile phones, tablets, desktops, and large screens. CSS layout tools help manage flexible design.

## Flexbox
Flexbox is useful for arranging items in a row or column.

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}
```

## Grid
CSS Grid is ideal for multi-column layouts.

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
```

## Responsive design
Use media queries to change styles based on screen size:

```css
@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
```

## Example layout
```html
<div class="container">
  <div class="card">One</div>
  <div class="card">Two</div>
  <div class="card">Three</div>
</div>
```

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.card {
  flex: 1 1 220px;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}
```

## Practice
Create a responsive layout where cards stack on small screens and sit side by side on larger screens.

## Quick question
Which CSS feature is best for arranging items in a two-dimensional layout?

Answer: CSS Grid
