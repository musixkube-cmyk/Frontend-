import Link from "next/link";

const sidebarItems = [
  { label: "Dashboard", href: "/ads", icon: "dashboard" },
  { label: "Campaigns", href: "/ads/campaigns", icon: "campaign" },
  { label: "Creative Studio", href: "/ads/creative/studio", icon: "creative" },
  { label: "Creative Library", href: "/ads/creative/library", icon: "library" },
  { label: "Reporting", href: "/ads/analytics/reporting", icon: "reporting" },
  { label: "Audience Insights", href: "/ads/analytics/audience", icon: "audience" },
  { label: "Lead Center", href: "/ads/leads/dashboard", icon: "leads" },
  { label: "Catalog Manager", href: "/ads/catalog/onboarding", icon: "catalog" },
];

const toolItems = [
  { label: "Account Settings", href: "/ads/settings/account", icon: "settings" },
  { label: "Billing", href: "/ads/billing/payment", icon: "billing" },
  { label: "Team", href: "/ads/team/members", icon: "team" },
  { label: "Notifications", href: "/ads/notifications/center", icon: "notifications" },
];

export default function AdsLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen bg-white text-neutral-900">
      {/* Left sidebar */}
      <aside className="flex w-60 shrink-0 flex-col border-r border-neutral-100 bg-white">
        {/* Logo */}
        <div className="flex h-14 items-center gap-2 border-b border-neutral-100 px-5">
          <img
            src="/musicosy-orange-logo.webp"
            alt="Musicosy"
            className="h-6 w-auto object-contain"
          />
          <span className="text-xs font-medium text-neutral-400">Ads</span>
        </div>

        {/* Main nav */}
        <nav className="flex-1 overflow-y-auto px-3 py-3">
          <p className="mb-2 px-2 text-[10px] font-semibold uppercase tracking-widest text-neutral-400">
            Manage
          </p>
          {sidebarItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="flex items-center gap-3 rounded-lg px-2 py-2 text-sm text-neutral-600 transition-colors hover:bg-neutral-50 hover:text-neutral-900"
            >
              <SidebarIcon type={item.icon} />
              {item.label}
            </Link>
          ))}

          <p className="mb-2 mt-6 px-2 text-[10px] font-semibold uppercase tracking-widest text-neutral-400">
            Tools
          </p>
          {toolItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="flex items-center gap-3 rounded-lg px-2 py-2 text-sm text-neutral-600 transition-colors hover:bg-neutral-50 hover:text-neutral-900"
            >
              <SidebarIcon type={item.icon} />
              {item.label}
            </Link>
          ))}
        </nav>

        {/* User */}
        <div className="border-t border-neutral-100 px-4 py-3">
          <div className="flex items-center gap-3">
            <div className="flex h-8 w-8 items-center justify-center rounded-full bg-neutral-200 text-xs font-semibold text-neutral-600">
              A
            </div>
            <div className="min-w-0 flex-1">
              <p className="truncate text-sm font-medium text-neutral-900">Advertiser</p>
              <p className="truncate text-xs text-neutral-400">Personal account</p>
            </div>
          </div>
        </div>
      </aside>

      {/* Right: top bar + content */}
      <div className="flex flex-1 flex-col overflow-hidden">
        {/* Top bar */}
        <header className="flex h-14 shrink-0 items-center justify-between border-b border-neutral-100 bg-white px-6">
          <div className="flex items-center gap-1 text-sm text-neutral-500">
            <Link href="/ads" className="text-neutral-400 hover:text-neutral-900">Ads</Link>
          </div>
          <div className="flex items-center gap-4">
            <Link
              href="/"
              className="text-xs text-neutral-400 transition-colors hover:text-neutral-600"
            >
              Back to Musicosy
            </Link>
          </div>
        </header>

        {/* Page content */}
        <main className="flex-1 overflow-y-auto bg-neutral-50/50 p-6">
          {children}
        </main>
      </div>
    </div>
  );
}

function SidebarIcon({ type }: { type: string }) {
  const size = 18;
  const props = { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 1.5, strokeLinecap: "round" as const, strokeLinejoin: "round" as const };

  switch (type) {
    case "dashboard":
      return <svg {...props}><rect x="3" y="3" width="7" height="7" rx="1" /><rect x="14" y="3" width="7" height="7" rx="1" /><rect x="3" y="14" width="7" height="7" rx="1" /><rect x="14" y="14" width="7" height="7" rx="1" /></svg>;
    case "campaign":
      return <svg {...props}><path d="M12 2L2 7l10 5 10-5-10-5z" /><path d="M2 17l10 5 10-5" /><path d="M2 12l10 5 10-5" /></svg>;
    case "creative":
      return <svg {...props}><path d="M12 3v18M3 12h18" /><circle cx="18" cy="6" r="3" /></svg>;
    case "library":
      return <svg {...props}><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" /><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" /></svg>;
    case "reporting":
      return <svg {...props}><path d="M3 3v18h18" /><path d="M7 16l4-4 4 4 5-5" /></svg>;
    case "audience":
      return <svg {...props}><circle cx="12" cy="12" r="10" /><path d="M12 6v6l4 2" /></svg>;
    case "leads":
      return <svg {...props}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>;
    case "catalog":
      return <svg {...props}><rect x="2" y="7" width="20" height="14" rx="2" /><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2" /></svg>;
    case "settings":
      return <svg {...props}><circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" /></svg>;
    case "billing":
      return <svg {...props}><rect x="1" y="4" width="22" height="16" rx="2" /><path d="M1 10h22" /></svg>;
    case "team":
      return <svg {...props}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>;
    case "notifications":
      return <svg {...props}><path d="M18 8A6 6 0 1 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" /><path d="M13.73 21a2 2 0 0 1-3.46 0" /></svg>;
    default:
      return <svg {...props}><circle cx="12" cy="12" r="1" /></svg>;
  }
}
