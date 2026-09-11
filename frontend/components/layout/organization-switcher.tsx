"use client";
import { Organization } from "@/lib/api/client";
export function OrganizationSwitcher({ organization }: { organization: Organization }) { return <button className="flex items-center gap-2 rounded-md border bg-white px-3 py-2 text-sm font-medium" aria-label="Current organization"><span aria-hidden>⌂</span>{organization.name}<span className="text-slate-400">⌄</span></button>; }
