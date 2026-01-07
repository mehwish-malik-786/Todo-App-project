// frontend/lib/auth.ts
import { createAuthClient } from 'better-auth/react';
import { API_BASE_URL } from './api';

export const authClient = createAuthClient({
  baseURL: API_BASE_URL,
  // We'll configure this to work with our backend auth endpoints
  // For now, we'll use a placeholder configuration
});