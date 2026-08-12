"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState, useMemo } from "react";
import { ProfileDropdown, SidebarProfile } from "@/components/ads/profile-dropdown";
import { useCurrentUser } from "@/hooks/use-auth";

/* ─── Collapsible sidebar navigation tree — matches spec exactly ─── */
const navTree = [
  {
    label: "Dashboard",
    icon: "home",
    children: [
      { label: "Dashboard", href: "/ads/dashboard", icon: "dashboard" },
      { label: "GMV Max", href: "/ads/gmv-max", icon: "chart" },
    ],
  },
  {
    label: "Ads Manager",
    icon: "campaigns",
    children: [
      { label: "Campaigns", href: "/ads/ads-manager/campaigns", icon: "campaigns" },
      { label: "Ad Groups", href: "/ads/ads-manager/ad-groups", icon: "layers" },
      { label: "Ads", href: "/ads/ads-manager/ads", icon: "ad" },
      { label: "Monitoring", href: "/ads/ads-manager/monitor", icon: "chart" },
      { label: "Optimization", href: "/ads/ads-manager/optimize", icon: "zap" },
      { label: "Create Campaign", href: "/ads/ads-manager/campaigns/create", icon: "plus-circle", primary: true },
    ],
  },
  {
    label: "Management Tools",
    icon: "zap",
    children: [
      { label: "Placement & Inventory", href: "/ads/inventory", icon: "layout" },
      { label: "Catalog Manager", href: "/ads/catalog", icon: "catalog" },
      { label: "Events Manager", href: "/ads/events", icon: "calendar" },
      { label: "Automated Rules", href: "/ads/automated-rules", icon: "zap" },
      { label: "Comments Manager", href: "/ads/comments-manager", icon: "message-square" },
      { label: "MMM Data Request", href: "/ads/mmm-data-request", icon: "report" },
      { label: "Notification Center", href: "/ads/notifications", icon: "bell" },
    ],
  },
  {
    label: "Audiences",
    icon: "users",
    children: [
      { label: "Audience List", href: "/ads/audiences", icon: "users" },
      { label: "Create Audience", href: "/ads/audiences/create", icon: "plus-circle", primary: true },
      { label: "Demographic Targeting", href: "/ads/audiences/demographic", icon: "users" },
      { label: "Location Targeting", href: "/ads/audiences/location", icon: "target" },
      { label: "Music Behavior", href: "/ads/audiences/music-behavior", icon: "chart" },
      { label: "Artist Affinity", href: "/ads/audiences/artist-affinity", icon: "sparkles" },
    ],
  },
  {
    label: "Creatives",
    icon: "palette",
    children: [
      { label: "Create an Ad", href: "/ads/creatives/create", icon: "plus-circle", primary: true },
      { label: "Creative Library", href: "/ads/creatives/library", icon: "folder" },
      { label: "Audio Upload", href: "/ads/creatives/audio", icon: "play-circle" },
      { label: "Companion Images", href: "/ads/creatives/companion", icon: "layout" },
      { label: "Logo Management", href: "/ads/creatives/logo", icon: "folder" },
      { label: "CTA Selector", href: "/ads/creatives/cta", icon: "link" },
      { label: "Ad Preview", href: "/ads/creatives/preview", icon: "ad" },
      { label: "AI Creative Gen", href: "/ads/creatives/ai", icon: "sparkles" },
      { label: "Creator Partnerships", href: "/ads/creatives/partnerships", icon: "users" },
    ],
  },
  {
    label: "Analytics",
    icon: "chart",
    children: [
      { label: "Analytics Dashboard", href: "/ads/analytics", icon: "chart" },
      { label: "Audience Insights", href: "/ads/analytics/audience", icon: "insight" },
      { label: "Attribution", href: "/ads/analytics/attribution", icon: "path" },
      { label: "Experiments", href: "/ads/analytics/experiments", icon: "flask" },
      { label: "Cross-Media", href: "/ads/analytics/cross-media", icon: "layout" },
      { label: "Third-Party", href: "/ads/analytics/third-party", icon: "shield" },
      { label: "Metrics Glossary", href: "/ads/analytics/metrics-glossary", icon: "file-text" },
      { label: "Reports", href: "/ads/analytics/reports", icon: "report" },
    ],
  },
  {
    label: "Leads",
    icon: "user-check",
    children: [
      { label: "Leads Center", href: "/ads/leads", icon: "user-check" },
      { label: "Instant Forms", href: "/ads/leads/instant-forms", icon: "file-text" },
      { label: "Website Forms", href: "/ads/leads/website-forms", icon: "file-text" },
      { label: "Direct Messages", href: "/ads/leads/direct-messages", icon: "message" },
      { label: "Inbox", href: "/ads/leads/inbox", icon: "inbox" },
      { label: "Message Settings", href: "/ads/leads/messaging", icon: "settings" },
      { label: "CRM Integration", href: "/ads/leads/crm", icon: "link" },
    ],
  },
  {
    label: "Tools & Resources",
    icon: "puzzle",
    children: [
      { label: "Keyword Planner", href: "/ads/tools/keyword-planner", icon: "target" },
      { label: "Negative Keywords", href: "/ads/tools/negative-keywords", icon: "target" },
      { label: "Video Editor", href: "/ads/tools/video-editor", icon: "play-circle" },
      { label: "Integrations", href: "/ads/tools/integrations", icon: "puzzle" },
      { label: "MCP Server", href: "/ads/tools/mcp", icon: "code" },
      { label: "AI Skills", href: "/ads/ai/skills", icon: "sparkles" },
    ],
  },
  {
    label: "Agency",
    icon: "building",
    children: [
      { label: "Agency Dashboard", href: "/ads/agency", icon: "dashboard" },
      { label: "Client Management", href: "/ads/agency/clients", icon: "users" },
      { label: "Cross-Client Reporting", href: "/ads/agency/cross-client", icon: "chart" },
      { label: "Agency Billing", href: "/ads/agency/billing", icon: "credit-card" },
      { label: "Agency Team", href: "/ads/agency/team", icon: "users-cog" },
    ],
  },
];

export default function AdsLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const [notifOpen, setNotifOpen] = useState(false);

  /* Auto-expand the section that contains the current route */
  const expandedByDefault = useMemo(() => {
    const idx = navTree.findIndex((s) =>
      s.children.some(
        (c) => pathname === c.href || (c.href !== "/ads" && pathname.startsWith(c.href))
      )
    );
    return idx >= 0 ? idx : 0; // default to Overview
  }, [pathname]);

  const [expanded, setExpanded] = useState<number>(expandedByDefault);

  /* Keep expanded in sync if pathname changes */
  useMemo(() => {
    setExpanded(expandedByDefault);
  }, [expandedByDefault]);

  function toggleSection(idx: number) {
    setExpanded(expanded === idx ? -1 : idx);
  }

  return (
    <div className="flex h-screen bg-white text-neutral-900">
      {/* ─── Left Sidebar ─── */}
      <aside className="flex w-60 shrink-0 flex-col border-r border-neutral-200 bg-white">
        {/* Logo */}
        <div className="flex h-14 items-center border-b border-neutral-200 px-5">
          <img
            src="/logo-full-same-row.png"
            alt="Musicosy"
            className="h-9 w-auto object-contain"
          />
        </div>

        {/* Global Create Campaign button */}
        <div className="px-4 pt-4 pb-2">
          <Link
            href="/ads/ads-manager/campaigns/create"
            className="flex w-full items-center justify-center gap-2 rounded-lg bg-neutral-900 px-4 py-2.5 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 5v14M5 12h14" />
            </svg>
            Create Campaign
          </Link>
        </div>

        {/* Collapsible nav tree */}
        <nav className="flex-1 overflow-y-auto px-3 py-1">
          {navTree.map((section, idx) => {
            const isExpanded = expanded === idx;
            const isActive = section.children.some(
              (c) => pathname === c.href || (c.href !== "/ads" && pathname.startsWith(c.href))
            );
            return (
              <div key={section.label} className="mb-0.5">
                {/* Section header — clickable to expand/collapse */}
                <button
                  onClick={() => toggleSection(idx)}
                  className={`flex w-full items-center gap-2.5 rounded-lg px-2 py-2 text-[13px] font-medium transition-colors ${
                    isActive
                      ? "text-neutral-900"
                      : "text-neutral-500 hover:text-neutral-700"
                  }`}
                >
                  <SidebarIcon type={section.icon} size={16} />
                  <span className="flex-1 text-left">{section.label}</span>
                  <svg
                    width="12"
                    height="12"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className={`text-neutral-400 transition-transform duration-200 ${
                      isExpanded ? "rotate-90" : ""
                    }`}
                  >
                    <path d="M9 18l6-6-6-6" />
                  </svg>
                </button>

                {/* Children — only rendered when expanded */}
                <div
                  className={`overflow-hidden transition-all duration-200 ${
                    isExpanded ? "max-h-96 opacity-100" : "max-h-0 opacity-0"
                  }`}
                >
                  <div className="ml-4 border-l border-neutral-200 py-0.5">
                    {section.children.map((child) => {
                      const childActive =
                        pathname === child.href ||
                        (child.href !== "/ads" && pathname.startsWith(child.href));
                      return (
                        <Link
                          key={child.href + child.label}
                          href={child.href}
                          className={`flex items-center gap-2.5 rounded-lg px-2.5 py-[6px] pl-3 text-[13px] transition-colors ${
                            childActive
                              ? "bg-neutral-100 font-medium text-neutral-900"
                              : child.primary
                                ? "font-medium text-neutral-900 hover:bg-neutral-50"
                                : "text-neutral-500 hover:bg-neutral-50 hover:text-neutral-700"
                          }`}
                        >
                          <SidebarIcon type={child.icon} size={14} />
                          {child.label}
                        </Link>
                      );
                    })}
                  </div>
                </div>
              </div>
            );
          })}
        </nav>

        {/* Profile — uses auth hook for real user data */}
        <SidebarProfile />
      </aside>

      {/* ─── Right area: top bar + main ─── */}
      <div className="flex flex-1 flex-col overflow-hidden">
        {/* ─── Top Bar ─── */}
        <header className="flex h-14 shrink-0 items-center justify-between border-b border-neutral-200 bg-white px-5">
          <div className="flex items-center gap-3">
            {/* Account Switcher — driven by auth state */}
            <AccountSwitcher />

            {/* Plan / Subscription Status — driven by auth state */}
            <PlanBadge />
          </div>

          <div className="flex items-center gap-2">
            {/* Global Search */}
            <button className="flex items-center gap-2 rounded-lg border border-neutral-200 px-3 py-1.5 text-sm text-neutral-400 transition-colors hover:bg-neutral-50 hover:text-neutral-600">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="11" cy="11" r="8" />
                <path d="M21 21l-4.35-4.35" />
              </svg>
              Search…
              <kbd className="ml-4 rounded border border-neutral-200 px-1.5 py-0.5 text-[10px] font-medium text-neutral-400">⌘K</kbd>
            </button>

            {/* Date Range */}
            <button className="flex items-center gap-1.5 rounded-lg border border-neutral-200 px-3 py-1.5 text-sm text-neutral-600 transition-colors hover:bg-neutral-50">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" />
                <line x1="16" y1="2" x2="16" y2="6" />
                <line x1="8" y1="2" x2="8" y2="6" />
                <line x1="3" y1="10" x2="21" y2="10" />
              </svg>
              Last 30 days
            </button>

            {/* Help */}
            <button className="flex h-8 w-8 items-center justify-center rounded-lg text-neutral-400 transition-colors hover:bg-neutral-50 hover:text-neutral-600">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10" />
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
                <line x1="12" y1="17" x2="12.01" y2="17" />
              </svg>
            </button>

            {/* Notifications */}
            <button
              onClick={() => setNotifOpen(!notifOpen)}
              className="relative flex h-8 w-8 items-center justify-center rounded-lg text-neutral-400 transition-colors hover:bg-neutral-50 hover:text-neutral-600"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                <path d="M18 8A6 6 0 1 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" />
                <path d="M13.73 21a2 2 0 0 1-3.46 0" />
              </svg>
              <span className="absolute right-1 top-1 flex h-2 w-2 rounded-full bg-red-500" />
            </button>

            {/* Profile Dropdown — Settings + Sign Out live here */}
            <ProfileDropdown />
          </div>
        </header>

        {/* ─── Main Content ─── */}
        <main className="flex-1 overflow-y-auto bg-neutral-50/50 p-6">{children}</main>
      </div>

      {/* ─── Notification Drawer ─── */}
      {notifOpen && (
        <div className="fixed inset-0 z-50 flex justify-end">
          <div className="absolute inset-0 bg-black/20" onClick={() => setNotifOpen(false)} />
          <div className="relative w-96 shrink-0 border-l border-neutral-200 bg-white shadow-xl">
            <div className="flex h-14 items-center justify-between border-b border-neutral-200 px-5">
              <h3 className="text-sm font-semibold text-neutral-900">Notifications</h3>
              <button onClick={() => setNotifOpen(false)} className="text-neutral-400 hover:text-neutral-600">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M18 6L6 18M6 6l12 12" /></svg>
              </button>
            </div>
            <div className="p-4">
              {["Issues", "Announcements", "Suggestions", "Tickets", "Asset Sync", "Events", "Features", "Promotions"].map((tab) => (
                <div key={tab} className="rounded-lg border border-neutral-100 bg-neutral-50 p-3 text-sm text-neutral-600 mb-2">
                  No {tab.toLowerCase()} notifications
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

/* ─── Account Switcher — driven by auth state ─── */
function AccountSwitcher() {
  const { user } = useCurrentUser();
  return (
    <button className="flex items-center gap-2 rounded-lg border border-neutral-200 px-3 py-1.5 text-sm font-medium text-neutral-700 transition-colors hover:bg-neutral-50">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
        <circle cx="12" cy="7" r="4" />
      </svg>
      {user?.accountName || "My Account"}
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M6 9l6 6 6-6" /></svg>
    </button>
  );
}

/* ─── Plan Badge — driven by auth state ─── */
function PlanBadge() {
  const { user } = useCurrentUser();
  return (
    <Link href="/ads/billing/plans" className="flex items-center gap-1.5 rounded-lg border border-neutral-200 px-3 py-1.5 text-xs font-medium text-neutral-500 transition-colors hover:bg-neutral-50 hover:text-neutral-700">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
        <rect x="1" y="4" width="22" height="16" rx="2" /><path d="M1 10h22" />
      </svg>
      {user?.plan?.label || "Free"}
    </Link>
  );
}

/* ─── Sidebar Icons ─── */
function SidebarIcon({ type, size = 16 }: { type: string; size?: number }) {
  const p: React.SVGProps<SVGSVGElement> = {
    width: size,
    height: size,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 1.5,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
  };
  switch (type) {
    case "home":
      return <svg {...p}><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" /><polyline points="9 22 9 12 15 12 15 22" /></svg>;
    case "dashboard":
      return <svg {...p}><rect x="3" y="3" width="7" height="7" rx="1" /><rect x="14" y="3" width="7" height="7" rx="1" /><rect x="3" y="14" width="7" height="7" rx="1" /><rect x="14" y="14" width="7" height="7" rx="1" /></svg>;
    case "campaigns":
      return <svg {...p}><path d="M12 2L2 7l10 5 10-5-10-5z" /><path d="M2 17l10 5 10-5" /><path d="M2 12l10 5 10-5" /></svg>;
    case "layers":
      return <svg {...p}><path d="M12 2L2 7l10 5 10-5-10-5z" /><path d="M2 17l10 5 10-5" /></svg>;
    case "ad":
      return <svg {...p}><rect x="2" y="3" width="20" height="14" rx="2" /><path d="M8 21h8" /><path d="M12 17v4" /></svg>;
    case "draft":
      return <svg {...p}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" /><polyline points="14 2 14 8 20 8" /><line x1="16" y1="13" x2="8" y2="13" /><line x1="16" y1="17" x2="8" y2="17" /></svg>;
    case "plus-circle":
      return <svg {...p}><circle cx="12" cy="12" r="10" /><path d="M12 8v8M8 12h8" /></svg>;
    case "folder":
      return <svg {...p}><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z" /></svg>;
    case "palette":
      return <svg {...p}><circle cx="13.5" cy="6.5" r="2.5" /><circle cx="6" cy="12" r="2.5" /><circle cx="18" cy="12" r="2.5" /><circle cx="8.5" cy="18.5" r="2.5" /><circle cx="15.5" cy="18.5" r="2.5" /></svg>;
    case "users":
      return <svg {...p}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>;
    case "catalog":
      return <svg {...p}><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z" /><line x1="3" y1="6" x2="21" y2="6" /><path d="M16 10a4 4 0 0 1-8 0" /></svg>;
    case "layout":
      return <svg {...p}><rect x="3" y="3" width="18" height="18" rx="2" /><line x1="3" y1="9" x2="21" y2="9" /><line x1="9" y1="9" x2="9" y2="21" /></svg>;
    case "chart":
      return <svg {...p}><path d="M3 3v18h18" /><path d="M7 16l4-4 4 4 5-5" /></svg>;
    case "report":
      return <svg {...p}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" /><polyline points="14 2 14 8 20 8" /><line x1="16" y1="13" x2="8" y2="13" /><line x1="16" y1="17" x2="8" y2="17" /></svg>;
    case "path":
      return <svg {...p}><circle cx="5" cy="6" r="3" /><circle cx="19" cy="18" r="3" /><path d="M15 9l-3-3 3-3" /><path d="M9 15l3 3-3 3" /><path d="M8 9h8" /><path d="M16 15H8" /></svg>;
    case "flask":
      return <svg {...p}><path d="M9 3h6" /><path d="M10 9V3h4v6l5 8.5a2 2 0 0 1-1.73 3H6.73a2 2 0 0 1-1.73-3L10 9z" /></svg>;
    case "insight":
      return <svg {...p}><circle cx="12" cy="12" r="10" /><path d="M12 16v-4" /><path d="M12 8h.01" /></svg>;
    case "play-circle":
      return <svg {...p}><circle cx="12" cy="12" r="10" /><polygon points="10 8 16 12 10 16 10 8" /></svg>;
    case "user-check":
      return <svg {...p}><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="8.5" cy="7" r="4" /><polyline points="17 11 19 13 23 9" /></svg>;
    case "file-text":
      return <svg {...p}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" /><polyline points="14 2 14 8 20 8" /><line x1="16" y1="13" x2="8" y2="13" /><line x1="16" y1="17" x2="8" y2="17" /></svg>;
    case "message":
      return <svg {...p}><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" /></svg>;
    case "inbox":
      return <svg {...p}><polyline points="22 12 18 12 15 15 9 15 6 12 2 12" /><path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z" /></svg>;
    case "link":
      return <svg {...p}><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" /><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" /></svg>;
    case "calendar":
      return <svg {...p}><rect x="3" y="4" width="18" height="18" rx="2" /><line x1="16" y1="2" x2="16" y2="6" /><line x1="8" y1="2" x2="8" y2="6" /><line x1="3" y1="10" x2="21" y2="10" /></svg>;
    case "zap":
      return <svg {...p}><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" /></svg>;
    case "message-square":
      return <svg {...p}><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" /></svg>;
    case "shield":
      return <svg {...p}><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" /></svg>;
    case "puzzle":
      return <svg {...p}><path d="M16 3h5v5M4 21h5v-5M21 8l-9 9M8 4l-4 4" /></svg>;
    case "sparkles":
      return <svg {...p}><path d="M12 2l2 7h7l-5.5 4 2 7L12 16l-5.5 4 2-7L3 9h7z" /></svg>;
    case "credit-card":
      return <svg {...p}><rect x="1" y="4" width="22" height="16" rx="2" /><path d="M1 10h22" /></svg>;
    case "wallet":
      return <svg {...p}><path d="M20 12V8H6a2 2 0 0 1-2-2c0-1.1.9-2 2-2h12v4" /><path d="M4 6v12a2 2 0 0 0 2 2h14v-4" /><path d="M18 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4z" /></svg>;
    case "receipt":
      return <svg {...p}><path d="M4 2v20l3-2 3 2 3-2 3 2 3-2 3 2V2l-3 2-3-2-3 2-3-2-3 2-3-2z" /></svg>;
    case "arrow-left-right":
      return <svg {...p}><path d="M17 1l4 4-4 4" /><path d="M3 5h18" /><path d="M7 23l-4-4 4-4" /><path d="M21 19H3" /></svg>;
    case "percent":
      return <svg {...p}><line x1="19" y1="5" x2="5" y2="19" /><circle cx="6.5" cy="6.5" r="2.5" /><circle cx="17.5" cy="17.5" r="2.5" /></svg>;
    case "gift":
      return <svg {...p}><polyline points="20 12 20 22 4 22 4 12" /><rect x="2" y="7" width="20" height="5" /><line x1="12" y1="22" x2="12" y2="7" /><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z" /><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z" /></svg>;
    case "bell":
      return <svg {...p}><path d="M18 8A6 6 0 1 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" /><path d="M13.73 21a2 2 0 0 1-3.46 0" /></svg>;
    case "building":
      return <svg {...p}><rect x="4" y="2" width="16" height="20" rx="2" /><path d="M9 22v-4h6v4" /><path d="M8 6h.01M16 6h.01M12 6h.01M8 10h.01M16 10h.01M12 10h.01M8 14h.01M16 14h.01M12 14h.01" /></svg>;
    case "users-cog":
      return <svg {...p}><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><path d="M23 21v-2a4 4 0 0 0-3-3.87" /><path d="M16 3.13a4 4 0 0 1 0 7.75" /></svg>;
    case "check-circle":
      return <svg {...p}><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" /><polyline points="22 4 12 14.01 9 11.01" /></svg>;
    case "lock":
      return <svg {...p}><rect x="3" y="11" width="18" height="11" rx="2" /><path d="M7 11V7a5 5 0 0 1 10 0v4" /></svg>;
    case "target":
      return <svg {...p}><circle cx="12" cy="12" r="10" /><circle cx="12" cy="12" r="6" /><circle cx="12" cy="12" r="2" /></svg>;
    case "code":
      return <svg {...p}><polyline points="16 18 22 12 16 6" /><polyline points="8 6 2 12 8 18" /></svg>;
    case "settings":
      return <svg {...p}><circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" /></svg>;
    case "help":
      return <svg {...p}><circle cx="12" cy="12" r="10" /><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" /><line x1="12" y1="17" x2="12.01" y2="17" /></svg>;
    default:
      return <svg {...p}><circle cx="12" cy="12" r="1" /></svg>;
  }
}
