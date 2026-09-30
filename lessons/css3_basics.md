# CSS3 Basics

## What is CSS3?
CSS3 is the most recent version of Cascading Style Sheets. It controls layout, colors, typography, spacing, animations, and responsiveness.

## Key features
### 1. Selectors
CSS can target elements and groups of elements:
```css
p {
  color: #333;
}

.card {
  background-color: #f5f5f5;
}
```

### 2. Colors and backgrounds
Use named colors, hex values, RGB, HSL, and gradients:
```css
body {
  background: linear-gradient(to bottom, #ffffff, #eaeaea);
}
```

### 3. Borders, shadows, and radii
```css
.card {
  border: 1px solid #ddd;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
```

### 4. Typography
CSS can adjust fonts, line heights, spacing, and text styling:
```css
h1 {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 0.04em;
}
```

## Example
```css
body {
  font-family: Arial, sans-serif;
  background: #f4f4f4;
  color: #222;
}

button {
  background: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 10px 16px;
  cursor: pointer;
}
```

## Practice
Create a button that changes color when hovered.

```css
button:hover {
  background: #0056b3;
}
```

## Quick question
Which CSS property creates rounded corners?

Answer: `border-radius`
