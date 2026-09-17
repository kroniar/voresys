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
  const [mobileNavOpen, setMobileNavOpen] = useState(false);

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

  useEffect(() => setMobileNavOpen(false), [pathname]);

  useEffect(() => {
    document.body.style.overflow = mobileNavOpen ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [mobileNavOpen]);

  if (!organization) {
    return <main className="grid min-h-screen place-items-center bg-slate-50 p-6 text-sm text-slate-500">Loading Verosys…</main>;
  }

  return (
    <div className="flex min-h-screen bg-slate-50">
      <Sidebar mobileOpen={mobileNavOpen} onClose={() => setMobileNavOpen(false)} />
      <div className="min-w-0 flex-1">
        <header className="sticky top-0 z-30 flex h-16 items-center gap-3 border-b border-slate-200 bg-white/95 px-4 backdrop-blur sm:px-5">
          <button
            type="button"
            aria-label="Open navigation"
            aria-expanded={mobileNavOpen}
            className="rounded-lg p-2 text-slate-600 transition-colors hover:bg-slate-100 hover:text-slate-950 md:hidden"
            onClick={() => setMobileNavOpen(true)}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" className="h-5 w-5">
              <path d="M4 7h16M4 12h16M4 17h16" strokeLinecap="round" />
            </svg>
          </button>
          <span className="hidden text-sm font-semibold tracking-[0.16em] text-slate-950 md:block">VEROSYS</span>
          <div className="min-w-0 flex-1">
            <OrganizationSwitcher organization={organization} />
          </div>
          <span className="hidden rounded-full bg-slate-100 px-3 py-1 text-xs font-medium capitalize text-slate-600 sm:inline-flex">
            {organization.role}
          </span>
        </header>
        <main className="mx-auto w-full max-w-6xl px-4 py-6 sm:px-6 md:py-8 lg:px-8" key={pathname}>
          {children}
        </main>
      </div>
    </div>
  );
}
