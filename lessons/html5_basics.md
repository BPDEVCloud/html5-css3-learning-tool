# HTML5 Basics

## What is HTML5?
HTML5 is the latest major version of the HyperText Markup Language. It adds powerful features for structure, media, forms, and interactivity.

## Key features
### 1. Semantic elements
These tags describe meaning, not just appearance:
- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<article>`
- `<aside>`
- `<footer>`

Semantic tags improve accessibility and SEO.

### 2. Media support
HTML5 makes it easy to embed media without third-party plugins:
```html
<video controls>
  <source src="movie.mp4" type="video/mp4">
</video>

<audio controls>
  <source src="song.mp3" type="audio/mpeg">
</audio>
```

### 3. Canvas and graphics
The `<canvas>` element allows drawing graphics using JavaScript.

### 4. Improved forms
New input types help with validation:
```html
<input type="email" required>
<input type="date">
<input type="tel">
<input type="range">
```

## Example
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>HTML5 Page</title>
  </head>
  <body>
    <header>
      <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
      </nav>
    </header>

    <main>
      <section>
        <h1>Welcome</h1>
        <article>
          <p>This page uses HTML5 semantic structure.</p>
        </article>
      </section>
    </main>
  </body>
</html>
```

## Practice
Try creating a page with:
- one header
- one navigation area
- one main section
- one article
- one footer

## Quick question
Which HTML5 element is best for a standalone content block, such as a blog post?

Answer: `<article>`
