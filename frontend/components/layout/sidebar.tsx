"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const sections = [
  ["", ["Overview", "/"]],
  ["OPERATIONS", ["Requests", "/requests"], ["Tasks", "/tasks"]],
  ["INFRASTRUCTURE", ["Environments", "/environments"], ["Repositories", "/repositories"]],
  ["AI", ["AI Tasks", "/ai-tasks"], ["Skills", "/skills"]],
  ["INTEGRATIONS", ["Connections", "/connections"]],
  ["SECURITY", ["Scans", "/scans"]],
] as const;

type SidebarProps = {
  mobileOpen?: boolean;
  onClose?: () => void;
};

function Navigation({ onNavigate }: { onNavigate?: () => void }) {
  const pathname = usePathname();

  return (
    <nav className="flex flex-1 flex-col">
      <div className="space-y-5">
        {sections.map(([label, ...items]) => (
          <div key={label || "main"}>
            {label && (
              <p className="mb-2 px-2 text-[10px] font-semibold uppercase tracking-[0.14em] text-slate-400">
                {label}
              </p>
            )}
            <div className="space-y-1">
              {items.map(([name, href]) => {
                const active = href === "/" ? pathname === href : pathname.startsWith(href);

                return (
                  <Link
                    className={`block rounded-lg px-3 py-2 text-sm font-medium transition-colors ${
                      active
                        ? "bg-slate-100 text-slate-950"
                        : "text-slate-600 hover:bg-slate-50 hover:text-slate-950"
                    }`}
                    key={href}
                    href={href}
                    onClick={onNavigate}
                  >
                    {name}
                  </Link>
                );
              })}
            </div>
          </div>
        ))}
      </div>

      <div className="mt-auto border-t pt-4">
        <Link
          className="block rounded-lg px-3 py-2 text-sm font-medium text-slate-600 transition-colors hover:bg-slate-50 hover:text-slate-950"
          href="/documentation"
          onClick={onNavigate}
        >
          Documentation
        </Link>
        <Link
          className="block rounded-lg px-3 py-2 text-sm font-medium text-slate-600 transition-colors hover:bg-slate-50 hover:text-slate-950"
          href="/settings"
          onClick={onNavigate}
        >
          Settings
        </Link>
      </div>
    </nav>
  );
}

function SidebarContent({ onClose, mobile = false }: { onClose?: () => void; mobile?: boolean }) {
  return (
    <div className="flex h-full flex-col">
      <div className="mb-8 flex items-center justify-between">
        <Link
          href="/"
          className="text-base font-semibold tracking-[0.18em] text-slate-950"
          onClick={onClose}
        >
          VEROSYS
        </Link>
        {mobile && (
          <button
            type="button"
            aria-label="Close navigation"
            className="rounded-lg p-2 text-slate-500 transition-colors hover:bg-slate-100 hover:text-slate-900"
            onClick={onClose}
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" className="h-5 w-5">
              <path d="M6 6l12 12M18 6L6 18" strokeLinecap="round" />
            </svg>
          </button>
        )}
      </div>
      <Navigation onNavigate={onClose} />
    </div>
  );
}

export function Sidebar({ mobileOpen = false, onClose }: SidebarProps) {
  return (
    <>
      <aside className="hidden w-64 shrink-0 border-r border-slate-200 bg-white p-5 md:flex md:flex-col">
        <SidebarContent />
      </aside>

      <div
        className={`fixed inset-0 z-50 md:hidden ${mobileOpen ? "pointer-events-auto" : "pointer-events-none"}`}
        aria-hidden={!mobileOpen}
      >
        <button
          type="button"
          aria-label="Close navigation"
          className={`absolute inset-0 bg-slate-950/25 transition-opacity ${mobileOpen ? "opacity-100" : "opacity-0"}`}
          onClick={onClose}
        />
        <aside
          className={`absolute inset-y-0 left-0 w-[min(19rem,88vw)] border-r border-slate-200 bg-white p-5 shadow-xl transition-transform duration-200 ease-out ${
            mobileOpen ? "translate-x-0" : "-translate-x-full"
          }`}
        >
          <SidebarContent mobile onClose={onClose} />
        </aside>
      </div>
    </>
  );
}
