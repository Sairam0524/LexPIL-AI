# LexPIL AI - Complete Website & Interface Guide

## Website Architecture

### Frontend Structure

```
frontend/
├── src/
│   ├── pages/
│   │   ├── Chat.tsx           # Main conversational interface
│   │   ├── Analysis.tsx        # Case analysis form
│   │   ├── Corpus.tsx          # Corpus management
│   │   ├── News.tsx            # News feed
│   │   └── Admin.tsx           # Admin panel
│   ├── components/
│   │   ├── Layout.tsx          # Main navigation
│   │   ├── ChatMessage.tsx     # Message display
│   │   └── SourceCitations.tsx # Citation display
│   ├── hooks/
│   │   ├── useChat.ts          # Chat API hook
│   │   └── useAnalyze.ts       # Analysis API hook
│   ├── App.tsx                 # Main app component
│   ├── main.tsx                # Entry point
│   └── index.css               # Global styles
├── index.html                  # HTML template
├── vite.config.ts              # Vite configuration
├── tailwind.config.js          # Tailwind CSS config
├── tsconfig.json               # TypeScript config
└── package.json                # Dependencies
```

### Pages Overview

#### 1. Chat Page (http://localhost:3000/)
- **Purpose**: Conversational legal research interface
- **Features**:
  - Message input and display
  - Real-time responses
  - Source citations
  - Conversation history
  - Auto-scroll to latest message
- **User Interaction**: Type legal questions → Get analyzed responses with authorities

#### 2. Analysis Page (http://localhost:3000/analyze)
- **Purpose**: Structured case analysis
- **Form Fields**:
  - Party 1 and Party 1 Jurisdiction
  - Party 2 and Party 2 Jurisdiction
  - Dispute Subject (Contract, Tort, Property, etc.)
  - Detailed Facts (text area)
- **Output**: Complete analysis from all 10 agents

#### 3. Corpus Page (http://localhost:3000/corpus)
- **Purpose**: View legal database statistics
- **Displays**:
  - Total cases
  - Total statutes
  - Total treaties
  - Last update timestamp

#### 4. News Page (http://localhost:3000/news)
- **Purpose**: Monitor legal developments
- **Features**:
  - News feed
  - Jurisdiction filtering
  - PIL impact indicators
  - Date filters

#### 5. Admin Panel (http://localhost:3000/admin)
- **Purpose**: System management (Admin role only)
- **Controls**:
  - Reindex Corpus button
  - Rebuild Graph button
  - System statistics
  - User management (TODO)

### Navigation
- **Sidebar Navigation**: Dark sidebar with menu items
- **Active Page Highlighting**: Current page is highlighted
- **Responsive Design**: Works on desktop and tablet

---

## Styling with TailwindCSS

### Color Scheme
- **Primary**: Blue-600 (#2563eb)
- **Background**: Gray-50 (#f9fafb)
- **Cards**: White with shadow
- **Text**: Gray-900 for headings, Gray-600 for body

### Key Component Styles

#### Buttons
```tsx
className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
```

#### Form Inputs
```tsx
className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
```

#### Cards
```tsx
className="bg-white rounded-lg shadow p-6"
```

#### Citations Box
```tsx
className="bg-blue-50 border border-blue-200 rounded-lg p-4"
```

---

## API Integration

### useChat Hook
```typescript
const { chat } = useChat()
const response = await chat("Your question")
// Returns: { response, cited_authorities, analysis_type }
```

### useAnalyze Hook
```typescript
const { analyze } = useAnalyze()
const result = await analyze({
  party1: "Company A",
  party2: "Company B",
  // ... other fields
})
// Returns complete analysis with all agents' output
```

---

## User Interface Flows

### Chat Flow
1. User opens Chat page
2. Enters legal question
3. System displays thinking indicator
4. AI agent responds with analysis
5. Source citations appear below response
6. User can continue conversation
7. Full history is maintained

### Analysis Flow
1. User navigates to Analysis page
2. Fills in case details form
3. Clicks "Analyze Case" button
4. Loading spinner appears
5. Results display in right panel
6. User can copy/download results
7. Can modify form and re-analyze

### Admin Flow
1. Admin logs in (TODO: auth)
2. Navigates to Admin panel
3. Views system statistics
4. Can trigger reindex or rebuild
5. Receives completion notifications
6. Can manage users (TODO)

---

## Responsive Design

### Desktop (1024px+)
- Sidebar navigation
- Multi-column layouts
- Full content display

### Tablet (768px - 1023px)
- Collapsible sidebar
- Adjusted column layouts
- Touch-friendly buttons

### Mobile (< 768px)
- Full-width layout
- Hamburger menu (TODO)
- Single column
- Large touch targets

---

## Performance Features

- **Code Splitting**: React Router for page-level splitting
- **Lazy Loading**: Components load on demand
- **Caching**: Axios instance with cache strategy
- **Debouncing**: Search inputs (TODO)
- **Memoization**: useMemo for expensive calculations

---

## Accessibility

- **Semantic HTML**: Proper heading hierarchy
- **ARIA Labels**: For screen readers
- **Keyboard Navigation**: Full keyboard support
- **Color Contrast**: WCAG AA compliant
- **Focus Management**: Visible focus indicators

---

## State Management

### Currently Using
- React hooks (useState, useEffect, useRef)
- Component-level state
- Custom hooks for API calls

### Recommended for Scaling
- Zustand for global state (lighter than Redux)
- React Query for server state
- Context API for theme/auth

---

## Future UI Enhancements

- [ ] Dark mode toggle
- [ ] Knowledge graph visualization
- [ ] Jurisdiction map visualization
- [ ] Citation network graph
- [ ] PDF report generation
- [ ] Email notifications
- [ ] User profile management
- [ ] Search history
- [ ] Bookmarked authorities
- [ ] Collaborative notes

---

## Testing the Website

### Manual Testing Checklist
- [ ] Chat messages send and receive
- [ ] Case analysis processes correctly
- [ ] Corpus stats display
- [ ] News feed loads
- [ ] Admin buttons trigger actions
- [ ] Responsive on mobile
- [ ] Navigation works on all pages
- [ ] Error messages display properly
- [ ] Loading states show
- [ ] Keyboard navigation works

### Browser Compatibility
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## Deployment

### Frontend Deployment Options

1. **Vercel** (Recommended for React)
   ```bash
   npm i -g vercel
   vercel
   ```

2. **Netlify**
   ```bash
   npm run build
   netlify deploy --prod --dir=dist
   ```

3. **AWS S3 + CloudFront**
   ```bash
   npm run build
   aws s3 sync dist/ s3://your-bucket/
   ```

4. **Docker**
   ```bash
   docker build -t lexpil-frontend .
   docker run -p 3000:3000 lexpil-frontend
   ```

---

For detailed component implementation, see the actual React files in the `frontend/src/` directory.
