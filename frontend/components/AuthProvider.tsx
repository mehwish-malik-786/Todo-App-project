// frontend/components/AuthProvider.tsx
'use client';

import { ReactNode } from 'react';

interface Props {
  children: ReactNode;
}

// Placeholder AuthProvider component
export function AuthProvider({ children }: Props) {
  return (
    <>{children}</>
  );
}

// Placeholder ProtectedRoute component
export function ProtectedRoute({ children }: Props) {
  return <>{children}</>;
}