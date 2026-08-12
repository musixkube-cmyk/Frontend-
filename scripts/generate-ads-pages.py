#!/usr/bin/env python3
"""Generate all Ad Center route pages for the consolidated nav structure."""

import os

BASE = "/home/z/my-project/src/app/ads"

def write(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  wrote {path}")

# ─── Helper: standard page shell ───
def page(title: str, desc: str, content: str = "") -> str:
    return f'''"use client";

import Link from "next/link";

export default function Page() {{
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">{title}</h1>
          <p className="mt-1 text-sm text-neutral-500">{desc}</p>
        </div>
      </div>
{content}
    </div>
  );
}}
'''

# ─── Helper: standard list page with table ───
def list_page(title: str, desc: str, columns: list[str], rows: list[list[str]], create_label: str = "", create_href: str = "") -> str:
    col_headers = "\n".join(f'              <th className="px-4 py-3">{c}</th>' for c in columns)
    row_cells = ""
    for row in rows:
        cells = "\n".join(f'                <td className="px-4 py-3 text-sm text-neutral-700">{c}</td>' for c in row)
        row_cells += f'''            <tr className="border-b border-neutral-50">
{cells}
            </tr>
'''
    create_btn = ""
    if create_label and create_href:
        create_btn = f'''        <Link
          href="{create_href}"
          className="flex h-9 items-center gap-2 rounded-lg bg-neutral-900 px-4 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M5 12h14" /></svg>
          {create_label}
        </Link>'''

    return f'''"use client";

import Link from "next/link";

export default function Page() {{
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">{title}</h1>
          <p className="mt-1 text-sm text-neutral-500">{desc}</p>
        </div>
        {create_btn}
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
{col_headers}
            </tr>
          </thead>
          <tbody>
{row_cells}
          </tbody>
        </table>
      </div>
    </div>
  );
}}
'''

# ─── Helper: card grid page ───
def card_page(title: str, desc: str, cards: list[dict]) -> str:
    card_html = ""
    for c in cards:
        card_html += f'''          <Link
            href="{c.get('href', '#')}"
            className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200 hover:bg-neutral-50"
          >
            <h3 className="text-sm font-semibold text-neutral-900">{c['label']}</h3>
            <p className="mt-1 text-xs text-neutral-500">{c.get('desc', '')}</p>
          </Link>
'''
    return f'''"use client";

import Link from "next/link";

export default function Page() {{
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">{title}</h1>
        <p className="mt-1 text-sm text-neutral-500">{desc}</p>
      </div>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
{card_html}
      </div>
    </div>
  );
}}
'''

# ═══════════════════════════════════════════════════════
# OVERVIEW
# ═══════════════════════════════════════════════════════

# Dashboard is /ads/page.tsx — already exists, we'll update it
write(f"{BASE}/page.tsx", '''"use client";

import Link from "next/link";

const campaigns = [
  { id: 1, name: "Summer Launch 2026", status: "Active", objective: "Conversions", spend: "$2,450", results: "1,230 clicks", date: "Jul 15 – Aug 12" },
  { id: 2, name: "Brand Awareness Push", status: "Active", objective: "Awareness", spend: "$890", results: "45K impressions", date: "Aug 1 – Aug 31" },
  { id: 3, name: "Catalog Carousel Test", status: "Paused", objective: "Conversions", spend: "$340", results: "89 clicks", date: "Jun 20 – Jul 5" },
];

export default function AdsDashboard() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Dashboard</h1>
          <p className="mt-1 text-sm text-neutral-500">Monitor account health and jump into optimization.</p>
        </div>
        <Link
          href="/ads/campaigns/create"
          className="flex h-10 items-center gap-2 rounded-lg bg-neutral-900 px-5 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M5 12h14" /></svg>
          Create Campaign
        </Link>
      </div>

      {/* KPI row */}
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        {[
          { label: "Spend", value: "$3,680", delta: "+12% vs last period" },
          { label: "Impressions", value: "142K", delta: "+8%" },
          { label: "CTR", value: "1.24%", delta: "+0.05%" },
          { label: "CPA", value: "$2.99", delta: "-$0.21" },
        ].map((kpi) => (
          <div key={kpi.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{kpi.label}</p>
            <p className="mt-2 text-3xl font-bold text-neutral-900">{kpi.value}</p>
            <p className="mt-1 text-xs text-emerald-600">{kpi.delta}</p>
          </div>
        ))}
      </div>

      {/* Campaign table */}
      <div className="rounded-xl border border-neutral-100 bg-white">
        <div className="flex items-center justify-between border-b border-neutral-100 px-5 py-4">
          <h2 className="text-sm font-semibold text-neutral-900">Active Campaigns</h2>
          <Link href="/ads/campaigns" className="text-xs font-medium text-neutral-500 transition-colors hover:text-neutral-900">View all</Link>
        </div>
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-5 py-3">Campaign</th>
              <th className="px-5 py-3">Status</th>
              <th className="px-5 py-3">Objective</th>
              <th className="px-5 py-3">Spend</th>
              <th className="px-5 py-3">Results</th>
              <th className="px-5 py-3">Date range</th>
            </tr>
          </thead>
          <tbody>
            {campaigns.map((c) => (
              <tr key={c.id} className="border-b border-neutral-50 text-sm last:border-0">
                <td className="px-5 py-4 font-medium text-neutral-900">{c.name}</td>
                <td className="px-5 py-4">
                  <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${c.status === "Active" ? "bg-emerald-50 text-emerald-700" : "bg-neutral-100 text-neutral-500"}`}>
                    {c.status}
                  </span>
                </td>
                <td className="px-5 py-4 text-neutral-600">{c.objective}</td>
                <td className="px-5 py-4 text-neutral-900">{c.spend}</td>
                <td className="px-5 py-4 text-neutral-600">{c.results}</td>
                <td className="px-5 py-4 text-neutral-400">{c.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
''')

# Notifications
write(f"{BASE}/notifications/page.tsx", list_page(
    "Notifications",
    "Review and resolve account events.",
    ["Type", "Message", "Time", "Status"],
    [
        ["Issue", "Campaign budget exhausted", "2 min ago", "Unresolved"],
        ["Announcement", "New placement: Top Feed Video", "1 hour ago", "Read"],
        ["Suggestion", "Increase budget on Summer Launch for 15% more reach", "3 hours ago", "Pending"],
        ["Ticket", "Creative rejected — policy violation", "Yesterday", "Open"],
    ],
))

# ═══════════════════════════════════════════════════════
# CAMPAIGNS
# ═══════════════════════════════════════════════════════

write(f"{BASE}/campaigns/page.tsx", list_page(
    "All Campaigns",
    "Find, compare, pause, duplicate, edit, and report on campaigns.",
    ["Campaign", "Status", "Objective", "Spend", "Results", "Date range"],
    [
        ["Summer Launch 2026", "Active", "Conversions", "$2,450", "1,230 clicks", "Jul 15 – Aug 12"],
        ["Brand Awareness Push", "Active", "Awareness", "$890", "45K impressions", "Aug 1 – Aug 31"],
        ["Catalog Carousel Test", "Paused", "Conversions", "$340", "89 clicks", "Jun 20 – Jul 5"],
        ["Artist Spotlight Q3", "Draft", "Consideration", "$0", "—", "Not set"],
        ["Holiday Promo 2025", "Completed", "Sales", "$12,400", "4,200 purchases", "Dec 1 – Dec 31"],
    ],
    "Create Campaign", "/ads/campaigns/create",
))

# Campaign detail
write(f"{BASE}/campaigns/[id]/page.tsx", '''"use client";

import Link from "next/link";
import { use } from "react";

export default function CampaignDetail({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  return (
    <div>
      <div className="mb-6">
        <div className="flex items-center gap-2 text-sm text-neutral-500">
          <Link href="/ads/campaigns" className="hover:text-neutral-900">Campaigns</Link>
          <span>/</span>
          <span className="text-neutral-900">Campaign {id}</span>
        </div>
        <div className="mt-3 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Summer Launch 2026</h1>
            <div className="mt-2 flex items-center gap-3">
              <span className="inline-flex items-center rounded-full bg-emerald-50 px-2.5 py-0.5 text-xs font-medium text-emerald-700">Active</span>
              <span className="text-sm text-neutral-500">Conversions · Daily budget $100</span>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700 transition-colors hover:bg-neutral-50">Pause</button>
            <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700 transition-colors hover:bg-neutral-50">Duplicate</button>
            <Link href={`/ads/campaigns/${id}/edit`} className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-neutral-800">Edit</Link>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="mb-6 flex gap-1 border-b border-neutral-200">
        {["Overview", "Ad Groups", "Ads", "Analytics", "Settings", "Activity"].map((tab, i) => (
          <button key={tab} className={`px-4 py-2.5 text-sm font-medium transition-colors ${i === 0 ? "border-b-2 border-neutral-900 text-neutral-900" : "text-neutral-500 hover:text-neutral-700"}`}>
            {tab}
          </button>
        ))}
      </div>

      {/* KPI row */}
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        {[
          { label: "Spend", value: "$2,450" },
          { label: "Impressions", value: "89.2K" },
          { label: "Clicks", value: "1,230" },
          { label: "Conversions", value: "186" },
        ].map((kpi) => (
          <div key={kpi.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{kpi.label}</p>
            <p className="mt-2 text-2xl font-bold text-neutral-900">{kpi.value}</p>
          </div>
        ))}
      </div>

      {/* Ad Groups table */}
      <div className="rounded-xl border border-neutral-100 bg-white">
        <div className="border-b border-neutral-100 px-5 py-4">
          <h2 className="text-sm font-semibold text-neutral-900">Ad Groups</h2>
        </div>
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-5 py-3">Ad Group</th>
              <th className="px-5 py-3">Status</th>
              <th className="px-5 py-3">Budget</th>
              <th className="px-5 py-3">Spend</th>
              <th className="px-5 py-3">Results</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50 text-sm">
              <td className="px-5 py-4 font-medium text-neutral-900">Audio — Broad Audience</td>
              <td className="px-5 py-4"><span className="inline-flex items-center rounded-full bg-emerald-50 px-2 py-0.5 text-xs font-medium text-emerald-700">Active</span></td>
              <td className="px-5 py-4 text-neutral-700">$50/day</td>
              <td className="px-5 py-4 text-neutral-900">$1,520</td>
              <td className="px-5 py-4 text-neutral-700">842 clicks</td>
            </tr>
            <tr className="text-sm">
              <td className="px-5 py-4 font-medium text-neutral-900">Video — Retarget</td>
              <td className="px-5 py-4"><span className="inline-flex items-center rounded-full bg-emerald-50 px-2 py-0.5 text-xs font-medium text-emerald-700">Active</span></td>
              <td className="px-5 py-4 text-neutral-700">$50/day</td>
              <td className="px-5 py-4 text-neutral-900">$930</td>
              <td className="px-5 py-4 text-neutral-700">388 clicks</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
''')

# Campaign edit
write(f"{BASE}/campaigns/[id]/edit/page.tsx", page("Edit Campaign", "Modify campaign settings, budget, and targeting.", '''      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <div className="grid gap-6 lg:grid-cols-2">
          <div>
            <label className="block text-sm font-medium text-neutral-700 mb-1">Campaign name</label>
            <input defaultValue="Summer Launch 2026" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
          </div>
          <div>
            <label className="block text-sm font-medium text-neutral-700 mb-1">Objective</label>
            <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
              <option>Conversions</option><option>Awareness</option><option>Consideration</option><option>Traffic</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-neutral-700 mb-1">Daily budget</label>
            <input defaultValue="100" type="number" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
          </div>
          <div>
            <label className="block text-sm font-medium text-neutral-700 mb-1">Delivery type</label>
            <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
              <option>Standard</option><option>Accelerated</option>
            </select>
          </div>
        </div>
        <div className="mt-6 flex justify-end gap-3">
          <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700">Cancel</button>
          <button className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white">Save</button>
        </div>
      </div>'''))

# Ad Groups list
write(f"{BASE}/campaigns/groups/page.tsx", list_page(
    "Ad Groups",
    "Configure and optimize distribution across your campaigns.",
    ["Ad Group", "Campaign", "Status", "Budget", "Spend", "Results"],
    [
        ["Audio — Broad Audience", "Summer Launch 2026", "Active", "$50/day", "$1,520", "842 clicks"],
        ["Video — Retarget", "Summer Launch 2026", "Active", "$50/day", "$930", "388 clicks"],
        ["Awareness — Gen Z", "Brand Awareness Push", "Active", "$30/day", "$445", "22K impressions"],
    ],
    "Create Ad Group", "/ads/campaigns/groups/create",
))

write(f"{BASE}/campaigns/groups/create/page.tsx", page("Create Ad Group", "Add a distribution group under a campaign.", '''      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <div className="grid gap-6 lg:grid-cols-2">
          <div className="lg:col-span-2">
            <label className="block text-sm font-medium text-neutral-700 mb-1">Ad group name</label>
            <input placeholder="e.g. Audio — Broad Audience" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
          </div>
          <div>
            <label className="block text-sm font-medium text-neutral-700 mb-1">Budget</label>
            <input defaultValue="50" type="number" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
          </div>
          <div>
            <label className="block text-sm font-medium text-neutral-700 mb-1">Optimization goal</label>
            <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
              <option>Clicks</option><option>Conversions</option><option>Impressions</option>
            </select>
          </div>
        </div>
        <div className="mt-6 flex justify-end gap-3">
          <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700">Cancel</button>
          <button className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white">Create</button>
        </div>
      </div>'''))

# Ad Group detail
write(f"{BASE}/campaigns/groups/[id]/page.tsx", page("Ad Group Detail", "Configure targeting, placements, budget/bid, analytics, and frequency controls.", '''      <div className="mb-6 flex gap-1 border-b border-neutral-200">
        {["Targeting", "Placements", "Budget & Bid", "Analytics", "Frequency Controls"].map((tab, i) => (
          <button key={tab} className={`px-4 py-2.5 text-sm font-medium transition-colors ${i === 0 ? "border-b-2 border-neutral-900 text-neutral-900" : "text-neutral-500 hover:text-neutral-700"}`}>{tab}</button>
        ))}
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-4">Audience targeting</h3>
        <div className="grid gap-4 lg:grid-cols-2">
          <div><label className="block text-sm text-neutral-600 mb-1">Location</label><input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
          <div><label className="block text-sm text-neutral-600 mb-1">Age</label><input defaultValue="18-55" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
          <div><label className="block text-sm text-neutral-600 mb-1">Gender</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>All</option><option>Male</option><option>Female</option></select></div>
          <div><label className="block text-sm text-neutral-600 mb-1">Language</label><input defaultValue="English" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
        </div>
      </div>'''))

# Ads list
write(f"{BASE}/campaigns/ads/page.tsx", list_page(
    "Ads",
    "Manage individual ad creatives and their delivery.",
    ["Ad", "Ad Group", "Status", "Type", "Spend", "Results"],
    [
        ["Summer Audio Spot", "Audio — Broad Audience", "Active", "Audio", "$820", "456 clicks"],
        ["Companion Banner", "Audio — Broad Audience", "Active", "Image", "$700", "386 clicks"],
        ["Video Retarget 15s", "Video — Retarget", "Active", "Video", "$930", "388 clicks"],
    ],
    "Create Ad", "/ads/campaigns/create",
))

# Drafts
write(f"{BASE}/campaigns/drafts/page.tsx", list_page(
    "Drafts",
    "Resume incomplete campaign builds.",
    ["Draft", "Objective", "Last edited", "Owner", "Status"],
    [
        ["Artist Spotlight Q3", "Consideration", "Aug 10, 2026", "You", "In progress"],
        ["Podcast Promo", "Awareness", "Aug 8, 2026", "You", "In progress"],
    ],
))

# Campaign create — the 5-step builder
write(f"{BASE}/campaigns/create/page.tsx", '''"use client";

import { useState } from "react";
import Link from "next/link";

const steps = ["Objective", "Campaign", "Ad Group", "Ad", "Review"];

const objectives = [
  { category: "Awareness", items: ["Reach", "Video Views"] },
  { category: "Consideration", items: ["Traffic", "Community Interaction", "Brand Consideration", "Music Streams"] },
  { category: "Conversion", items: ["App Promotion", "Lead Generation", "Sales"] },
];

export default function CreateCampaign() {
  const [step, setStep] = useState(0);
  const [objective, setObjective] = useState("");
  const [campaignName, setCampaignName] = useState("");
  const [dailyBudget, setDailyBudget] = useState("50");
  const [budgetType, setBudgetType] = useState("daily");

  return (
    <div>
      {/* Stepper */}
      <div className="mb-8 flex items-center gap-2">
        {steps.map((s, i) => (
          <div key={s} className="flex items-center gap-2">
            <button
              onClick={() => i <= step && setStep(i)}
              className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-semibold transition-colors ${
                i < step ? "bg-neutral-900 text-white" : i === step ? "border-2 border-neutral-900 text-neutral-900" : "border border-neutral-300 text-neutral-400"
              }`}
            >
              {i < step ? "✓" : i + 1}
            </button>
            <span className={`text-sm ${i === step ? "font-medium text-neutral-900" : "text-neutral-400"}`}>{s}</span>
            {i < steps.length - 1 && <div className="mx-2 h-px w-8 bg-neutral-200" />}
          </div>
        ))}
      </div>

      <div className="flex gap-6">
        {/* Main form area */}
        <div className="flex-1">
          {/* Step 0: Objective */}
          {step === 0 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Choose an objective</h2>
              <p className="text-sm text-neutral-500 mb-6">Your objective determines how your ads are optimized and delivered.</p>
              <div className="space-y-6">
                {objectives.map((cat) => (
                  <div key={cat.category}>
                    <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">{cat.category}</h3>
                    <div className="grid grid-cols-2 gap-3">
                      {cat.items.map((item) => (
                        <button
                          key={item}
                          onClick={() => setObjective(item)}
                          className={`rounded-xl border p-4 text-left text-sm transition-colors ${
                            objective === item ? "border-neutral-900 bg-neutral-50 font-medium text-neutral-900" : "border-neutral-200 text-neutral-700 hover:border-neutral-300"
                          }`}
                        >
                          {item}
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Step 1: Campaign */}
          {step === 1 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Campaign settings</h2>
              <p className="text-sm text-neutral-500 mb-6">Name your campaign and configure budget and delivery.</p>
              <div className="space-y-5">
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Campaign name</label>
                  <input value={campaignName} onChange={(e) => setCampaignName(e.target.value)} placeholder="e.g. Summer Launch 2026" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Special ad category</label>
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                    <option>None</option><option>Housing</option><option>Credit</option><option>Employment</option><option>Politics</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Budget type</label>
                  <div className="flex gap-2">
                    <button onClick={() => setBudgetType("daily")} className={`rounded-lg px-4 py-2 text-sm font-medium transition-colors ${budgetType === "daily" ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-700"}`}>Daily</button>
                    <button onClick={() => setBudgetType("lifetime")} className={`rounded-lg px-4 py-2 text-sm font-medium transition-colors ${budgetType === "lifetime" ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-700"}`}>Lifetime</button>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">{budgetType === "daily" ? "Daily budget" : "Lifetime budget"}</label>
                  <div className="relative">
                    <span className="absolute left-3 top-1/2 -translate-y-1/2 text-sm text-neutral-400">$</span>
                    <input value={dailyBudget} onChange={(e) => setDailyBudget(e.target.value)} type="number" className="w-full rounded-lg border border-neutral-200 py-2.5 pl-7 pr-3 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Delivery type</label>
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                    <option>Standard</option><option>Accelerated</option>
                  </select>
                </div>
              </div>
            </div>
          )}

          {/* Step 2: Ad Group */}
          {step === 2 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Ad group configuration</h2>
              <p className="text-sm text-neutral-500 mb-6">Define audience, placements, and optimization for this ad group.</p>
              <div className="space-y-5">
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Ad group name</label>
                  <input defaultValue="Ad Group 1" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Locations</label>
                  <input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">Age range</label>
                    <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                      <option>18–55</option><option>18–24</option><option>25–34</option><option>35–54</option><option>55+</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">Gender</label>
                    <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                      <option>All</option><option>Male</option><option>Female</option>
                    </select>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Placements</label>
                  <div className="flex flex-wrap gap-2">
                    {["In-Feed Audio", "In-Feed Video", "Top Feed", "Search Ads", "Catalog Ads"].map((p) => (
                      <button key={p} className="rounded-lg border border-neutral-200 px-3 py-1.5 text-xs font-medium text-neutral-700 transition-colors hover:border-neutral-300">{p}</button>
                    ))}
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Optimization goal</label>
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                    <option>Maximize clicks</option><option>Maximize conversions</option><option>Maximize reach</option>
                  </select>
                </div>
              </div>
            </div>
          )}

          {/* Step 3: Ad */}
          {step === 3 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Ad creative</h2>
              <p className="text-sm text-neutral-500 mb-6">Choose or create your ad creative, set CTA and destination.</p>
              <div className="space-y-5">
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Ad name</label>
                  <input defaultValue="Ad 1" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Audio</label>
                  <div className="flex items-center justify-center rounded-xl border-2 border-dashed border-neutral-200 p-8 text-sm text-neutral-400">
                    <div className="text-center">
                      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="mx-auto mb-2 text-neutral-300"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /><polyline points="17 8 12 3 7 8" /><line x1="12" y1="3" x2="12" y2="15" /></svg>
                      Drag audio file or click to upload
                    </div>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Companion image</label>
                  <div className="flex items-center justify-center rounded-xl border-2 border-dashed border-neutral-200 p-8 text-sm text-neutral-400">
                    Upload companion image (1200×628)
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">CTA</label>
                    <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                      <option>Learn More</option><option>Shop Now</option><option>Listen Now</option><option>Download</option><option>Sign Up</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">Destination URL</label>
                    <input placeholder="https://..." className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Step 4: Review */}
          {step === 4 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Review & publish</h2>
              <p className="text-sm text-neutral-500 mb-6">Confirm your campaign configuration before publishing.</p>
              <div className="space-y-4">
                <div className="rounded-xl border border-neutral-100 bg-white p-5">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">Campaign</h3>
                  <div className="grid grid-cols-2 gap-y-2 text-sm">
                    <span className="text-neutral-500">Name</span><span className="text-neutral-900 font-medium">{campaignName || "Untitled"}</span>
                    <span className="text-neutral-500">Objective</span><span className="text-neutral-900 font-medium">{objective || "Not selected"}</span>
                    <span className="text-neutral-500">Budget</span><span className="text-neutral-900 font-medium">${dailyBudget}/{budgetType === "daily" ? "day" : "lifetime"}</span>
                  </div>
                </div>
                <div className="rounded-xl border border-neutral-100 bg-white p-5">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">Policy check</h3>
                  <p className="text-sm text-emerald-600">No issues found. Campaign is ready to publish.</p>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Right context panel — estimates & policy */}
        {step >= 1 && (
          <div className="hidden w-72 shrink-0 lg:block">
            <div className="rounded-xl border border-neutral-100 bg-white p-5">
              <h3 className="text-sm font-semibold text-neutral-900 mb-3">Estimated results</h3>
              <div className="space-y-3 text-sm">
                <div className="flex justify-between"><span className="text-neutral-500">Reach</span><span className="font-medium text-neutral-900">~24K</span></div>
                <div className="flex justify-between"><span className="text-neutral-500">Impressions</span><span className="font-medium text-neutral-900">~42K</span></div>
                <div className="flex justify-between"><span className="text-neutral-500">Clicks</span><span className="font-medium text-neutral-900">~520</span></div>
                <div className="flex justify-between"><span className="text-neutral-500">CPA</span><span className="font-medium text-neutral-900">~$9.60</span></div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Footer actions */}
      <div className="mt-8 flex items-center justify-between border-t border-neutral-200 pt-4">
        <button
          onClick={() => step > 0 && setStep(step - 1)}
          className={`text-sm font-medium ${step > 0 ? "text-neutral-700" : "text-neutral-300"}`}
          disabled={step === 0}
        >
          Back
        </button>
        <div className="flex gap-3">
          <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700">Save draft</button>
          {step < 4 ? (
            <button onClick={() => setStep(step + 1)} className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-neutral-800">Continue</button>
          ) : (
            <button className="rounded-lg bg-neutral-900 px-6 py-2 text-sm font-medium text-white transition-colors hover:bg-neutral-800">Publish</button>
          )}
        </div>
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════
# ASSETS
# ═══════════════════════════════════════════════════════

write(f"{BASE}/creatives/library/page.tsx", list_page(
    "Creative Library",
    "Store and reuse approved creative assets. Search, tag, and manage versions.",
    ["Asset", "Type", "Size", "Status", "Last updated", "Tags"],
    [
        ["Summer Hero Image", "Image", "1200×628", "Approved", "Aug 10, 2026", "summer, hero"],
        ["Brand Audio 30s", "Audio", "30s", "Approved", "Aug 8, 2026", "brand, audio"],
        ["Product Video 15s", "Video", "15s", "In review", "Aug 5, 2026", "product, video"],
        ["Logo Dark", "Image", "200×200", "Approved", "Jul 30, 2026", "logo"],
    ],
    "Upload Asset", "/ads/creatives/studio",
))

write(f"{BASE}/creatives/studio/page.tsx", card_page(
    "Creative Studio",
    "Build reusable ad creative. Upload, compose, preview, and generate with AI.",
    [
        {"label": "Audio Upload", "desc": "Upload and manage audio ad files", "href": "/ads/creatives/audio"},
        {"label": "Companion Images", "desc": "Upload companion visuals for audio ads", "href": "/ads/creatives/companion"},
        {"label": "Logo Manager", "desc": "Upload and manage brand logos", "href": "/ads/creatives/logo"},
        {"label": "CTA Builder", "desc": "Configure call-to-action buttons", "href": "/ads/creatives/cta"},
        {"label": "Destination URLs", "desc": "Set and validate landing page URLs", "href": "/ads/creatives/destination"},
        {"label": "Ad Preview", "desc": "Preview your ad across placements", "href": "/ads/creatives/preview"},
        {"label": "AI Generator", "desc": "Generate creative with AI tools", "href": "/ads/creatives/ai"},
        {"label": "Overlay Manager", "desc": "Manage ad overlays and stickers", "href": "/ads/creatives/overlay"},
    ],
))

write(f"{BASE}/audiences/page.tsx", list_page(
    "Audiences",
    "Create and manage reusable audiences — custom, lookalike, artist affinity, demographics.",
    ["Audience", "Type", "Size", "Status", "Last updated"],
    [
        ["Broad US 18-55", "Demographic", "~42M", "Ready", "Aug 10, 2026"],
        ["Custom — Past Purchasers", "Custom", "~12K", "Ready", "Aug 8, 2026"],
        ["Lookalike — Purchasers 1%", "Lookalike", "~2.1M", "Ready", "Aug 5, 2026"],
        ["Artist Affinity — EDM", "Artist Affinity", "~890K", "Ready", "Aug 1, 2026"],
        ["Exclude — Employees", "Exclusion", "~450", "Ready", "Jul 30, 2026"],
    ],
    "Create Audience", "/ads/audiences/create",
))

write(f"{BASE}/catalog/page.tsx", list_page(
    "Catalogs",
    "Manage product data for catalog ads — feeds, manual entry, Shopify sync.",
    ["Catalog", "Products", "Feed status", "Last synced", "Format"],
    [
        ["Main Product Catalog", "1,240", "Healthy", "2 hours ago", "DPA"],
        ["Holiday Collection", "86", "Healthy", "1 day ago", "Carousel"],
        ["Shopify Sync", "3,100", "Warning: 12 errors", "3 hours ago", "Shoppable"],
    ],
    "Import Feed", "/ads/catalog/feed",
))

write(f"{BASE}/inventory/page.tsx", card_page(
    "Placements & Inventory",
    "Understand availability and performance across all ad placements.",
    [
        {"label": "In-Feed Audio", "desc": "Audio ads between songs in user feeds", "href": "/ads/inventory/feed-audio"},
        {"label": "In-Feed Video", "desc": "Video ads in content feeds", "href": "/ads/inventory/feed-video"},
        {"label": "Top Feed", "desc": "Premium placement at top of feed", "href": "/ads/inventory/top-feed"},
        {"label": "Search Ads", "desc": "Ads in search results", "href": "/ads/inventory/search"},
        {"label": "Catalog Ads", "desc": "Product-based catalog placements", "href": "/ads/inventory/catalog"},
        {"label": "Automatic Placements", "desc": "Let the system optimize placement selection", "href": "/ads/inventory/automatic"},
    ],
))

# ═══════════════════════════════════════════════════════
# MEASURE
# ═══════════════════════════════════════════════════════

write(f"{BASE}/analytics/page.tsx", '''"use client";

export default function AnalyticsOverview() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Analytics Overview</h1>
        <p className="mt-1 text-sm text-neutral-500">Diagnose performance across campaigns, ad groups, ads, and audiences.</p>
      </div>

      {/* Breakdown selector */}
      <div className="mb-6 flex gap-2">
        {["Campaign", "Ad Group", "Ad", "Audience", "Creative", "Delivery"].map((view, i) => (
          <button key={view} className={`rounded-lg px-3 py-1.5 text-sm font-medium transition-colors ${i === 0 ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-600 hover:bg-neutral-50"}`}>{view}</button>
        ))}
      </div>

      {/* Metric scorecards */}
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-6">
        {[
          { label: "Spend", value: "$3,680" },
          { label: "Impressions", value: "142K" },
          { label: "Clicks", value: "1,824" },
          { label: "CTR", value: "1.28%" },
          { label: "CPA", value: "$19.78" },
          { label: "ROAS", value: "3.4x" },
        ].map((m) => (
          <div key={m.label} className="rounded-xl border border-neutral-100 bg-white p-4">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{m.label}</p>
            <p className="mt-1 text-xl font-bold text-neutral-900">{m.value}</p>
          </div>
        ))}
      </div>

      {/* Chart placeholder */}
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-4">Performance trend</h3>
        <div className="flex h-48 items-center justify-center text-sm text-neutral-400">
          Chart renders here — connect to analytics API
        </div>
      </div>
    </div>
  );
}
''')

write(f"{BASE}/analytics/reports/page.tsx", list_page(
    "Reports",
    "Create distributable performance reports. Custom columns, breakdowns, schedule.",
    ["Report", "Type", "Schedule", "Last run", "Status"],
    [
        ["Weekly Campaign Summary", "Scheduled", "Every Monday", "Aug 7, 2026", "Active"],
        ["Monthly ROAS Deep Dive", "Scheduled", "1st of month", "Aug 1, 2026", "Active"],
        ["Q2 Performance Report", "One-time", "—", "Jul 1, 2026", "Completed"],
    ],
    "Create Report", "/ads/analytics/reports/create",
))

write(f"{BASE}/analytics/attribution/page.tsx", page(
    "Attribution",
    "Evaluate contribution and outcomes. Compare attribution windows and conversion events.",
    '''      <div className="mb-6 grid grid-cols-3 gap-4">
        {[
          { label: "7-day click", value: "186 conversions" },
          { label: "1-day view", value: "42 conversions" },
          { label: "28-day click", value: "214 conversions" },
        ].map((w) => (
          <div key={w.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{w.label}</p>
            <p className="mt-2 text-xl font-bold text-neutral-900">{w.value}</p>
          </div>
        ))}
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-4">Conversion paths</h3>
        <div className="flex h-48 items-center justify-center text-sm text-neutral-400">Attribution path visualization</div>
      </div>'''
))

write(f"{BASE}/analytics/experiments/page.tsx", list_page(
    "Experiments",
    "Measure incremental impact with split tests and lift studies.",
    ["Experiment", "Type", "Status", "Confidence", "Duration"],
    [
        ["Budget A/B Test", "Split test", "Running", "72%", "Day 7 of 14"],
        ["Creative Lift Study", "Lift study", "Completed", "95%", "14 days"],
    ],
    "Create Experiment", "#",
))

write(f"{BASE}/analytics/audience-insights/page.tsx", '''"use client";

export default function AudienceInsightsPage() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Audience Insights</h1>
        <p className="mt-1 text-sm text-neutral-500">Learn who responds to your campaigns — age, gender, genre, artist affinity, location, language.</p>
      </div>
      <div className="grid grid-cols-2 gap-4 lg:grid-cols-3">
        {[
          { label: "Top Age", value: "25–34", pct: "38%" },
          { label: "Top Gender", value: "Female", pct: "56%" },
          { label: "Top Genre", value: "Pop", pct: "24%" },
          { label: "Top Artist", value: "Drake", pct: "12%" },
          { label: "Top Location", value: "California", pct: "18%" },
          { label: "Top Language", value: "English", pct: "89%" },
        ].map((s) => (
          <div key={s.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{s.label}</p>
            <p className="mt-2 text-xl font-bold text-neutral-900">{s.value}</p>
            <p className="mt-1 text-xs text-neutral-500">{s.pct} of audience</p>
          </div>
        ))}
      </div>
    </div>
  );
}
''')

write(f"{BASE}/analytics/video-audio-insights/page.tsx", page(
    "Video & Audio Insights",
    "Evaluate media-format engagement — video views, completion, streams, audio engagement, SVI.",
    '''      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        {[
          { label: "Video views", value: "28.4K" },
          { label: "Video completion", value: "67%" },
          { label: "Audio streams", value: "14.2K" },
          { label: "SVI", value: "1.8" },
        ].map((m) => (
          <div key={m.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{m.label}</p>
            <p className="mt-2 text-2xl font-bold text-neutral-900">{m.value}</p>
          </div>
        ))}
      </div>'''
))

# ═══════════════════════════════════════════════════════
# LEADS
# ═══════════════════════════════════════════════════════

write(f"{BASE}/leads/page.tsx", list_page(
    "Leads Center",
    "Filter, search, export, respond to, and qualify leads.",
    ["Lead", "Source", "Campaign", "Status", "Created", "Value"],
    [
        ["Sarah Chen", "Instant Form", "Summer Launch 2026", "New", "Aug 12, 2026", "$120"],
        ["Marcus Johnson", "Direct Message", "Brand Awareness Push", "Contacted", "Aug 11, 2026", "$85"],
        ["Emily Rodriguez", "Website Form", "Summer Launch 2026", "Qualified", "Aug 10, 2026", "$200"],
        ["David Kim", "Instant Form", "Summer Launch 2026", "New", "Aug 9, 2026", "$95"],
    ],
    "Export Leads", "/ads/leads/export",
))

write(f"{BASE}/leads/instant-forms/page.tsx", list_page(
    "Instant Forms",
    "Create and manage lead generation forms.",
    ["Form", "Leads", "Conversion rate", "Status", "Last updated"],
    [
        ["Summer Lead Form", "234", "8.2%", "Active", "Aug 10, 2026"],
        ["Newsletter Signup", "1,420", "12.4%", "Active", "Aug 1, 2026"],
        ["Demo Request", "56", "3.1%", "Paused", "Jul 15, 2026"],
    ],
    "Create Form", "#",
))

write(f"{BASE}/leads/direct-messages/page.tsx", page("Direct Messages", "Manage lead conversations via direct message."))

write(f"{BASE}/leads/inbox/page.tsx", page("Inbox", "Central inbox for all lead communications and conversations."))

write(f"{BASE}/leads/crm/page.tsx", card_page(
    "CRM Integrations",
    "Sync leads to your CRM system.",
    [
        {"label": "HubSpot", "desc": "Sync leads and contacts to HubSpot", "href": "#"},
        {"label": "Salesforce", "desc": "Push leads to Salesforce CRM", "href": "#"},
        {"label": "Zapier", "desc": "Connect to 5,000+ apps via Zapier", "href": "#"},
        {"label": "Custom Webhook", "desc": "Set up a custom webhook endpoint", "href": "#"},
    ],
))

write(f"{BASE}/leads/export/page.tsx", page("Export Leads", "Download leads as CSV or sync to CRM."))

# ═══════════════════════════════════════════════════════
# MANAGE
# ═══════════════════════════════════════════════════════

write(f"{BASE}/events/page.tsx", list_page(
    "Events Manager",
    "Configure conversion events and data sources for tracking.",
    ["Event", "Source", "Count (7d)", "Status", "Last received"],
    [
        ["Purchase", "Website pixel", "186", "Active", "2 min ago"],
        ["Add to Cart", "Website pixel", "412", "Active", "5 min ago"],
        ["Lead", "Instant Form", "234", "Active", "1 hour ago"],
        ["App Install", "SDK", "89", "Active", "3 hours ago"],
    ],
    "Add Event", "#",
))

write(f"{BASE}/rules/page.tsx", list_page(
    "Automated Rules",
    "Create rules that automatically adjust campaigns based on conditions.",
    ["Rule", "Condition", "Action", "Status", "Last triggered"],
    [
        ["Pause low CTR", "CTR < 0.5% for 3 days", "Pause ad group", "Active", "Aug 10, 2026"],
        ["Budget increase", "CPA < $10 and spend > 80%", "Increase budget 20%", "Active", "Aug 8, 2026"],
    ],
    "Create Rule", "#",
))

write(f"{BASE}/comments/page.tsx", page("Comments Manager", "Moderate and respond to comments on your ads and sponsored content."))

write(f"{BASE}/brand-safety/page.tsx", card_page(
    "Brand Safety",
    "Central policy and control center for brand safety and suitability.",
    [
        {"label": "Blocklists", "desc": "Manage content and publisher blocklists", "href": "#"},
        {"label": "Suitability", "desc": "Set brand suitability tiers and controls", "href": "#"},
        {"label": "Content controls", "desc": "Control what content your ads appear alongside", "href": "#"},
        {"label": "Inventory filter", "desc": "Filter available inventory by safety rating", "href": "#"},
    ],
))

write(f"{BASE}/integrations/page.tsx", card_page(
    "Integrations",
    "Manage external connections — pixels, SDKs, MMPs, and data partners.",
    [
        {"label": "Website Pixel", "desc": "Install and manage the Musicosy pixel", "href": "#"},
        {"label": "Mobile SDK", "desc": "Integrate the iOS/Android SDK", "href": "#"},
        {"label": "MMP Partners", "desc": "Connect measurement partners (AppsFlyer, Branch)", "href": "#"},
        {"label": "Data Partners", "desc": "Third-party data enrichment connections", "href": "#"},
        {"label": "CRM Sync", "desc": "Bidirectional CRM integrations", "href": "/ads/leads/crm"},
        {"label": "SSP / Exchange", "desc": "Programmatic exchange connections", "href": "#"},
    ],
))

write(f"{BASE}/ai/skills/page.tsx", card_page(
    "AI Skills & MCP",
    "AI-powered workflows, skills, and Model Context Protocol connections.",
    [
        {"label": "AI Dashboard", "desc": "Overview of AI-powered tools and usage", "href": "/ads/ai/skills/browse"},
        {"label": "Browse Skills", "desc": "Discover and install AI skills", "href": "/ads/ai/skills/browse"},
        {"label": "MCP Connections", "desc": "Manage Model Context Protocol endpoints", "href": "/ads/ai/skills/mcp"},
        {"label": "Search", "desc": "Search all AI skills and templates", "href": "/ads/ai/skills/search"},
    ],
))

# ═══════════════════════════════════════════════════════
# BILLING
# ═══════════════════════════════════════════════════════

write(f"{BASE}/billing/page.tsx", '''"use client";

export default function BillingOverview() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Billing Overview</h1>
        <p className="mt-1 text-sm text-neutral-500">Manage payment, invoices, and billing identity.</p>
      </div>
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        {[
          { label: "Account balance", value: "$4,320" },
          { label: "Current spend", value: "$3,680" },
          { label: "Next invoice", value: "Aug 15, 2026" },
          { label: "Payment method", value: "Visa ····4242" },
        ].map((kpi) => (
          <div key={kpi.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{kpi.label}</p>
            <p className="mt-2 text-2xl font-bold text-neutral-900">{kpi.value}</p>
          </div>
        ))}
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-4">Recent transactions</h3>
        <div className="flex h-32 items-center justify-center text-sm text-neutral-400">Transaction history loads here</div>
      </div>
    </div>
  );
}
''')

write(f"{BASE}/billing/payment-methods/page.tsx", list_page(
    "Payment Methods",
    "Manage credit cards, debit cards, and other payment methods.",
    ["Method", "Type", "Last 4", "Expiry", "Default"],
    [
        ["Visa ending 4242", "Credit card", "4242", "12/27", "Yes"],
        ["Mastercard ending 8888", "Credit card", "8888", "06/26", "No"],
    ],
    "Add Payment Method", "/ads/billing/payment-methods/add",
))

write(f"{BASE}/billing/payment-methods/add/page.tsx", page("Add Payment Method", "Securely add a new payment method.", '''      <div className="mx-auto max-w-lg rounded-xl border border-neutral-100 bg-white p-6">
        <div className="space-y-4">
          <div><label className="block text-sm font-medium text-neutral-700 mb-1">Card number</label><input placeholder="4242 4242 4242 4242" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
          <div className="grid grid-cols-2 gap-4">
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">Expiry</label><input placeholder="MM/YY" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">CVC</label><input placeholder="123" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
          </div>
          <div><label className="block text-sm font-medium text-neutral-700 mb-1">Billing address</label><input placeholder="123 Main St" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
        </div>
        <button className="mt-6 w-full rounded-lg bg-neutral-900 py-2.5 text-sm font-medium text-white">Add Payment Method</button>
      </div>'''))

write(f"{BASE}/billing/invoices/page.tsx", list_page(
    "Invoices",
    "View and download invoices.",
    ["Invoice", "Date", "Amount", "Status", "Due date"],
    [
        ["INV-2026-08", "Aug 1, 2026", "$3,680.00", "Paid", "Aug 15, 2026"],
        ["INV-2026-07", "Jul 1, 2026", "$2,140.00", "Paid", "Jul 15, 2026"],
        ["INV-2026-06", "Jun 1, 2026", "$1,890.00", "Paid", "Jun 15, 2026"],
    ],
))

write(f"{BASE}/billing/transactions/page.tsx", list_page(
    "Transactions",
    "Review payment history and billing events.",
    ["Transaction", "Type", "Amount", "Date", "Status"],
    [
        ["TXN-8924", "Charge", "$120.00", "Aug 12, 2026", "Completed"],
        ["TXN-8923", "Charge", "$95.00", "Aug 11, 2026", "Completed"],
        ["TXN-8922", "Refund", "$15.00", "Aug 10, 2026", "Completed"],
    ],
))

write(f"{BASE}/billing/tax/page.tsx", page("Taxes", "Manage tax information and billing address."))

write(f"{BASE}/billing/credits/page.tsx", list_page(
    "Credits & Promotions",
    "View ad credits, promotional offers, and rebates.",
    ["Credit", "Type", "Amount", "Expires", "Status"],
    [
        ["Welcome credit", "Promotional", "$500.00", "Dec 31, 2026", "Active"],
        ["Spend match Q3", "Match", "$250.00", "Sep 30, 2026", "Active"],
    ],
))

# ═══════════════════════════════════════════════════════
# SETTINGS
# ═══════════════════════════════════════════════════════

write(f"{BASE}/settings/account/page.tsx", '''"use client";

export default function AccountBusinessPage() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Account & Business</h1>
        <p className="mt-1 text-sm text-neutral-500">Manage your advertiser account and business information.</p>
      </div>
      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Business information</h3>
          <div className="grid gap-4 lg:grid-cols-2">
            <div><label className="block text-sm text-neutral-600 mb-1">Business name</label><input defaultValue="Acme Music Group" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Industry</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Music & Entertainment</option><option>Technology</option><option>Retail</option></select></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Country</label><input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Website</label><input defaultValue="https://acmemusic.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
          </div>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Advertiser account</h3>
          <div className="grid gap-4 lg:grid-cols-3">
            <div><label className="block text-sm text-neutral-600 mb-1">Account name</label><input defaultValue="Acme Ads" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Time zone</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>America/Chicago (CDT)</option></select></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Currency</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>USD</option><option>EUR</option><option>GBP</option></select></div>
          </div>
        </div>
        <div className="flex justify-end"><button className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white">Save</button></div>
      </div>
    </div>
  );
}
''')

write(f"{BASE}/settings/team/page.tsx", list_page(
    "Team & Permissions",
    "Invite members, manage roles, and control access levels.",
    ["Member", "Email", "Role", "Status", "Added"],
    [
        ["You", "you@acme.com", "Admin", "Active", "Jun 1, 2026"],
        ["Sarah Chen", "sarah@acme.com", "Editor", "Active", "Jul 15, 2026"],
        ["Marcus Johnson", "marcus@acme.com", "Viewer", "Pending", "Aug 10, 2026"],
    ],
    "Invite Member", "#",
))

write(f"{BASE}/settings/verification/page.tsx", card_page(
    "Verification",
    "Start or check the status of business verification.",
    [
        {"label": "Start Verification", "desc": "Begin the business verification process", "href": "#"},
        {"label": "Verification Status", "desc": "Check current verification status", "href": "#"},
        {"label": "Creator Engagement", "desc": "Eligibility for creator engagement features", "href": "#"},
        {"label": "Creator Payment", "desc": "Eligibility for creator payment features", "href": "#"},
    ],
))

write(f"{BASE}/settings/security/page.tsx", card_page(
    "Security & Documents",
    "Manage account security, uploaded documents, and compliance.",
    [
        {"label": "Two-Factor Auth", "desc": "Enable or manage 2FA settings", "href": "#"},
        {"label": "Sessions", "desc": "View and manage active sessions", "href": "#"},
        {"label": "Uploaded Documents", "desc": "Business licenses, tax forms, IDs", "href": "#"},
        {"label": "Audit Log", "desc": "Account activity and change history", "href": "#"},
    ],
))

write(f"{BASE}/settings/notifications/page.tsx", page("Notification Preferences", "Choose which notifications you receive and how."))

write(f"{BASE}/settings/targeting-defaults/page.tsx", page("Targeting Defaults", "Set account-level targeting defaults that pre-fill in the campaign builder."))

write(f"{BASE}/settings/api/page.tsx", page("API Access", "Manage API keys, webhooks, and developer access."))

# ═══════════════════════════════════════════════════════
# ONBOARDING
# ═══════════════════════════════════════════════════════

write(f"{BASE}/onboarding/page.tsx", '''"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

const steps = ["Intent", "Organization", "Business Info", "Account", "Verification", "Invite Members"];

export default function Onboarding() {
  const [step, setStep] = useState(0);
  const router = useRouter();
  const [intent, setIntent] = useState("");
  const [orgType, setOrgType] = useState("");

  return (
    <div className="mx-auto max-w-2xl">
      <div className="mb-8 text-center">
        <img src="/musicosy-orange-logo.webp" alt="Musicosy" className="mx-auto h-10 w-auto object-contain" />
        <h1 className="mt-4 text-2xl font-bold text-neutral-900">Set up your Ad Center</h1>
        <p className="mt-1 text-sm text-neutral-500">Step {step + 1} of {steps.length}</p>
      </div>

      {/* Progress bar */}
      <div className="mb-8 flex gap-1">
        {steps.map((_, i) => (
          <div key={i} className={`h-1 flex-1 rounded-full ${i <= step ? "bg-neutral-900" : "bg-neutral-200"}`} />
        ))}
      </div>

      {/* Step 0: Intent */}
      {step === 0 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">What do you want to do?</h2>
          <div className="space-y-3">
            {["Work with artists", "Grow my business"].map((opt) => (
              <button
                key={opt}
                onClick={() => setIntent(opt)}
                className={`w-full rounded-xl border p-4 text-left text-sm transition-colors ${intent === opt ? "border-neutral-900 bg-neutral-50 font-medium" : "border-neutral-200 hover:border-neutral-300"}`}
              >
                {opt}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Step 1: Organization type */}
      {step === 1 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Organization type</h2>
          <div className="space-y-3">
            {["Advertiser", "Agency"].map((opt) => (
              <button
                key={opt}
                onClick={() => setOrgType(opt)}
                className={`w-full rounded-xl border p-4 text-left text-sm transition-colors ${orgType === opt ? "border-neutral-900 bg-neutral-50 font-medium" : "border-neutral-200 hover:border-neutral-300"}`}
              >
                {opt}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Step 2: Business info */}
      {step === 2 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Business information</h2>
          <div className="space-y-4">
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">Business name</label><input className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">Industry</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>Music & Entertainment</option><option>Technology</option><option>Retail</option></select></div>
            <div className="grid grid-cols-2 gap-4">
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Country</label><input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Website</label><input placeholder="https://..." className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
            </div>
          </div>
        </div>
      )}

      {/* Step 3: Advertiser account */}
      {step === 3 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Advertiser account</h2>
          <div className="space-y-4">
            <div><label className="block text-sm font-medium text-neutral-700 mb-1">Account name</label><input className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
            <div className="grid grid-cols-2 gap-4">
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Time zone</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>America/Chicago</option><option>America/New_York</option><option>America/Los_Angeles</option></select></div>
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Currency</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>USD</option><option>EUR</option><option>GBP</option></select></div>
            </div>
          </div>
        </div>
      )}

      {/* Step 4: Verification */}
      {step === 4 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Business verification</h2>
          <p className="text-sm text-neutral-500 mb-4">Verification enables full ad delivery and payment features.</p>
          <div className="space-y-3">
            <div className="rounded-xl border border-neutral-200 p-4"><h3 className="text-sm font-medium text-neutral-900">Start verification</h3><p className="text-xs text-neutral-500">Submit business documents for review</p></div>
            <div className="rounded-xl border border-neutral-200 p-4"><h3 className="text-sm font-medium text-neutral-900">Creator engagement eligibility</h3><p className="text-xs text-neutral-500">Required for creator collaboration features</p></div>
            <div className="rounded-xl border border-neutral-200 p-4"><h3 className="text-sm font-medium text-neutral-900">Analytics eligibility</h3><p className="text-xs text-neutral-500">Access advanced measurement and insights</p></div>
          </div>
        </div>
      )}

      {/* Step 5: Invite members */}
      {step === 5 && (
        <div>
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Invite team members</h2>
          <p className="text-sm text-neutral-500 mb-4">Add collaborators to help manage your ad campaigns.</p>
          <div className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Email</label><input placeholder="colleague@company.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div>
              <div><label className="block text-sm font-medium text-neutral-700 mb-1">Role</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>Admin</option><option>Editor</option><option>Viewer</option></select></div>
            </div>
            <button className="text-sm font-medium text-neutral-600">+ Add another member</button>
          </div>
        </div>
      )}

      {/* Footer */}
      <div className="mt-8 flex items-center justify-between">
        <button onClick={() => step > 0 && setStep(step - 1)} className={`text-sm font-medium ${step > 0 ? "text-neutral-700" : "text-neutral-300"}`} disabled={step === 0}>Back</button>
        {step < steps.length - 1 ? (
          <button onClick={() => setStep(step + 1)} className="rounded-lg bg-neutral-900 px-6 py-2.5 text-sm font-medium text-white">Continue</button>
        ) : (
          <button onClick={() => router.push("/ads")} className="rounded-lg bg-neutral-900 px-6 py-2.5 text-sm font-medium text-white">Go to Ad Center</button>
        )}
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════
# DETAIL / SUB PAGES (minimal but functional)
# ═══════════════════════════════════════════════════════

# Audience detail
write(f"{BASE}/audiences/[id]/page.tsx", '''"use client";import { use } from "react";import Link from "next/link";export default function AudienceDetail({ params }: { params: Promise<{ id: string }> }) { const { id } = use(params); return <div><div className="mb-6"><div className="flex items-center gap-2 text-sm text-neutral-500"><Link href="/ads/audiences" className="hover:text-neutral-900">Audiences</Link><span>/</span><span className="text-neutral-900">Audience {id}</span></div><h1 className="mt-3 text-2xl font-bold tracking-tight text-neutral-900">Custom — Past Purchasers</h1><p className="mt-1 text-sm text-neutral-500">~12,000 members · Custom audience · Ready</p></div><div className="grid grid-cols-2 gap-4 lg:grid-cols-4">{[{label:"Size",value:"~12K"},{label:"Type",value:"Custom"},{label:"Lookalike",value:"1% — 2.1M"},{label:"Status",value:"Ready"}].map(m=><div key={m.label} className="rounded-xl border border-neutral-100 bg-white p-5"><p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{m.label}</p><p className="mt-2 text-xl font-bold text-neutral-900">{m.value}</p></div>)}</div></div>; }''')

# Audience create
write(f"{BASE}/audiences/create/page.tsx", page("Create Audience", "Build a new reusable audience.", '''      <div className="rounded-xl border border-neutral-100 bg-white p-6"><div className="space-y-4"><div><label className="block text-sm font-medium text-neutral-700 mb-1">Audience name</label><input placeholder="e.g. Past Purchasers" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900" /></div><div><label className="block text-sm font-medium text-neutral-700 mb-1">Type</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900"><option>Custom</option><option>Lookalike</option><option>Artist Affinity</option><option>Demographic</option></select></div></div><div className="mt-6 flex justify-end gap-3"><button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700">Cancel</button><button className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white">Create</button></div></div>'''))

# Inventory sub-pages
for inv in ["feed-audio", "feed-video", "top-feed", "search", "catalog", "automatic", "performance"]:
    title = inv.replace("-", " ").title()
    write(f"{BASE}/inventory/{inv}/page.tsx", page(f"{title} Inventory", f"Performance and availability for {title.lower()} placements."))

# Analytics sub-pages
for sub in ["reports/create", "reports/export", "reports/schedule"]:
    title = sub.split("/")[-1].title()
    write(f"{BASE}/analytics/{sub}/page.tsx", page(f"{title} Report", f"Configure {title.lower()} report settings."))

# Creative sub-pages
for sub in ["audio", "companion", "logo", "cta", "destination", "preview", "overlay"]:
    title = sub.title()
    write(f"{BASE}/creatives/{sub}/page.tsx", page(f"{title}", f"Manage {title.lower()} creative assets."))

write(f"{BASE}/creatives/ai/page.tsx", card_page("AI Creative Tools", "Generate creative with AI.", [
    {"label": "Video Generator", "desc": "AI-powered video ad creation", "href": "/ads/creatives/ai/video"},
    {"label": "Voiceover", "desc": "AI voiceover generation", "href": "/ads/creatives/ai/voiceover"},
    {"label": "Music", "desc": "AI music and audio generation", "href": "/ads/creatives/ai/music"},
    {"label": "Script Writer", "desc": "AI ad script generation", "href": "/ads/creatives/ai/script"},
    {"label": "Templates", "desc": "AI template recommendations", "href": "/ads/creatives/ai/templates"},
]))

for ai_sub in ["video", "voiceover", "music", "script", "templates"]:
    write(f"{BASE}/creatives/ai/{ai_sub}/page.tsx", page(f"AI {ai_sub.title()}", f"AI-powered {ai_sub} generation tools."))

# AI Skills sub-pages
for skill_sub in ["browse", "search", "mcp"]:
    write(f"{BASE}/ai/skills/{skill_sub}/page.tsx", page(f"AI Skills — {skill_sub.title()}", f"Browse, search, and manage AI skills and MCP connections."))

# Catalog sub-pages
for cat_sub in ["feed", "manual", "shopify", "storefront"]:
    write(f"{BASE}/catalog/{cat_sub}/page.tsx", page(f"Catalog — {cat_sub.title()}", f"Manage {cat_sub} catalog source."))

write(f"{BASE}/catalog/formats/page.tsx", card_page("Catalog Formats", "Choose a catalog ad format.", [
    {"label": "Carousel", "desc": "Swipeable product carousel", "href": "/ads/catalog/formats/carousel"},
    {"label": "Shoppable", "desc": "Directly shoppable product cards", "href": "/ads/catalog/formats/shoppable"},
    {"label": "Product Showcase", "desc": "Single product highlight", "href": "/ads/catalog/formats/product-showcase"},
]))

for fmt in ["carousel", "shoppable", "product-showcase"]:
    write(f"{BASE}/catalog/formats/{fmt}/page.tsx", page(f"Catalog — {fmt.title()}", f"Configure {fmt} format catalog ads."))

write(f"{BASE}/catalog/products/page.tsx", list_page("Products", "Manage products in your catalog.", ["Product", "Price", "Availability", "Category", "Last updated"], [
    ["Premium Headphones", "$299.99", "In stock", "Electronics", "Aug 10, 2026"],
    ["Wireless Earbuds", "$79.99", "In stock", "Electronics", "Aug 8, 2026"],
    ["Concert Tee", "$34.99", "In stock", "Merch", "Aug 5, 2026"],
]))

# Events sub-pages
write(f"{BASE}/events/data-sources/page.tsx", card_page("Data Sources", "Configure event data sources.", [
    {"label": "Website Pixel", "desc": "Track events from your website", "href": "/ads/events/data-sources/website"},
    {"label": "App SDK", "desc": "Track events from your mobile app", "href": "/ads/events/data-sources/app"},
    {"label": "Shop", "desc": "Track Musicosy shop events", "href": "/ads/events/data-sources/shop"},
    {"label": "CRM", "desc": "Import offline conversion data", "href": "/ads/events/data-sources/crm"},
]))

for ds in ["website", "app", "shop", "crm"]:
    write(f"{BASE}/events/data-sources/{ds}/page.tsx", page(f"Data Source — {ds.title()}", f"Configure {ds} event data source."))

write(f"{BASE}/events/customization/page.tsx", page("Event Customization", "Customize event parameters and rules."))
write(f"{BASE}/events/partners/page.tsx", page("Event Partners", "Manage measurement and data partners."))

# Billing sub-pages that might still be stubs
write(f"{BASE}/billing/rebates/page.tsx", page("Rebates", "View rebate history and eligibility."))
write(f"{BASE}/billing/settings/page.tsx", page("Billing Settings", "Configure billing preferences and auto-recharge."))
write(f"{BASE}/billing/invoices/[id]/page.tsx", '''"use client";import { use } from "react";export default function InvoiceDetail({ params }: { params: Promise<{ id: string }> }) { const { id } = use(params); return <div><h1 className="text-2xl font-bold tracking-tight text-neutral-900">Invoice {id}</h1><p className="mt-1 text-sm text-neutral-500">View invoice details and download PDF.</p></div>; }''')

# Leads sub-pages
write(f"{BASE}/leads/[id]/page.tsx", '''"use client";import { use } from "react";import Link from "next/link";export default function LeadDetail({ params }: { params: Promise<{ id: string }> }) { const { id } = use(params); return <div><div className="flex items-center gap-2 text-sm text-neutral-500"><Link href="/ads/leads" className="hover:text-neutral-900">Leads</Link><span>/</span><span className="text-neutral-900">Lead {id}</span></div><h1 className="mt-3 text-2xl font-bold tracking-tight text-neutral-900">Sarah Chen</h1><p className="mt-1 text-sm text-neutral-500">New · Instant Form · Summer Launch 2026</p></div>; }''')
write(f"{BASE}/leads/message-assistant/page.tsx", page("Message Assistant", "AI-powered lead response assistant."))
write(f"{BASE}/leads/website-forms/page.tsx", page("Website Forms", "Manage website lead capture forms."))
write(f"{BASE}/leads/filter/page.tsx", page("Filter Leads", "Apply filters to narrow down leads."))

# Campaign action pages
write(f"{BASE}/campaigns/[id]/duplicate/page.tsx", page("Duplicate Campaign", "Create a copy of this campaign."))
write(f"{BASE}/campaigns/[id]/pause/page.tsx", page("Pause Campaign", "Pause delivery for this campaign."))
write(f"{BASE}/campaigns/[id]/resume/page.tsx", page("Resume Campaign", "Resume delivery for this paused campaign."))
write(f"{BASE}/campaigns/[id]/delete/page.tsx", page("Delete Campaign", "Permanently delete this campaign."))

# Team sub-pages
write(f"{BASE}/account/team/page.tsx", list_page("Team", "Manage team members and roles.", ["Member", "Role", "Status"], [["You", "Admin", "Active"]], "Invite", "#"))

# Other missing pages for old routes that might still be hit
write(f"{BASE}/account/page.tsx", page("Account", "Account settings and profile."))
write(f"{BASE}/account/health/page.tsx", page("Account Health", "Monitor account health and delivery status."))
write(f"{BASE}/account/brand-safety/page.tsx", page("Brand Safety Settings", "Account-level brand safety configuration."))
write(f"{BASE}/account/documents/page.tsx", page("Documents", "Uploaded business documents and IDs."))
write(f"{BASE}/account/verification/page.tsx", page("Verification", "Business verification status and process."))
write(f"{BASE}/account/notifications/page.tsx", page("Account Notifications", "Notification settings for this account."))
write(f"{BASE}/account/profile/page.tsx", page("Profile", "Manage your advertiser profile."))
write(f"{BASE}/account/tiers/page.tsx", page("Account Tiers", "View and manage account tier and limits."))
write(f"{BASE}/account/targeting/page.tsx", page("Targeting Defaults", "Account-level targeting defaults."))
write(f"{BASE}/settings/page.tsx", card_page("Settings", "Ad Center settings.", [
    {"label": "Account & Business", "desc": "Business info, account settings", "href": "/ads/settings/account"},
    {"label": "Team & Permissions", "desc": "Invite members, manage roles", "href": "/ads/settings/team"},
    {"label": "Verification", "desc": "Business verification", "href": "/ads/settings/verification"},
    {"label": "Security & Documents", "desc": "2FA, sessions, documents", "href": "/ads/settings/security"},
    {"label": "Notification Preferences", "desc": "Choose what notifications you receive", "href": "/ads/settings/notifications"},
    {"label": "Targeting Defaults", "desc": "Pre-fill targeting in campaign builder", "href": "/ads/settings/targeting-defaults"},
    {"label": "API Access", "desc": "API keys, webhooks, developer access", "href": "/ads/settings/api"},
]))

# Exchange (accessible via Integrations, not sidebar)
write(f"{BASE}/exchange/page.tsx", card_page("Exchange", "Programmatic exchange connections.", [
    {"label": "Open Auction", "desc": "Open auction inventory", "href": "/ads/exchange/open-auction"},
    {"label": "PMP", "desc": "Private marketplace deals", "href": "/ads/exchange/pmp"},
    {"label": "Programmatic Guaranteed", "desc": "Guaranteed delivery deals", "href": "/ads/exchange/programmatic-guaranteed"},
    {"label": "Partners", "desc": "Connected DSPs and SSPs", "href": "/ads/exchange/partners"},
]))

for ex in ["open-auction", "pmp", "programmatic-guaranteed", "partners", "openrtb", "daast", "vaast", "reconciliation"]:
    write(f"{BASE}/exchange/{ex}/page.tsx", page(f"Exchange — {ex.replace('-', ' ').title()}", f"Configure {ex.replace('-', ' ')} exchange settings."))

# Agency
write(f"{BASE}/agency/page.tsx", page("Agency", "Agency workspace for managing clients and cross-client reporting."))

print("\n✅ All Ad Center pages generated!")
