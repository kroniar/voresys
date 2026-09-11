const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api/v1";
export type Organization = { id: number; name: string; slug: string; role: string };
export async function api<T>(path: string, options: RequestInit = {}, organizationId?: number): Promise<T> {
  const token = typeof window !== "undefined" ? localStorage.getItem("verosys_access_token") : null;
  const headers = new Headers(options.headers);
  headers.set("Content-Type", "application/json");
  if (token) headers.set("Authorization", `Bearer ${token}`);
  if (organizationId) headers.set("X-Organization-ID", String(organizationId));
  const response = await fetch(`${API_URL}${path}`, { ...options, headers });
  if (!response.ok) throw new Error((await response.json().catch(() => ({}))).detail ?? "Request failed");
  return response.json() as Promise<T>;
}
