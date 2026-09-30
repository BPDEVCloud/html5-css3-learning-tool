# Advanced Features

## Transforms
Transforms allow elements to rotate, scale, or move.

```css
.card:hover {
  transform: translateY(-5px) scale(1.02);
}
```

## Transitions
Transitions add smooth motion when a state changes.

```css
button {
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #0056b3;
  transform: scale(1.03);
}
```

## Animations
Animations can create motion without JavaScript.

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.hero {
  animation: fadeIn 1s ease-in;
}
```

## CSS Variables
CSS custom properties make styling easier to maintain.

```css
:root {
  --primary-color: #007bff;
  --padding: 16px;
}

button {
  background: var(--primary-color);
  padding: var(--padding);
}
```

## Best practices
- Use semantic HTML
- Keep CSS organized and readable
- Prefer responsive layouts
- Use variables for repeated values
- Test on different screen sizes

## Practice
Create a card that:
- has a shadow
- changes slightly on hover
- uses a transition
- loads with a fade-in animation

## Quick question
What CSS feature helps create smooth visual effects during state changes?

Answer: `transition`
