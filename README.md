# Personal Portfolio Website

A modern, responsive portfolio website featuring a sleek dark theme and animated interactions.

## Features
- **Responsive Design**: Optimized for all device sizes with mobile-first approach
- **Modern Dark Theme**: Elegant noir color scheme with gradient backgrounds
- **Smooth Animations**: CSS animations with intersection observers for scroll-triggered effects
- **Interactive Elements**: Hover effects, button press animations, and smooth scrolling
- **Typography**: Custom font combinations (Inter, Space Grotesk) for modern aesthetics
- **Performance Optimized**: Efficient CSS with hardware acceleration and optimized animations

## Tech Stack

### Backend
- **Flask 3.0.0** - Python web framework
- **Jinja2** - Template engine for dynamic content
- **Werkzeug** - WSGI utility library

### Frontend
- **HTML5** - Semantic markup with accessibility features
- **CSS3** - Advanced styling with:
  - CSS Grid & Flexbox layouts
  - Custom animations and keyframes
  - CSS variables for theming
  - Backdrop filters and gradients
- **Tailwind CSS** - Utility-first CSS framework (CDN)
- **JavaScript (Vanilla)** - Interactive features:
  - Intersection Observer API for scroll animations
  - Smooth scrolling navigation
  - Mobile menu interactions
  - Dynamic content reveals

### Design & Assets
- **Font Awesome 6.0** - Icon library for social links and UI elements
- **Google Fonts** - Inter & Space Grotesk typography
- **Custom Graphics** - Favicon and profile images

### Deployment
- **Vercel** - Serverless deployment platform
- **Git** - Version control

## Project Structure
```
├── app.py              # Flask application entry point
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel deployment configuration
├── static/
│   ├── style.css      # Main stylesheet with animations
│   ├── site.webmanifest # PWA manifest
│   └── images/        # Static assets (favicon, profile images)
└── templates/
    └── about.html     # Main template with Tailwind integration
```

## Setup & Development
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd personalwebsite
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**
   ```bash
   python app.py
   ```
   The site will be available at `http://localhost:5000`

4. **For development**
   - Edit templates in `templates/` directory
   - Modify styles in `static/style.css`
   - Static assets go in `static/images/`

## Key Features Implementation
- **Responsive Grid Layouts**: CSS Grid for project showcases and skill categories
- **Scroll-triggered Animations**: Intersection Observer API for progressive content revelation
- **Custom CSS Animations**: Keyframe animations for skill boxes, text effects, and hover states
- **Mobile Navigation**: JavaScript-powered hamburger menu with staggered animations
- **Performance Optimizations**: Hardware-accelerated transforms and efficient selectors

## Browser Support
- Modern browsers with CSS Grid and Intersection Observer support
- Progressive enhancement for older browsers
- Mobile-optimized with touch-friendly interactions

## License
MIT
