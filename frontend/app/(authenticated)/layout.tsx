"use client";
import { useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { api, Organization } from "@/lib/api/client";
import { OrganizationSwitcher } from "@/components/layout/organization-switcher";
import { Sidebar } from "@/components/layout/sidebar";
export default function AuthenticatedLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [organization, setOrganization] = useState<Organization>();
  useEffect(() => {
    if (!localStorage.getItem("verosys_access_token")) {
      router.replace("/login");
      return;
    }
    api<Organization[]>("/organizations/")
      .then((items) => {
        if (!items.length) throw new Error("No organization membership");
        setOrganization(items[0]);
      })
      .catch(() => router.replace("/login"));
  }, [router]);
  if (!organization) return <main className="p-8 text-sm text-slate-500">Loading Verosys…</main>;
  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <div className="min-w-0 flex-1">
        <header className="flex h-16 items-center justify-between border-b bg-white px-5">
          <span className="text-sm text-slate-500 md:hidden">VEROSYS</span>
          <OrganizationSwitcher organization={organization} />
          <span className="text-sm text-slate-500">{organization.role}</span>
        </header>
        <main className="mx-auto max-w-5xl p-6 md:p-10" key={pathname}>
          {children}
        </main>
      </div>
    </div>
  );
}
