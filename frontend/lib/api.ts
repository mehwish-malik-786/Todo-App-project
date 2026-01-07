// frontend/lib/api.ts
// API client with authentication support
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

class ApiClient {
  async request(endpoint: string, options: RequestInit = {}) {
    // Get the JWT token from localStorage or cookies
    const token = localStorage.getItem('auth_token');

    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
      ...options.headers,
    };

    // Add authorization header if token exists
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers,
      });

      if (response.status === 401) {
        // Handle unauthorized access
        console.error('Unauthorized access - redirect to login');
        // Remove invalid token
        localStorage.removeItem('auth_token');
        // In a real app, redirect to login page
        // window.location.href = '/login';
        throw new Error('Unauthorized');
      }

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  // Task-related API methods
  async getTasks(status?: 'all' | 'active' | 'completed', sort?: string) {
    let url = '/api/tasks';
    const params = new URLSearchParams();

    if (status) params.append('status', status);
    if (sort) params.append('sort', sort);

    if (params.toString()) {
      url += `?${params.toString()}`;
    }

    return this.request(url);
  }

  async createTask(taskData: Omit<Task, 'id' | 'user_id' | 'completed' | 'created_at' | 'updated_at'>) {
    return this.request('/api/tasks', {
      method: 'POST',
      body: JSON.stringify(taskData),
    });
  }

  async updateTask(id: string, taskData: Partial<Omit<Task, 'id' | 'user_id' | 'created_at' | 'updated_at'>>) {
    return this.request(`/api/tasks/${id}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  }

  async deleteTask(id: string) {
    return this.request(`/api/tasks/${id}`, {
      method: 'DELETE',
    });
  }

  async toggleTaskCompletion(id: string) {
    return this.request(`/api/tasks/${id}/complete`, {
      method: 'PATCH',
    });
  }

  // Authentication methods
  async register(email: string, name: string, password: string) {
    return this.request('/api/register', {
      method: 'POST',
      body: JSON.stringify({ email, name, password }),
    });
  }

  async login(email: string, password: string) {
    const response = await this.request('/api/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });

    // Store the token in localStorage
    if (response && response.access_token) {
      localStorage.setItem('auth_token', response.access_token);
    }

    return response;
  }

  async logout() {
    // Remove the token from localStorage
    localStorage.removeItem('auth_token');

    // Call the backend logout endpoint
    return this.request('/api/logout', {
      method: 'POST',
    });
  }

  // Check if user is authenticated
  isAuthenticated() {
    const token = localStorage.getItem('auth_token');
    return !!token;
  }
}

export const apiClient = new ApiClient();

export type { Task };