# Copy the entire prompt in raw and make amendments such as removing this line, and modifying the template for name and app features to build your very own application in a single prompt

Build a full-stack web application called "{{AppName}}" where users can securely create, view, edit, and delete personal items. The app should be fully functional, modular, and ready to run locally. Include placeholders so users can easily customize app title, features, and item content.

---

# Backend:

- Use Supabase as the database and authentication provider.
- Implement user authentication (signup, login, logout) using Supabase Auth.
- Create a database table named `items` with columns:
  - id (primary key)
  - title (text)
  - description (text)
  - user_id (foreign key to users)
  - created_at, updated_at (timestamps)
- Ensure users can only access their own data.
- Include environment variable placeholders for Supabase keys.

# Frontend:

- Modern, responsive UI using React (or another modern framework).
- Routing:
  - `/login` → login page
  - `/signup` → signup page
  - `/dashboard` → user’s items
- Components:
  - Dashboard: lists user items
  - AddItemForm: form to add new item
  - EditItemForm: form to edit existing item
  - DeleteItemModal: confirm deletion
  - Header/Footer with `{{AppTitle}}` placeholder
- Include placeholders for "Feature 1", "Feature 2", "Feature 3" in the dashboard for users to customize.

# CRUD Functionality:

- List all user items on the dashboard.
- Add a new item (title + description).
- Edit an existing item.
- Delete an item with confirmation.
- Sync all CRUD operations securely with Supabase backend.

# Security:

- Users can only view and edit their own items.
- Validate input on frontend and backend.
- Use environment variables for Supabase project URL and API key.

# Instructions / Placeholders:

- AppName → Change the app name easily
- AppTitle → Change the main title visible on UI
- Features → "Feature 1", "Feature 2", "Feature 3" placeholders for users to rename or add more
- Example item → Add sample titles and descriptions

# Tasks Lovable Should Handle:

1. Generate Supabase schema for users and items.
2. Set up Supabase Auth for signup/login/logout.
3. Generate frontend components for listing, adding, editing, deleting items.
4. Connect frontend securely to Supabase backend.
5. Include routing between login/signup and dashboard.
6. Add placeholders for AppTitle, Features, and sample item content.
7. Provide README.md with instructions:
   - Set environment variables
   - Run the app locally
   - Connect to Supabase

# Output Requirements:

- Full working codebase ready to run locally.
- Modular folder structure with separate frontend, backend, components, and utils.
- Clear comments indicating where users can customize app name, features, or content.
- Secure, functional, visually simple but appealing UI.
- Include instructions for running locally, setting up Supabase, and environment variables.

# Optional Enhancements:

- Add responsive design for mobile.
- Include timestamps on dashboard items.
- Add sorting/filtering options for user items.
