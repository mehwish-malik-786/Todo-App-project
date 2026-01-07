// frontend/app/page.tsx
import { redirect } from 'next/navigation';

export default function Home() {
  // Redirect to the tasks page if authenticated, otherwise to login
  redirect('/tasks');
}