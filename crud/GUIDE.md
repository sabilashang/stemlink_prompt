Build a full-stack web application boilerplate called "AppName" (placeholder for users to rename) that allows users to securely create, view, edit, and delete personal items. The app should be modular, secure, and easily extensible. Include placeholders so users can modify app title, features, or content.

---

Backend:

- Use Supabase as the database and authentication provider.
- Implement user authentication (signup, login, logout) using Supabase Auth.
- Create a database table for the main content items (e.g., notes, tasks, posts), linked to each authenticated user.
- Include columns: 
  - id (primary key)
  - title (text)
  - description/content (text)
  - user_id (foreign key to users)
  - created_at, updated_at (timestamps)
- Secure database access so users can only read/write their own items.

Frontend:

- Include a modern, simple UI (React/Vue/Svelte) with routing:
  - Login / Signup page
  - Dashboard showing user’s items
  - Add new item form
  - Edit existing item form
  - Delete confirmation modal
- Use a placeholder "AppTitle" at top so users can change the title easily.
- Include placeholders for "Feature 1", "Feature 2", … so users can add or rename features easily.
- Connect frontend securely to Supabase backend using environment variables.

Security:

- Ensure users only see and modify their own content.
- Use environment variables for Supabase keys.
- Include simple input validation on frontend and backend.

Instructions / Tasks for Generated Code:

1. Generate the Supabase table schema for users and main content items.
2. Set up Supabase Auth for signup/login/logout.
3. Generate API routes (REST or Supabase client functions) for CRUD operations.
4. Generate frontend pages/components for listing, adding, editing, and deleting items.
5. Connect frontend to Supabase securely with environment variables.
6. Include routing so login/signup redirects to dashboard.
7. Make UI simple, responsive, and visually appealing.
8. Include placeholder content sections where users can modify:
   - AppTitle
   - Feature 1, Feature 2, Feature 3 …
   - Example item titles and descriptions
9. Provide a README.md with instructions:
   - How to set environment variables
   - How to run the app locally
   - How to connect to Supabase

---

Output Requirements:

- Full codebase ready to run locally.
- Include environment variable placeholders.
- Clean, modular code with separate files for components, services, and utilities.
- Clear comments indicating where users can modify app name, features, or content.
- Secure and functional, ready for immediate testing.
- Provide all files structured in a `/crud` folder.
