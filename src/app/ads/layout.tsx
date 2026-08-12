import Link from "next/link";

const mainNav = [
  { label: "Dashboard", href: "/ads/dashboard", icon: "dashboard" },
  { label: "Campaigns", href: "/ads/campaigns", icon: "campaign" },
  { label: "Audiences", href: "/ads/audiences", icon: "audience" },
  { label: "Creatives", href: "/ads/creatives", icon: "creative" },
  { label: "Inventory", href: "/ads/inventory", icon: "inventory" },
  { label: "Catalog", href: "/ads/catalog", icon: "catalog" },
];

const analyticsNav = [
  { label: "Analytics", href: "/ads/analytics", icon: "reporting" },
  { label: "Reports", href: "/ads/analytics/reports", icon: "reports" },
  { label: "Audience Insights", href: "/ads/analytics/audience", icon: "audience-insights" },
];

const toolsNav = [
  { label: "Lead Center", href: "/ads/leads", icon: "leads" },
  { label: "Exchange", href: "/ads/exchange", icon: "exchange" },
  { label: "AI Skills", href: "/ads/ai/skills", icon: "ai" },
  { label: "Events", href: "/ads/events", icon: "events" },
  { label: "Agency", href: "/ads/agency", icon: "agency" },
];

const settingsNav = [
  { label: "Account", href: "/ads/account", icon: "account" },
  { label: "Billing", href: "/ads/billing", icon: "billing" },
  { label: "Team", href: "/ads/account/team", icon: "team" },
  { label: "Settings", href: "/ads/settings", icon: "settings" },
  { label: "Notifications", href: "/ads/account/notifications", icon: "notifications" },
];

export default function AdsLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen bg-white text-neutral-900">
      <aside className="flex w-60 shrink-0 flex-col border-r border-neutral-100 bg-white">
        <div className="flex h-14 items-center gap-2 border-b border-neutral-100 px-5">
          <img src="/musicosy-orange-logo.webp" alt="Musicosy" className="h-6 w-auto object-contain" />
          <span className="text-xs font-medium text-neutral-400">Ads</span>
        </div>
        <nav className="flex-1 overflow-y-auto px-3 py-3">
          <NavSection label="Main" items={mainNav} />
          <NavSection label="Analytics" items={analyticsNav} />
          <NavSection label="Tools" items={toolsNav} />
          <NavSection label="Settings" items={settingsNav} />
        </nav>
        <div className="border-t border-neutral-100 px-4 py-3">
          <div className="flex items-center gap-3">
            <div className="flex h-8 w-8 items-center justify-center rounded-full bg-neutral-200 text-xs font-semibold text-neutral-600">A</div>
            <div className="min-w-0 flex-1">
              <p className="truncate text-sm font-medium text-neutral-900">Advertiser</p>
              <p className="truncate text-xs text-neutral-400">Personal account</p>
            </div>
          </div>
        </div>
      </aside>
      <div className="flex flex-1 flex-col overflow-hidden">
        <header className="flex h-14 shrink-0 items-center justify-between border-b border-neutral-100 bg-white px-6">
          <div className="flex items-center gap-1 text-sm text-neutral-500">
            <Link href="/ads" className="text-neutral-400 hover:text-neutral-900">Ads</Link>
          </div>
          <div className="flex items-center gap-4">
            <Link href="/" className="text-xs text-neutral-400 transition-colors hover:text-neutral-600">Back to Musicosy</Link>
          </div>
        </header>
        <main className="flex-1 overflow-y-auto bg-neutral-50/50 p-6">{children}</main>
      </div>
    </div>
  );
}

function NavSection({ label, items }: { label: string; items: { label: string; href: string; icon: string }[] }) {
  return (
    <div className="mb-2">
      <p className="mb-2 px-2 text-[10px] font-semibold uppercase tracking-widest text-neutral-400">{label}</p>
      {items.map((item) => (
        <Link key={item.href} href={item.href} className="flex items-center gap-3 rounded-lg px-2 py-2 text-sm text-neutral-600 transition-colors hover:bg-neutral-50 hover:text-neutral-900">
          <Icon type={item.icon} />
          {item.label}
        </Link>
      ))}
    </div>
  );
}

function Icon({ type }: { type: string }) {
  const p: React.SVGProps<SVGSVGElement> = { width: 18, height: 18, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 1.5, strokeLinecap: "round", strokeLinejoin: "round" };
  switch (type) {
    case "dashboard": return <svg {...p}><rect x="3" y="3" width="7" height="7" rx="1" /><rect x="14" y="3" width="7" height="7" rx="1" /><rect x="3" y="14" width="7" height="7" rx="1" /><rect x="14" y="14" width="7" height="7" rx="1" /></svg>;
    case "campaign": return <svg {...p}><path d="M12 2L2 7l10 5 10-5-10-5z" /><path d="M2 17l10 5 10-5" /><path d="M2 12l10 5 10-5" /></svg>;
    case "audience": case "audience-insights": return <svg {...p}><circle cx="12" cy="12" r="10" /><path d="M12 6v6l4 2" /></svg>;
    case "creative": return <svg {...p}><path d="M12 3v18M3 12h18" /><circle cx="18" cy="6" r="3" /></svg>;
    case "inventory": return <svg {...p}><rect x="2" y="7" width="20" height="14" rx="2" /><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2" /></svg>;
    case "catalog": return <svg {...p}><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z" /><line x1="3" y1="6" x2="21" y2="6" /><path d="M16 10a4 4 0 0 1-8 0" /></svg>;
    case "reporting": case "reports": return <svg {...p}><path d="M3 3v18h18" /><path d="M7 16l4-4 4 4 5-5" /></svg>;
    case "leads": return <svg {...p}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>;
    case "exchange": return <svg {...p}><path d="M17 1l4 4-4 4" /><path d="M3 5h18" /><path d="M7 23l-4-4 4-4" /><path d="M21 19H3" /></svg>;
    case "ai": return <svg {...p}><path d="M12 2l2 7h7l-5.5 4 2 7L12 16l-5.5 4 2-7L3 9h7z" /></svg>;
    case "events": return <svg {...p}><rect x="3" y="4" width="18" height="18" rx="2" /><line x1="16" y1="2" x2="16" y2="6" /><line x1="8" y1="2" x2="8" y2="6" /><line x1="3" y1="10" x2="21" y2="10" /></svg>;
    case "agency": return <svg {...p}><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" /><polyline points="9 22 9 12 15 12 15 22" /></svg>;
    case "account": return <svg {...p}><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" /><circle cx="12" cy="7" r="4" /></svg>;
    case "billing": return <svg {...p}><rect x="1" y="4" width="22" height="16" rx="2" /><path d="M1 10h22" /></svg>;
    case "team": return <svg {...p}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>;
    case "settings": return <svg {...p}><circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" /></svg>;
    case "notifications": return <svg {...p}><path d="M18 8A6 6 0 1 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" /><path d="M13.73 21a2 2 0 0 1-3.46 0" /></svg>;
    default: return <svg {...p}><circle cx="12" cy="12" r="1" /></svg>;
  }
}
