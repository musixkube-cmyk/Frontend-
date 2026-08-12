#!/usr/bin/env python3
"""Generate all missing Ad Center page.tsx files."""

import os
from pathlib import Path

BASE = Path("/home/z/my-project/src/app/ads")

# ─── Track stats ───
created = 0
skipped = 0
errors = []

def write_page(route: str, content: str):
    """Write a page.tsx at the given route under BASE. Skip if exists."""
    global created, skipped, errors
    dir_path = BASE / route
    file_path = dir_path / "page.tsx"
    try:
        if file_path.exists():
            skipped += 1
            return
        dir_path.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        created += 1
    except Exception as e:
        errors.append(f"{route}: {e}")


# ═══════════════════════════════════════════════════════════════════════════
# 1. /ads/ads-manager/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("ads-manager", '''"use client";

import { PageHeader, CardGrid, MetricCard } from "@/components/ads/ui";

export default function AdsManagerPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Ads Manager"
        description="Launch campaigns, manage resources, monitor data, and optimize performance."
      />

      <div className="mb-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <MetricCard label="Active Campaigns" value="24" delta="+3 this week" deltaType="positive" />
        <MetricCard label="Total Spend" value="$12,840" delta="$2,100 today" deltaType="neutral" prefix="$" />
        <MetricCard label="Impressions" value="1.2M" delta="+12% vs last period" deltaType="positive" />
        <MetricCard label="Avg. CPM" value="$10.70" delta="-0.5% vs last period" deltaType="positive" prefix="$" />
      </div>

      <h2 className="mb-4 text-lg font-semibold text-neutral-900">Quick Actions</h2>
      <CardGrid
        cards={[
          { label: "Campaigns", description: "View, create, and manage all your advertising campaigns", href: "/ads/ads-manager/campaigns" },
          { label: "Ad Groups", description: "Organize your ads by audience, placement, and targeting", href: "/ads/ads-manager/ad-groups" },
          { label: "Ads", description: "Manage individual ad creatives and their configurations", href: "/ads/ads-manager/ads" },
          { label: "Monitor", description: "Track delivery health, spend pacing, and performance alerts", href: "/ads/ads-manager/monitor" },
          { label: "Optimize", description: "Get budget, audience, placement, and creative recommendations", href: "/ads/ads-manager/optimize" },
          { label: "Create Campaign", description: "Launch a new campaign with the guided 7-step wizard", href: "/ads/ads-manager/campaigns/create" },
        ]}
      />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 2. /ads/ads-manager/campaigns/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("ads-manager/campaigns", '''"use client";

import { useState } from "react";
import { PageHeader, FilterBar, DataTable, StatusBadge, Button, BulkActionToolbar } from "@/components/ads/ui";

const campaigns = [
  { id: "c1", name: "Summer Launch 2025", objective: "Traffic", status: "active" as const, budget: "$5,000", spend: "$3,210", impressions: "428K", clicks: "12.4K", ctr: "2.9%" },
  { id: "c2", name: "Brand Awareness Q2", objective: "Reach", status: "active" as const, budget: "$10,000", spend: "$7,840", impressions: "1.2M", clicks: "8.1K", ctr: "0.7%" },
  { id: "c3", name: "New Artist Promo", objective: "Video Views", status: "paused" as const, budget: "$2,500", spend: "$1,100", impressions: "89K", clicks: "3.2K", ctr: "3.6%" },
  { id: "c4", name: "Holiday Retargeting", objective: "Sales", status: "draft" as const, budget: "$8,000", spend: "$0", impressions: "—", clicks: "—", ctr: "—" },
  { id: "c5", name: "Podcast Discovery", objective: "Music Streams", status: "active" as const, budget: "$3,000", spend: "$2,490", impressions: "310K", clicks: "9.7K", ctr: "3.1%" },
  { id: "c6", name: "Lead Gen - Newsletter", objective: "Lead Generation", status: "in_review" as const, budget: "$1,500", spend: "$0", impressions: "—", clicks: "—", ctr: "—" },
];

const columns = [
  { key: "name", label: "Campaign" },
  { key: "objective", label: "Objective" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "budget", label: "Budget" },
  { key: "spend", label: "Spend" },
  { key: "impressions", label: "Impressions" },
  { key: "clicks", label: "Clicks" },
  { key: "ctr", label: "CTR" },
];

export default function CampaignsPage() {
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState("");

  const filtered = campaigns.filter((c) =>
    c.name.toLowerCase().includes(search.toLowerCase())
  );

  const toggleSelect = (id: string) => {
    const next = new Set(selected);
    next.has(id) ? next.delete(id) : next.add(id);
    setSelected(next);
  };

  const toggleAll = () => {
    if (selected.size === filtered.length) {
      setSelected(new Set());
    } else {
      setSelected(new Set(filtered.map((c) => c.id)));
    }
  };

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Campaigns"
        description="View and manage all your advertising campaigns."
        breadcrumbs={[{ label: "Ads Manager", href: "/ads/ads-manager" }, { label: "Campaigns" }]}
        actions={
          <Button onClick={() => window.location.href = "/ads/ads-manager/campaigns/create"}>
            + Create Campaign
          </Button>
        }
      />

      <FilterBar
        searchPlaceholder="Search campaigns…"
        onSearch={setSearch}
        filters={[
          { label: "Status", options: ["Active", "Paused", "Draft", "In Review"] },
          { label: "Objective", options: ["Reach", "Traffic", "Video Views", "Sales", "Music Streams", "Lead Generation"] },
        ]}
      />

      <BulkActionToolbar
        selectedCount={selected.size}
        actions={[
          { label: "Pause", onClick: () => {} },
          { label: "Resume", onClick: () => {} },
          { label: "Duplicate", onClick: () => {} },
          { label: "Delete", onClick: () => {}, variant: "danger" },
        ]}
      />

      <DataTable
        columns={columns}
        data={filtered}
        selectable
        selected={selected}
        onToggleSelect={toggleSelect}
        onToggleAll={toggleAll}
        rowHref={(row) => `/ads/campaigns/${row.id}`}
      />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 3. /ads/ads-manager/campaigns/create/page.tsx - 7-step wizard
# ═══════════════════════════════════════════════════════════════════════════
write_page("ads-manager/campaigns/create", '''"use client";

import { useState } from "react";
import { PageHeader, Button, FormField, EstimatePanel } from "@/components/ads/ui";

const STEPS = [
  "Creation Method",
  "Objectives",
  "Campaign Setup",
  "Plan & Commitment",
  "Ad Group Setup",
  "Create Ad",
  "Review & Launch",
];

export default function CreateCampaignPage() {
  const [step, setStep] = useState(0);
  const [method, setMethod] = useState("guided");
  const [objective, setObjective] = useState("");
  const [campaignName, setCampaignName] = useState("");
  const [specialCategory, setSpecialCategory] = useState("none");
  const [splitTest, setSplitTest] = useState(false);
  const [plan, setPlan] = useState("standard");
  const [cbo, setCbo] = useState(true);
  const [budget, setBudget] = useState("5000");
  const [budgetPeriod, setBudgetPeriod] = useState("daily");
  const [budgetStrategy, setBudgetStrategy] = useState("maximize");
  const [selectedCreative, setSelectedCreative] = useState("");
  const [cta, setCta] = useState("Learn More");
  const [destinationUrl, setDestinationUrl] = useState("");

  return (
    <div className="mx-auto max-w-4xl p-6">
      <PageHeader
        title="Create Campaign"
        description={`Step ${step + 1} of 7 — ${STEPS[step]}`}
        breadcrumbs={[{ label: "Ads Manager", href: "/ads/ads-manager" }, { label: "Campaigns", href: "/ads/ads-manager/campaigns" }, { label: "Create" }]}
      />

      {/* Step indicator */}
      <div className="mb-8 flex items-center gap-1">
        {STEPS.map((s, i) => (
          <div key={s} className="flex items-center gap-1">
            <div className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-semibold ${
              i === step ? "bg-neutral-900 text-white" : i < step ? "bg-emerald-500 text-white" : "bg-neutral-100 text-neutral-400"
            }`}>
              {i + 1}
            </div>
            {i < STEPS.length - 1 && <div className={`h-0.5 w-6 ${i < step ? "bg-emerald-500" : "bg-neutral-100"}`} />}
          </div>
        ))}
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        {/* Step 1: Creation Method */}
        {step === 0 && (
          <div>
            <h2 className="text-lg font-semibold text-neutral-900 mb-4">Choose how to create your campaign</h2>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
              {[
                { id: "guided", label: "Guided Setup", desc: "Step-by-step wizard with recommendations and best practices" },
                { id: "quick", label: "Quick Create", desc: "Fast setup with essential fields only — perfect for experienced advertisers" },
                { id: "import", label: "Import", desc: "Import settings from an existing campaign or CSV file" },
              ].map((m) => (
                <button
                  key={m.id}
                  onClick={() => setMethod(m.id)}
                  className={`rounded-xl border-2 p-5 text-left transition-colors ${
                    method === m.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100 hover:border-neutral-200"
                  }`}
                >
                  <h3 className="text-sm font-semibold text-neutral-900">{m.label}</h3>
                  <p className="mt-1 text-xs text-neutral-500">{m.desc}</p>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Step 2: Objectives */}
        {step === 1 && (
          <div>
            <h2 className="text-lg font-semibold text-neutral-900 mb-4">Select your advertising objective</h2>
            <div className="space-y-6">
              {/* Awareness */}
              <div>
                <h3 className="text-sm font-semibold text-neutral-700 mb-2">Awareness</h3>
                <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                  <button onClick={() => setObjective("reach")} className={`rounded-lg border p-4 text-left ${objective === "reach" ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                    <h4 className="text-sm font-medium text-neutral-900">Reach</h4>
                    <p className="text-xs text-neutral-500">Show your ad to the maximum number of people</p>
                  </button>
                </div>
              </div>
              {/* Consideration */}
              <div>
                <h3 className="text-sm font-semibold text-neutral-700 mb-2">Consideration</h3>
                <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
                  {[
                    { id: "traffic", label: "Traffic", desc: "Drive clicks to your website or app" },
                    { id: "video-views", label: "Video Views", desc: "Maximize video views and engagement" },
                    { id: "community", label: "Community Interaction", desc: "Grow followers and engagement" },
                    { id: "brand-consideration", label: "Brand Consideration", desc: "Increase brand recall and favorability" },
                    { id: "music-streams", label: "Music Streams", desc: "Drive streams on the music platform" },
                  ].map((o) => (
                    <button key={o.id} onClick={() => setObjective(o.id)} className={`rounded-lg border p-4 text-left ${objective === o.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                      <h4 className="text-sm font-medium text-neutral-900">{o.label}</h4>
                      <p className="text-xs text-neutral-500">{o.desc}</p>
                    </button>
                  ))}
                </div>
              </div>
              {/* Conversion */}
              <div>
                <h3 className="text-sm font-semibold text-neutral-700 mb-2">Conversion</h3>
                <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
                  {[
                    { id: "app-promotion", label: "App Promotion", desc: "Drive app installs and engagement" },
                    { id: "lead-gen", label: "Lead Generation", desc: "Collect leads with instant forms" },
                    { id: "sales", label: "Sales", desc: "Drive purchases and conversions" },
                  ].map((o) => (
                    <button key={o.id} onClick={() => setObjective(o.id)} className={`rounded-lg border p-4 text-left ${objective === o.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                      <h4 className="text-sm font-medium text-neutral-900">{o.label}</h4>
                      <p className="text-xs text-neutral-500">{o.desc}</p>
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Step 3: Campaign Setup */}
        {step === 2 && (
          <div className="space-y-5">
            <h2 className="text-lg font-semibold text-neutral-900">Campaign Setup</h2>
            <FormField label="Campaign Name" description="A descriptive name to identify this campaign">
              <input value={campaignName} onChange={(e) => setCampaignName(e.target.value)} placeholder="e.g., Summer Launch 2025" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
            </FormField>
            <FormField label="Special Ad Category" description="Required for ads about credit, employment, housing, or social issues">
              <select value={specialCategory} onChange={(e) => setSpecialCategory(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option value="none">None</option>
                <option value="credit">Credit</option>
                <option value="employment">Employment</option>
                <option value="housing">Housing</option>
                <option value="social">Social Issues</option>
              </select>
            </FormField>
            <div className="flex items-center gap-3">
              <label className="text-sm font-medium text-neutral-700">Enable Split Test (A/B)</label>
              <button onClick={() => setSplitTest(!splitTest)} className={`relative inline-flex h-5 w-9 shrink-0 rounded-full border-2 border-transparent transition-colors ${splitTest ? "bg-emerald-500" : "bg-neutral-200"}`}>
                <span className={`pointer-events-none inline-block h-4 w-4 rounded-full bg-white shadow transition-transform ${splitTest ? "translate-x-4" : "translate-x-0"}`} />
              </button>
            </div>
            {splitTest && (
              <div className="rounded-lg border border-neutral-100 bg-neutral-50 p-4 text-sm text-neutral-600">
                Split test enabled. Your campaign will create two ad sets with different variables to test performance.
              </div>
            )}
          </div>
        )}

        {/* Step 4: Plan & Commitment */}
        {step === 3 && (
          <div className="space-y-5">
            <h2 className="text-lg font-semibold text-neutral-900">Plan, Budget & Commitment</h2>
            <FormField label="Plan Selection">
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
                {[
                  { id: "standard", label: "Standard", desc: "Pay per impression, full flexibility" },
                  { id: "committed", label: "Committed", desc: "Volume commitment with CPM discounts" },
                  { id: "premium", label: "Premium", desc: "Guaranteed delivery with priority access" },
                ].map((p) => (
                  <button key={p.id} onClick={() => setPlan(p.id)} className={`rounded-lg border-2 p-4 text-left ${plan === p.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                    <h4 className="text-sm font-semibold text-neutral-900">{p.label}</h4>
                    <p className="text-xs text-neutral-500">{p.desc}</p>
                  </button>
                ))}
              </div>
            </FormField>
            <div className="flex items-center gap-3">
              <label className="text-sm font-medium text-neutral-700">Campaign Budget Optimization (CBO)</label>
              <button onClick={() => setCbo(!cbo)} className={`relative inline-flex h-5 w-9 shrink-0 rounded-full border-2 border-transparent transition-colors ${cbo ? "bg-emerald-500" : "bg-neutral-200"}`}>
                <span className={`pointer-events-none inline-block h-4 w-4 rounded-full bg-white shadow transition-transform ${cbo ? "translate-x-4" : "translate-x-0"}`} />
              </button>
              <span className="text-xs text-neutral-500">Distribute budget across ad groups automatically</span>
            </div>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
              <FormField label="Budget Amount">
                <div className="relative">
                  <span className="absolute left-3 top-1/2 -translate-y-1/2 text-sm text-neutral-400">$</span>
                  <input value={budget} onChange={(e) => setBudget(e.target.value)} type="number" className="w-full rounded-lg border border-neutral-200 py-2 pl-7 pr-3 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
              </FormField>
              <FormField label="Budget Allocation">
                <select value={budgetPeriod} onChange={(e) => setBudgetPeriod(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option value="daily">Daily</option>
                  <option value="weekly">Weekly</option>
                  <option value="monthly">Monthly</option>
                  <option value="lifetime">Lifetime</option>
                </select>
              </FormField>
              <FormField label="Budget Strategy">
                <select value={budgetStrategy} onChange={(e) => setBudgetStrategy(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option value="maximize">Maximize Results</option>
                  <option value="target-cpa">Target CPA</option>
                  <option value="target-roas">Target ROAS</option>
                  <option value="bid-cap">Bid Cap</option>
                </select>
              </FormField>
            </div>
            <EstimatePanel
              estimates={[
                { label: "Estimated Impressions", value: "640K – 850K" },
                { label: "Estimated Clicks", value: "18K – 25K" },
                { label: "Estimated CPM", value: "$7.50 – $9.80" },
              ]}
              deliveryLikelihood={87}
            />
          </div>
        )}

        {/* Step 5: Ad Group Setup */}
        {step === 4 && (
          <div className="space-y-5">
            <h2 className="text-lg font-semibold text-neutral-900">Ad Group Setup</h2>
            <FormField label="Placements" description="Choose where your ads will appear">
              <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
                {["Home Feed", "Search Results", "Artist Page", "Playlist", "Podcast", "Radio", "Video", "Stories"].map((p) => (
                  <label key={p} className="flex items-center gap-2 rounded-lg border border-neutral-100 px-3 py-2 text-sm text-neutral-700 hover:bg-neutral-50">
                    <input type="checkbox" defaultChecked={["Home Feed", "Search Results"].includes(p)} className="h-4 w-4 rounded border-neutral-300" />
                    {p}
                  </label>
                ))}
              </div>
            </FormField>
            <FormField label="Audience Targeting">
              <div className="flex flex-wrap gap-2">
                {["Age 18-34", "Music Enthusiasts", "US Only", "English"].map((t) => (
                  <span key={t} className="inline-flex items-center gap-1 rounded-full bg-neutral-100 px-3 py-1 text-xs font-medium text-neutral-700">
                    {t}
                    <button className="text-neutral-400 hover:text-neutral-600">×</button>
                  </span>
                ))}
                <button className="rounded-full border border-dashed border-neutral-300 px-3 py-1 text-xs text-neutral-500 hover:border-neutral-400">
                  + Add targeting
                </button>
              </div>
            </FormField>
            <FormField label="Bidding Strategy">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>Automatic — Maximize results</option>
                <option>Manual CPM</option>
                <option>Target CPA</option>
                <option>Target ROAS</option>
              </select>
            </FormField>
            <FormField label="Frequency Capping" description="Limit how often a user sees your ad">
              <div className="flex items-center gap-2">
                <input type="number" defaultValue={3} className="w-20 rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                <span className="text-sm text-neutral-500">impressions per</span>
                <select className="rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>day</option>
                  <option>week</option>
                  <option>month</option>
                </select>
              </div>
            </FormField>
            <FormField label="Brand Safety">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>Standard — Block sensitive content</option>
                <option>Strict — Block more categories</option>
                <option>Limited — Maximum brand safety</option>
              </select>
            </FormField>
          </div>
        )}

        {/* Step 6: Create Ad */}
        {step === 5 && (
          <div className="space-y-5">
            <h2 className="text-lg font-semibold text-neutral-900">Create Your Ad</h2>
            <FormField label="Creative">
              <div className="flex items-start gap-3">
                <select value={selectedCreative} onChange={(e) => setSelectedCreative(e.target.value)} className="flex-1 rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option value="">Select an existing creative…</option>
                  <option value="audio-1">Summer Anthem — Audio Ad</option>
                  <option value="video-1">Brand Story — Video Ad</option>
                  <option value="display-1">New Release — Display Ad</option>
                </select>
                <Button variant="secondary" onClick={() => {}}>+ Create New</Button>
              </div>
            </FormField>
            <FormField label="Call-to-Action (CTA)">
              <select value={cta} onChange={(e) => setCta(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                {["Learn More", "Shop Now", "Listen Now", "Download", "Sign Up", "Watch More", "Get Offer", "Contact Us"].map((c) => (
                  <option key={c} value={c}>{c}</option>
                ))}
              </select>
            </FormField>
            <FormField label="Destination URL">
              <input value={destinationUrl} onChange={(e) => setDestinationUrl(e.target.value)} placeholder="https://example.com/landing" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
            </FormField>
            <div className="rounded-xl border border-neutral-100 bg-neutral-50 p-6 text-center">
              <p className="text-sm text-neutral-500">Ad Preview</p>
              <div className="mt-4 mx-auto max-w-sm rounded-lg border border-neutral-200 bg-white p-4">
                <div className="h-24 rounded bg-neutral-100 flex items-center justify-center text-xs text-neutral-400">Creative Preview</div>
                <p className="mt-2 text-sm font-medium text-neutral-900">{campaignName || "Your Campaign"}</p>
                <p className="text-xs text-neutral-500 mt-0.5">{cta}</p>
                <p className="text-xs text-neutral-400 mt-0.5 truncate">{destinationUrl || "https://example.com"}</p>
              </div>
            </div>
          </div>
        )}

        {/* Step 7: Review & Launch */}
        {step === 6 && (
          <div className="space-y-5">
            <h2 className="text-lg font-semibold text-neutral-900">Review & Launch</h2>
            <div className="rounded-xl border border-neutral-100 bg-white p-5 space-y-3">
              <h3 className="text-sm font-semibold text-neutral-900">Campaign Summary</h3>
              <div className="grid grid-cols-2 gap-3 text-sm">
                <div><span className="text-neutral-500">Name:</span> <span className="font-medium text-neutral-900">{campaignName || "Untitled Campaign"}</span></div>
                <div><span className="text-neutral-500">Method:</span> <span className="font-medium text-neutral-900 capitalize">{method}</span></div>
                <div><span className="text-neutral-500">Objective:</span> <span className="font-medium text-neutral-900">{objective || "Not selected"}</span></div>
                <div><span className="text-neutral-500">Special Category:</span> <span className="font-medium text-neutral-900">{specialCategory}</span></div>
                <div><span className="text-neutral-500">Plan:</span> <span className="font-medium text-neutral-900 capitalize">{plan}</span></div>
                <div><span className="text-neutral-500">Budget:</span> <span className="font-medium text-neutral-900">${budget} {budgetPeriod}</span></div>
                <div><span className="text-neutral-500">CBO:</span> <span className="font-medium text-neutral-900">{cbo ? "On" : "Off"}</span></div>
                <div><span className="text-neutral-500">Split Test:</span> <span className="font-medium text-neutral-900">{splitTest ? "On" : "Off"}</span></div>
                <div><span className="text-neutral-500">CTA:</span> <span className="font-medium text-neutral-900">{cta}</span></div>
                <div><span className="text-neutral-500">Destination:</span> <span className="font-medium text-neutral-900 truncate block">{destinationUrl || "—"}</span></div>
              </div>
            </div>
            <div className="flex flex-wrap items-center gap-3 pt-4">
              <Button variant="secondary" onClick={() => {}}>Save as Draft</Button>
              <Button variant="secondary" onClick={() => {}}>Submit Action Request</Button>
              <Button onClick={() => {}}>Launch Campaign</Button>
            </div>
          </div>
        )}
      </div>

      {/* Navigation */}
      <div className="mt-6 flex items-center justify-between">
        <Button variant="ghost" onClick={() => setStep(Math.max(0, step - 1))} disabled={step === 0}>
          Back
        </Button>
        {step < STEPS.length - 1 ? (
          <Button onClick={() => setStep(Math.min(STEPS.length - 1, step + 1))} disabled={step === 1 && !objective}>
            Continue
          </Button>
        ) : (
          <Button onClick={() => window.location.href = "/ads/ads-manager/campaigns"}>
            Done
          </Button>
        )}
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 4. /ads/ads-manager/ad-groups/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("ads-manager/ad-groups", '''"use client";

import { useState } from "react";
import { PageHeader, FilterBar, DataTable, StatusBadge, Button } from "@/components/ads/ui";

const adGroups = [
  { id: "ag1", name: "Young Music Fans", campaign: "Summer Launch 2025", status: "active" as const, budget: "$1,500/day", impressions: "210K", clicks: "6.2K", ctr: "2.95%" },
  { id: "ag2", name: "Broad Reach — US", campaign: "Brand Awareness Q2", status: "active" as const, budget: "$3,000/day", impressions: "580K", clicks: "4.1K", ctr: "0.71%" },
  { id: "ag3", name: "Retargeting Pool", campaign: "Summer Launch 2025", status: "paused" as const, budget: "$500/day", impressions: "42K", clicks: "1.8K", ctr: "4.29%" },
  { id: "ag4", name: "Podcast Listeners 25-44", campaign: "Podcast Discovery", status: "active" as const, budget: "$800/day", impressions: "95K", clicks: "2.3K", ctr: "2.42%" },
];

const columns = [
  { key: "name", label: "Ad Group" },
  { key: "campaign", label: "Campaign" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "budget", label: "Budget" },
  { key: "impressions", label: "Impressions" },
  { key: "clicks", label: "Clicks" },
  { key: "ctr", label: "CTR" },
];

export default function AdGroupsPage() {
  const [search, setSearch] = useState("");
  const filtered = adGroups.filter((g) => g.name.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Ad Groups"
        description="Organize your campaigns with targeted ad groups."
        breadcrumbs={[{ label: "Ads Manager", href: "/ads/ads-manager" }, { label: "Ad Groups" }]}
        actions={<Button>+ Create Ad Group</Button>}
      />
      <FilterBar searchPlaceholder="Search ad groups…" onSearch={setSearch} />
      <DataTable columns={columns} data={filtered} />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 5. /ads/ads-manager/ads/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("ads-manager/ads", '''"use client";

import { useState } from "react";
import { PageHeader, FilterBar, DataTable, StatusBadge, Button } from "@/components/ads/ui";

const ads = [
  { id: "a1", name: "Summer Anthem — Audio", adGroup: "Young Music Fans", type: "Audio", status: "active" as const, impressions: "120K", clicks: "3.5K", ctr: "2.92%" },
  { id: "a2", name: "Brand Story — Video", adGroup: "Broad Reach — US", type: "Video", status: "active" as const, impressions: "340K", clicks: "2.1K", ctr: "0.62%" },
  { id: "a3", name: "New Release Display", adGroup: "Retargeting Pool", type: "Display", status: "paused" as const, impressions: "42K", clicks: "1.8K", ctr: "4.29%" },
  { id: "a4", name: "Podcast Promo — Audio", adGroup: "Podcast Listeners 25-44", type: "Audio", status: "active" as const, impressions: "78K", clicks: "1.9K", ctr: "2.44%" },
  { id: "a5", name: "Holiday Sale — Companion", adGroup: "Young Music Fans", type: "Companion", status: "draft" as const, impressions: "—", clicks: "—", ctr: "—" },
];

const columns = [
  { key: "name", label: "Ad" },
  { key: "adGroup", label: "Ad Group" },
  { key: "type", label: "Type" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "impressions", label: "Impressions" },
  { key: "clicks", label: "Clicks" },
  { key: "ctr", label: "CTR" },
];

export default function AdsListPage() {
  const [search, setSearch] = useState("");
  const filtered = ads.filter((a) => a.name.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Ads"
        description="Manage all your ad creatives and their delivery."
        breadcrumbs={[{ label: "Ads Manager", href: "/ads/ads-manager" }, { label: "Ads" }]}
        actions={<Button>+ Create Ad</Button>}
      />
      <FilterBar
        searchPlaceholder="Search ads…"
        onSearch={setSearch}
        filters={[
          { label: "Type", options: ["Audio", "Video", "Display", "Companion"] },
          { label: "Status", options: ["Active", "Paused", "Draft"] },
        ]}
      />
      <DataTable columns={columns} data={filtered} />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 6. /ads/ads-manager/monitor/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("ads-manager/monitor", '''"use client";

import { useState } from "react";
import { PageHeader, TabBar, MetricCard, DataTable, StatusBadge } from "@/components/ads/ui";

const alerts = [
  { id: "al1", campaign: "Summer Launch 2025", type: "Delivery", message: "Spend pacing 15% below target", severity: "warning" as const, time: "2 min ago" },
  { id: "al2", campaign: "Brand Awareness Q2", type: "Budget", message: "Daily budget reached 90% threshold", severity: "warning" as const, time: "15 min ago" },
  { id: "al3", campaign: "New Artist Promo", type: "Creative", message: "Ad rejected — policy violation (misleading claims)", severity: "error" as const, time: "1 hr ago" },
  { id: "al4", campaign: "Podcast Discovery", type: "Audience", message: "Audience size decreased below 1,000", severity: "info" as const, time: "3 hr ago" },
];

const healthData = [
  { id: "h1", campaign: "Summer Launch 2025", status: "active" as const, pacing: "92%", delivery: "Good", cpm: "$7.50", trend: "Stable" },
  { id: "h2", campaign: "Brand Awareness Q2", status: "active" as const, pacing: "88%", delivery: "Good", cpm: "$10.20", trend: "Improving" },
  { id: "h3", campaign: "New Artist Promo", status: "paused" as const, pacing: "45%", delivery: "Under-delivering", cpm: "$14.30", trend: "Declining" },
  { id: "h4", campaign: "Podcast Discovery", status: "active" as const, pacing: "78%", delivery: "Fair", cpm: "$8.10", trend: "Stable" },
];

const healthColumns = [
  { key: "campaign", label: "Campaign" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "pacing", label: "Pacing" },
  { key: "delivery", label: "Delivery Health" },
  { key: "cpm", label: "CPM" },
  { key: "trend", label: "Trend" },
];

export default function MonitorPage() {
  const [tab, setTab] = useState(0);

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Monitor"
        description="Track delivery health, performance alerts, and spend pacing across your campaigns."
        breadcrumbs={[{ label: "Ads Manager", href: "/ads/ads-manager" }, { label: "Monitor" }]}
      />

      <TabBar tabs={["Delivery Health", "Alerts", "Performance Links"]} active={tab} onChange={setTab} />

      {tab === 0 && (
        <div>
          <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
            <MetricCard label="Healthy Campaigns" value="2" delta="of 4 total" deltaType="neutral" />
            <MetricCard label="Under-delivering" value="1" delta="New Artist Promo" deltaType="negative" />
            <MetricCard label="Avg. Pacing" value="76%" delta="+5% vs yesterday" deltaType="positive" />
          </div>
          <DataTable columns={healthColumns} data={healthData} />
        </div>
      )}

      {tab === 1 && (
        <div className="space-y-3">
          {alerts.map((alert) => (
            <div key={alert.id} className={`rounded-lg border p-4 ${
              alert.severity === "error" ? "border-red-200 bg-red-50" : alert.severity === "warning" ? "border-amber-200 bg-amber-50" : "border-blue-200 bg-blue-50"
            }`}>
              <div className="flex items-center justify-between">
                <div>
                  <span className="text-xs font-medium uppercase text-neutral-500">{alert.type}</span>
                  <p className="text-sm font-medium text-neutral-900">{alert.campaign}</p>
                  <p className="text-sm text-neutral-600">{alert.message}</p>
                </div>
                <span className="text-xs text-neutral-400">{alert.time}</span>
              </div>
            </div>
          ))}
        </div>
      )}

      {tab === 2 && (
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {[
            { label: "Analytics Dashboard", desc: "Detailed performance metrics and trends", href: "/ads/analytics" },
            { label: "Attribution Reports", desc: "Understand your conversion paths", href: "/ads/analytics/attribution" },
            { label: "Audience Insights", desc: "Who is engaging with your ads", href: "/ads/analytics/audience" },
            { label: "Creative Performance", desc: "Compare ad creative effectiveness", href: "/ads/creatives" },
            { label: "Billing Overview", desc: "Spend, invoices, and payment details", href: "/ads/billing" },
            { label: "Experiments", desc: "A/B tests and lift studies", href: "/ads/analytics/experiments" },
          ].map((link) => (
            <a key={link.label} href={link.href} className="rounded-xl border border-neutral-100 bg-white p-5 transition-colors hover:border-neutral-200">
              <h3 className="text-sm font-semibold text-neutral-900">{link.label}</h3>
              <p className="mt-1 text-xs text-neutral-500">{link.desc}</p>
            </a>
          ))}
        </div>
      )}
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 7. /ads/ads-manager/optimize/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("ads-manager/optimize", '''"use client";

import { useState } from "react";
import { PageHeader, TabBar, MetricCard, Button } from "@/components/ads/ui";

export default function OptimizePage() {
  const [tab, setTab] = useState(0);

  const recommendations = {
    budget: [
      { id: "b1", campaign: "Summer Launch 2025", action: "Increase daily budget by 20%", reason: "Campaign is pacing 92% with strong ROAS of 4.2x", impact: "High" },
      { id: "b2", campaign: "Brand Awareness Q2", action: "Shift budget to weekends", reason: "Weekend CPM is 30% lower with similar reach", impact: "Medium" },
      { id: "b3", campaign: "Podcast Discovery", action: "Reduce budget by 10%", reason: "CPA has increased 25% over last 7 days", impact: "Medium" },
    ],
    delivery: [
      { id: "d1", campaign: "New Artist Promo", action: "Expand audience targeting", reason: "Current audience too narrow — delivery limited", impact: "High" },
      { id: "d2", campaign: "Summer Launch 2025", action: "Add podcast placements", reason: "Untapped inventory with low competition", impact: "Medium" },
    ],
    audience: [
      { id: "a1", campaign: "Brand Awareness Q2", action: "Add 25-34 age segment", reason: "Best performing segment not fully captured", impact: "High" },
      { id: "a2", campaign: "Podcast Discovery", action: "Include lookalike audience", reason: "Similar users convert 2x better than broad", impact: "High" },
    ],
    creative: [
      { id: "c1", campaign: "Summer Launch 2025", action: "Test video variant", reason: "Audio-only ads underperforming vs video in this segment", impact: "High" },
      { id: "c2", campaign: "Brand Awareness Q2", action: "Refresh companion image", reason: "Current creative showing fatigue — 14 days live", impact: "Medium" },
    ],
  };

  const currentRecs = tab === 0 ? recommendations.budget : tab === 1 ? recommendations.delivery : tab === 2 ? recommendations.audience : recommendations.creative;

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Optimize"
        description="AI-powered recommendations to improve campaign performance."
        breadcrumbs={[{ label: "Ads Manager", href: "/ads/ads-manager" }, { label: "Optimize" }]}
      />

      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-4">
        <MetricCard label="Budget" value="3" delta="recommendations" deltaType="neutral" />
        <MetricCard label="Delivery" value="2" delta="recommendations" deltaType="neutral" />
        <MetricCard label="Audience" value="2" delta="recommendations" deltaType="neutral" />
        <MetricCard label="Creative" value="2" delta="recommendations" deltaType="neutral" />
      </div>

      <TabBar tabs={["Budget", "Delivery", "Audience", "Creative"]} active={tab} onChange={setTab} />

      <div className="space-y-4">
        {currentRecs.map((rec) => (
          <div key={rec.id} className="rounded-xl border border-neutral-100 bg-white p-5">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-xs font-medium text-neutral-400">{rec.campaign}</span>
                <p className="mt-1 text-sm font-semibold text-neutral-900">{rec.action}</p>
                <p className="mt-1 text-sm text-neutral-500">{rec.reason}</p>
              </div>
              <div className="flex items-center gap-3">
                <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${
                  rec.impact === "High" ? "bg-emerald-50 text-emerald-700" : "bg-amber-50 text-amber-700"
                }`}>
                  {rec.impact} impact
                </span>
                <Button variant="secondary" onClick={() => {}}>Apply</Button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 8. /ads/automated-rules/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("automated-rules", '''"use client";

import { useState } from "react";
import { PageHeader, FilterBar, DataTable, StatusBadge, Button, StatusToggle } from "@/components/ads/ui";

const rules = [
  { id: "r1", name: "Pause low CTR campaigns", trigger: "CTR < 0.5% for 3 days", action: "Pause campaign", status: "active" as const, appliesTo: "All campaigns", lastTriggered: "2 days ago" },
  { id: "r2", name: "Budget increase for high ROAS", trigger: "ROAS > 5x for 7 days", action: "Increase budget by 20%", status: "active" as const, appliesTo: "Sales campaigns", lastTriggered: "1 week ago" },
  { id: "r3", name: "Notify high CPA", trigger: "CPA > $50", action: "Send email notification", status: "paused" as const, appliesTo: "Lead gen campaigns", lastTriggered: "Never" },
  { id: "r4", name: "Frequency cap alert", trigger: "Frequency > 5 per week", action: "Send Slack notification", status: "active" as const, appliesTo: "Awareness campaigns", lastTriggered: "5 hours ago" },
  { id: "r5", name: "Auto-resume campaigns", trigger: "Paused by budget rule", action: "Resume at 12:00 AM", status: "active" as const, appliesTo: "All campaigns", lastTriggered: "Yesterday" },
];

const columns = [
  { key: "name", label: "Rule Name" },
  { key: "trigger", label: "Trigger Condition" },
  { key: "action", label: "Action" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "appliesTo", label: "Applies To" },
  { key: "lastTriggered", label: "Last Triggered" },
];

export default function AutomatedRulesPage() {
  const [search, setSearch] = useState("");
  const filtered = rules.filter((r) => r.name.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Automated Rules"
        description="Create rules that automatically adjust your campaigns based on performance conditions."
        actions={<Button>+ Create Rule</Button>}
      />
      <FilterBar searchPlaceholder="Search rules…" onSearch={setSearch} filters={[{ label: "Status", options: ["Active", "Paused"] }]} />
      <DataTable columns={columns} data={filtered} />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 9. /ads/comments-manager/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("comments-manager", '''"use client";

import { useState } from "react";
import { PageHeader, TabBar, FilterBar, DataTable, Button } from "@/components/ads/ui";

const comments = [
  { id: "cm1", user: "Alex Rivera", text: "Love the new summer playlist ad! 🔥", ad: "Summer Anthem — Audio", time: "5 min ago", replied: false },
  { id: "cm2", user: "Jordan Lee", text: "Where can I find more tracks like this?", ad: "Summer Anthem — Audio", time: "22 min ago", replied: true },
  { id: "cm3", user: "Sam Chen", text: "This brand is amazing, been a fan for years", ad: "Brand Story — Video", time: "1 hr ago", replied: false },
  { id: "cm4", user: "Casey Kim", text: "Link doesn\\'t work on mobile 😕", ad: "New Release Display", time: "3 hr ago", replied: false },
  { id: "cm5", user: "Morgan Blake", text: "Great podcast recommendation, subscribed!", ad: "Podcast Promo — Audio", time: "5 hr ago", replied: true },
];

const columns = [
  { key: "user", label: "User" },
  { key: "text", label: "Comment" },
  { key: "ad", label: "Ad" },
  { key: "time", label: "Time" },
  { key: "replied", label: "Replied", render: (v: boolean) => (
    <span className={`text-xs font-medium ${v ? "text-emerald-600" : "text-amber-600"}`}>
      {v ? "Yes" : "Pending"}
    </span>
  )},
];

export default function CommentsManagerPage() {
  const [tab, setTab] = useState(0);
  const [search, setSearch] = useState("");

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Comments Manager"
        description="Monitor, reply to, and moderate comments on your ads."
      />
      <TabBar tabs={["All Comments", "Unreplied", "Flagged", "Hidden"]} active={tab} onChange={setTab} />
      <FilterBar searchPlaceholder="Search comments…" onSearch={setSearch} />
      <DataTable columns={columns} data={tab === 1 ? comments.filter((c) => !c.replied) : comments} />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 10. /ads/mmm-data-request/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("mmm-data-request", '''"use client";

import { useState } from "react";
import { PageHeader, DataTable, StatusBadge, Button, FormField, MetricCard } from "@/components/ads/ui";

const requests = [
  { id: "mr1", name: "Q2 2025 MMM Analysis", status: "completed" as const, dateRange: "Apr 1 – Jun 30, 2025", channels: "Audio, Video, Display", requestedBy: "Marketing Team", requestedDate: "Mar 15, 2025" },
  { id: "mr2", name: "Holiday Campaign MMM", status: "pending_review" as const, dateRange: "Nov 15 – Dec 31, 2024", channels: "All channels", requestedBy: "Analytics Team", requestedDate: "Jan 10, 2025" },
  { id: "mr3", name: "Cross-Media Attribution", status: "in_review" as const, dateRange: "Jan 1 – Mar 31, 2025", channels: "Audio, Podcast", requestedBy: "Brand Team", requestedDate: "Apr 1, 2025" },
];

const columns = [
  { key: "name", label: "Request" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "dateRange", label: "Date Range" },
  { key: "channels", label: "Channels" },
  { key: "requestedBy", label: "Requested By" },
  { key: "requestedDate", label: "Requested Date" },
];

export default function MMMDataRequestPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="MMM Data Request"
        description="Request Marketing Mix Modeling data to measure cross-channel advertising effectiveness."
        actions={<Button>+ New Request</Button>}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Completed" value="1" delta="request" deltaType="neutral" />
        <MetricCard label="In Review" value="1" delta="request" deltaType="neutral" />
        <MetricCard label="Pending" value="1" delta="request" deltaType="neutral" />
      </div>
      <DataTable columns={columns} data={requests} />
      <div className="mt-8 rounded-xl border border-neutral-100 bg-white p-6">
        <h2 className="text-lg font-semibold text-neutral-900 mb-4">Submit New MMM Data Request</h2>
        <div className="space-y-4">
          <FormField label="Analysis Name">
            <input placeholder="e.g., Q3 2025 MMM Analysis" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
          </FormField>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <FormField label="Start Date">
              <input type="date" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
            </FormField>
            <FormField label="End Date">
              <input type="date" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
            </FormField>
          </div>
          <FormField label="Channels to Include">
            <div className="flex flex-wrap gap-2">
              {["Audio Ads", "Video Ads", "Display", "Podcast", "Radio", "Search", "Social"].map((ch) => (
                <label key={ch} className="flex items-center gap-2 text-sm text-neutral-700">
                  <input type="checkbox" defaultChecked className="h-4 w-4 rounded border-neutral-300" />
                  {ch}
                </label>
              ))}
            </div>
          </FormField>
          <Button>Submit Request</Button>
        </div>
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 11. /ads/audiences/demographic/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("audiences/demographic", '''"use client";

import { PageHeader, MetricCard, Button, FormField } from "@/components/ads/ui";

export default function DemographicTargetingPage() {
  const ageGroups = ["13-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"];
  const genders = ["Male", "Female", "Non-binary", "Prefer not to say"];

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Demographic Targeting"
        description="Define audience segments based on age, gender, and other demographic attributes."
        breadcrumbs={[{ label: "Audiences", href: "/ads/audiences" }, { label: "Demographics" }]}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Reachable Audience" value="42.8M" delta="with current settings" deltaType="neutral" />
        <MetricCard label="Age Segments" value="5" delta="selected" deltaType="neutral" />
        <MetricCard label="Gender" value="All" delta="selected" deltaType="neutral" />
      </div>
      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Age Range</h3>
          <div className="flex flex-wrap gap-3">
            {ageGroups.map((age) => (
              <label key={age} className="flex items-center gap-2 rounded-lg border border-neutral-100 px-4 py-2.5 text-sm text-neutral-700 hover:bg-neutral-50">
                <input type="checkbox" defaultChecked={["18-24", "25-34", "35-44"].includes(age)} className="h-4 w-4 rounded border-neutral-300" />
                {age}
              </label>
            ))}
          </div>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Gender</h3>
          <div className="flex flex-wrap gap-3">
            {genders.map((g) => (
              <label key={g} className="flex items-center gap-2 rounded-lg border border-neutral-100 px-4 py-2.5 text-sm text-neutral-700 hover:bg-neutral-50">
                <input type="checkbox" defaultChecked className="h-4 w-4 rounded border-neutral-300" />
                {g}
              </label>
            ))}
          </div>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Household Income</h3>
          <div className="flex flex-wrap gap-3">
            {["Top 10%", "10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "60-70%", "70-80%", "80-90%", "Bottom 10%"].map((inc) => (
              <label key={inc} className="flex items-center gap-2 rounded-lg border border-neutral-100 px-4 py-2.5 text-sm text-neutral-700 hover:bg-neutral-50">
                <input type="checkbox" className="h-4 w-4 rounded border-neutral-300" />
                {inc}
              </label>
            ))}
          </div>
        </div>
        <Button>Save Demographic Targeting</Button>
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 12. /ads/creatives/create/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("creatives/create", '''"use client";

import { useState } from "react";
import { PageHeader, FormField, Button } from "@/components/ads/ui";

export default function CreateCreativePage() {
  const [adType, setAdType] = useState("audio");
  const [name, setName] = useState("");
  const [cta, setCta] = useState("Learn More");
  const [destination, setDestination] = useState("");

  return (
    <div className="mx-auto max-w-4xl p-6">
      <PageHeader
        title="Create Ad"
        description="Build a new ad creative for your campaigns."
        breadcrumbs={[{ label: "Creatives", href: "/ads/creatives" }, { label: "Create" }]}
      />

      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h2 className="text-lg font-semibold text-neutral-900 mb-4">Ad Type</h2>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
            {[
              { id: "audio", label: "Audio Ad", desc: "30-sec audio clip between songs" },
              { id: "video", label: "Video Ad", desc: "In-feed video with companion" },
              { id: "display", label: "Display Ad", desc: "Image-based companion ad" },
            ].map((t) => (
              <button key={t.id} onClick={() => setAdType(t.id)} className={`rounded-xl border-2 p-5 text-left ${adType === t.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                <h3 className="text-sm font-semibold text-neutral-900">{t.label}</h3>
                <p className="mt-1 text-xs text-neutral-500">{t.desc}</p>
              </button>
            ))}
          </div>
        </div>

        <div className="rounded-xl border border-neutral-100 bg-white p-6 space-y-5">
          <FormField label="Ad Name">
            <input value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g., Summer Promo Audio Ad" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
          </FormField>

          {adType === "audio" && (
            <div className="space-y-4">
              <FormField label="Audio File" description="MP3 or WAV, max 30 seconds">
                <div className="flex items-center gap-3">
                  <div className="flex-1 rounded-lg border border-dashed border-neutral-300 p-6 text-center text-sm text-neutral-400">
                    Drag & drop audio file or click to browse
                  </div>
                </div>
              </FormField>
              <FormField label="Companion Image (optional)">
                <div className="rounded-lg border border-dashed border-neutral-300 p-6 text-center text-sm text-neutral-400">
                  1200×628px recommended, JPG or PNG
                </div>
              </FormField>
            </div>
          )}

          {adType === "video" && (
            <div className="space-y-4">
              <FormField label="Video File" description="MP4, 16:9 or 1:1, max 30 seconds">
                <div className="rounded-lg border border-dashed border-neutral-300 p-8 text-center text-sm text-neutral-400">
                  Drag & drop video file or click to browse
                </div>
              </FormField>
            </div>
          )}

          {adType === "display" && (
            <FormField label="Image" description="1200×628px, JPG or PNG, max 5MB">
              <div className="rounded-lg border border-dashed border-neutral-300 p-8 text-center text-sm text-neutral-400">
                Drag & drop image or click to browse
              </div>
            </FormField>
          )}

          <FormField label="Call-to-Action">
            <select value={cta} onChange={(e) => setCta(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
              {["Learn More", "Shop Now", "Listen Now", "Download", "Sign Up", "Watch More", "Get Offer"].map((c) => (
                <option key={c}>{c}</option>
              ))}
            </select>
          </FormField>

          <FormField label="Destination URL">
            <input value={destination} onChange={(e) => setDestination(e.target.value)} placeholder="https://example.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
          </FormField>
        </div>

        <div className="rounded-xl border border-neutral-100 bg-neutral-50 p-6 text-center">
          <p className="text-sm text-neutral-500 mb-3">Ad Preview</p>
          <div className="mx-auto max-w-sm rounded-lg border border-neutral-200 bg-white p-4">
            <div className="h-20 rounded bg-neutral-100 flex items-center justify-center text-xs text-neutral-400">
              {adType === "audio" ? "🎵 Audio" : adType === "video" ? "🎬 Video" : "🖼 Display"}
            </div>
            <p className="mt-2 text-sm font-medium text-neutral-900">{name || "Your Ad"}</p>
            <p className="text-xs text-neutral-500">{cta} → {destination || "example.com"}</p>
          </div>
        </div>

        <div className="flex gap-3">
          <Button variant="secondary">Save as Draft</Button>
          <Button>Create Ad</Button>
        </div>
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 13. /ads/creatives/partnerships/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("creatives/partnerships", '''"use client";

import { PageHeader, DataTable, StatusBadge, Button, MetricCard } from "@/components/ads/ui";

const partners = [
  { id: "p1", name: "Creative Studio X", type: "Production", status: "active" as const, campaigns: 8, lastActive: "2 days ago" },
  { id: "p2", name: "SoundDesign Co.", type: "Audio Production", status: "active" as const, campaigns: 3, lastActive: "1 week ago" },
  { id: "p3", name: "VidCraft Agency", type: "Video Production", status: "pending_review" as const, campaigns: 0, lastActive: "Pending approval" },
  { id: "p4", name: "Influencer Connect", type: "Creator Partnership", status: "active" as const, campaigns: 12, lastActive: "Today" },
];

const columns = [
  { key: "name", label: "Partner" },
  { key: "type", label: "Type" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "campaigns", label: "Active Campaigns" },
  { key: "lastActive", label: "Last Active" },
];

export default function CreativePartnershipsPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Creative Partnerships"
        description="Manage partnerships with creative agencies, production studios, and content creators."
        breadcrumbs={[{ label: "Creatives", href: "/ads/creatives" }, { label: "Partnerships" }]}
        actions={<Button>+ Add Partner</Button>}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Active Partners" value="3" delta="1 pending approval" deltaType="neutral" />
        <MetricCard label="Partner Campaigns" value="23" delta="+5 this month" deltaType="positive" />
        <MetricCard label="Total Partner Spend" value="$48,200" prefix="$" delta="this month" deltaType="neutral" />
      </div>
      <DataTable columns={columns} data={partners} />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 14. /ads/analytics/cross-media/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("analytics/cross-media", '''"use client";

import { useState } from "react";
import { PageHeader, TabBar, MetricCard, DataTable } from "@/components/ads/ui";

const channelData = [
  { id: "ch1", channel: "Audio Ads", reach: "28.4M", frequency: "3.2", incrementalReach: "8.1M", deDupedReach: "20.3M" },
  { id: "ch2", channel: "Video Ads", reach: "15.6M", frequency: "2.1", incrementalReach: "5.2M", deDupedReach: "10.4M" },
  { id: "ch3", channel: "Display", reach: "22.1M", frequency: "4.8", incrementalReach: "3.9M", deDupedReach: "18.2M" },
  { id: "ch4", channel: "Podcast", reach: "6.8M", frequency: "1.5", incrementalReach: "4.1M", deDupedReach: "2.7M" },
];

const columns = [
  { key: "channel", label: "Channel" },
  { key: "reach", label: "Total Reach" },
  { key: "frequency", label: "Avg. Frequency" },
  { key: "incrementalReach", label: "Incremental Reach" },
  { key: "deDupedReach", label: "De-duped Reach" },
];

export default function CrossMediaPage() {
  const [tab, setTab] = useState(0);

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Cross-Media Measurement"
        description="Measure reach and frequency across channels with de-duplicated audience insights."
        breadcrumbs={[{ label: "Analytics", href: "/ads/analytics" }, { label: "Cross-Media" }]}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-4">
        <MetricCard label="Total Reach" value="52.9M" delta="across all channels" deltaType="neutral" />
        <MetricCard label="De-duped Reach" value="38.4M" delta="27% overlap" deltaType="neutral" />
        <MetricCard label="Avg. Frequency" value="2.9" delta="across channels" deltaType="neutral" />
        <MetricCard label="Incremental Reach" value="21.3M" delta="from secondary channels" deltaType="positive" />
      </div>
      <TabBar tabs={["Channel Comparison", "Overlap Analysis", "Reach Curves"]} active={tab} onChange={setTab} />
      {tab === 0 && <DataTable columns={columns} data={channelData} />}
      {tab === 1 && (
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Channel Overlap</h3>
          <div className="space-y-3">
            {[
              { pair: "Audio × Video", overlap: "18%", sharedReach: "5.1M" },
              { pair: "Audio × Display", overlap: "24%", sharedReach: "6.8M" },
              { pair: "Video × Display", overlap: "12%", sharedReach: "1.9M" },
              { pair: "Audio × Podcast", overlap: "8%", sharedReach: "2.2M" },
            ].map((item) => (
              <div key={item.pair} className="flex items-center justify-between rounded-lg border border-neutral-50 px-4 py-3">
                <span className="text-sm font-medium text-neutral-900">{item.pair}</span>
                <div className="flex items-center gap-6 text-sm">
                  <span className="text-neutral-500">Overlap: <span className="font-medium text-neutral-700">{item.overlap}</span></span>
                  <span className="text-neutral-500">Shared: <span className="font-medium text-neutral-700">{item.sharedReach}</span></span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      {tab === 2 && (
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Reach Curves</h3>
          <p className="text-sm text-neutral-500">Reach curve visualization shows marginal reach gains per dollar spent across channels. Contact your analytics team for the full interactive report.</p>
        </div>
      )}
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 15. /ads/analytics/third-party/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("analytics/third-party", '''"use client";

import { PageHeader, DataTable, StatusBadge, Button, MetricCard } from "@/components/ads/ui";

const vendors = [
  { id: "v1", name: "DoubleVerify", type: "Viewability & Fraud", status: "active" as const, lastSync: "2 hr ago", metrics: "Viewability: 92%, Fraud: 0.3%" },
  { id: "v2", name: "IAS", type: "Brand Safety", status: "active" as const, lastSync: "1 hr ago", metrics: "Safe: 99.1%, Risk: 0.9%" },
  { id: "v3", name: "Moat", type: "Attention Metrics", status: "active" as const, lastSync: "3 hr ago", metrics: "Attention: 4.2s, In-view: 88%" },
  { id: "v4", name: "Neustar", type: "Audience Verification", status: "paused" as const, lastSync: "2 days ago", metrics: "Paused" },
  { id: "v5", name: "Comscore", type: "Cross-Platform Reach", status: "active" as const, lastSync: "6 hr ago", metrics: "Deduped reach: 38M" },
];

const columns = [
  { key: "name", label: "Vendor" },
  { key: "type", label: "Measurement Type" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "lastSync", label: "Last Sync" },
  { key: "metrics", label: "Key Metrics" },
];

export default function ThirdPartyPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Third-Party Measurement"
        description="Integrate and manage third-party measurement vendors for independent verification."
        breadcrumbs={[{ label: "Analytics", href: "/ads/analytics" }, { label: "Third-Party" }]}
        actions={<Button>+ Add Vendor</Button>}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Active Vendors" value="4" delta="1 paused" deltaType="neutral" />
        <MetricCard label="Avg. Viewability" value="92%" delta="+2% vs last month" deltaType="positive" />
        <MetricCard label="Brand Safety Score" value="99.1%" delta="across all vendors" deltaType="neutral" />
      </div>
      <DataTable columns={columns} data={vendors} />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 16. /ads/analytics/metrics-glossary/page.tsx
# ═══════════════════════════════════════════════════════════════════════════
write_page("analytics/metrics-glossary", '''"use client";

import { useState } from "react";
import { PageHeader, FilterBar, DataTable } from "@/components/ads/ui";

const metrics = [
  { id: "m1", metric: "Impressions", category: "Delivery", definition: "The number of times your ad was displayed to users" },
  { id: "m2", metric: "Reach", category: "Delivery", definition: "The number of unique users who saw your ad" },
  { id: "m3", metric: "Frequency", category: "Delivery", definition: "Average number of times each user saw your ad (Impressions ÷ Reach)" },
  { id: "m4", metric: "Clicks", category: "Engagement", definition: "The number of times users clicked on your ad" },
  { id: "m5", metric: "CTR", category: "Engagement", definition: "Click-through rate — Clicks ÷ Impressions × 100" },
  { id: "m6", metric: "Video Views", category: "Engagement", definition: "Number of times your video ad was viewed (various thresholds: 2s, 25%, 50%, 100%)" },
  { id: "m7", metric: "CPM", category: "Cost", definition: "Cost per thousand impressions — Total Spend ÷ Impressions × 1000" },
  { id: "m8", metric: "CPC", category: "Cost", definition: "Cost per click — Total Spend ÷ Clicks" },
  { id: "m9", metric: "CPA", category: "Cost", definition: "Cost per acquisition — Total Spend ÷ Conversions" },
  { id: "m10", metric: "ROAS", category: "Conversion", definition: "Return on ad spend — Revenue ÷ Total Spend" },
  { id: "m11", metric: "Conversion Rate", category: "Conversion", definition: "Conversions ÷ Clicks × 100" },
  { id: "m12", metric: "SVI", category: "Audio", definition: "Stream Volume Index — relative streaming activity driven by your ads" },
  { id: "m13", metric: "Audio Completion Rate", category: "Audio", definition: "Percentage of audio ads listened to completion" },
  { id: "m14", metric: "Brand Lift", category: "Brand", definition: "Measured increase in brand awareness, consideration, or favorability" },
  { id: "m15", metric: "Ad Recall", category: "Brand", definition: "Percentage of users who remember seeing your ad" },
];

const columns = [
  { key: "metric", label: "Metric" },
  { key: "category", label: "Category" },
  { key: "definition", label: "Definition" },
];

export default function MetricsGlossaryPage() {
  const [search, setSearch] = useState("");
  const filtered = metrics.filter((m) =>
    m.metric.toLowerCase().includes(search.toLowerCase()) ||
    m.definition.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Metrics Glossary"
        description="Definitions and calculations for all advertising metrics."
        breadcrumbs={[{ label: "Analytics", href: "/ads/analytics" }, { label: "Metrics Glossary" }]}
      />
      <FilterBar searchPlaceholder="Search metrics…" onSearch={setSearch} filters={[{ label: "Category", options: ["Delivery", "Engagement", "Cost", "Conversion", "Audio", "Brand"] }]} />
      <DataTable columns={columns} data={filtered} />
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 17-21. /ads/tools/* pages
# ═══════════════════════════════════════════════════════════════════════════
write_page("tools/keyword-planner", '''"use client";

import { useState } from "react";
import { PageHeader, FilterBar, DataTable, MetricCard, Button } from "@/components/ads/ui";

const keywords = [
  { id: "k1", keyword: "summer playlist", volume: "185K", competition: "High", bid: "$2.40", relevance: 95 },
  { id: "k2", keyword: "new music release", volume: "92K", competition: "Medium", bid: "$1.80", relevance: 88 },
  { id: "k3", keyword: "workout music", volume: "124K", competition: "High", bid: "$2.10", relevance: 72 },
  { id: "k4", keyword: "chill vibes", volume: "67K", competition: "Low", bid: "$0.90", relevance: 65 },
  { id: "k5", keyword: "indie discovery", volume: "28K", competition: "Low", bid: "$0.60", relevance: 82 },
  { id: "k6", keyword: "podcast comedy", volume: "51K", competition: "Medium", bid: "$1.40", relevance: 58 },
];

const columns = [
  { key: "keyword", label: "Keyword" },
  { key: "volume", label: "Monthly Volume" },
  { key: "competition", label: "Competition" },
  { key: "bid", label: "Suggested Bid" },
  { key: "relevance", label: "Relevance Score", render: (v: number) => (
    <div className="flex items-center gap-2">
      <div className="h-1.5 w-16 rounded-full bg-neutral-100"><div className="h-1.5 rounded-full bg-emerald-500" style={{ width: `${v}%` }} /></div>
      <span className="text-xs text-neutral-500">{v}%</span>
    </div>
  )},
];

export default function KeywordPlannerPage() {
  const [search, setSearch] = useState("");
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader title="Keyword Planner" description="Research keywords, view search volume, and discover new targeting opportunities." />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Keywords Researched" value="6" delta="in this session" deltaType="neutral" />
        <MetricCard label="Avg. Volume" value="91K" delta="monthly searches" deltaType="neutral" />
        <MetricCard label="Avg. Bid" value="$1.53" prefix="$" delta="suggested" deltaType="neutral" />
      </div>
      <FilterBar searchPlaceholder="Search keywords…" onSearch={setSearch} />
      <DataTable columns={columns} data={keywords} />
      <div className="mt-4 flex gap-2">
        <Button variant="secondary">Export Keywords</Button>
        <Button variant="secondary">Add to Campaign</Button>
      </div>
    </div>
  );
}
''')

write_page("tools/negative-keywords", '''"use client";

import { useState } from "react";
import { PageHeader, FilterBar, DataTable, Button, FormField } from "@/components/ads/ui";

const negativeKeywords = [
  { id: "nk1", keyword: "free music download", matchType: "Broad", campaign: "All campaigns", addedBy: "System", date: "Jan 15, 2025" },
  { id: "nk2", keyword: "pirated", matchType: "Exact", campaign: "Brand Awareness Q2", addedBy: "Manual", date: "Feb 1, 2025" },
  { id: "nk3", keyword: "illegal streaming", matchType: "Phrase", campaign: "All campaigns", addedBy: "System", date: "Jan 15, 2025" },
  { id: "nk4", keyword: "mp3 converter", matchType: "Broad", campaign: "Summer Launch 2025", addedBy: "Manual", date: "Mar 10, 2025" },
];

const columns = [
  { key: "keyword", label: "Keyword" },
  { key: "matchType", label: "Match Type" },
  { key: "campaign", label: "Campaign" },
  { key: "addedBy", label: "Added By" },
  { key: "date", label: "Date Added" },
];

export default function NegativeKeywordsPage() {
  const [search, setSearch] = useState("");
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader title="Negative Keywords" description="Prevent your ads from showing for irrelevant or harmful search terms." actions={<Button>+ Add Negative Keyword</Button>} />
      <FilterBar searchPlaceholder="Search negative keywords…" onSearch={setSearch} filters={[{ label: "Match Type", options: ["Broad", "Exact", "Phrase"] }]} />
      <DataTable columns={columns} data={negativeKeywords} selectable selected={new Set()} />
      <div className="mt-6 rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Add Negative Keywords</h3>
        <div className="space-y-3">
          <FormField label="Keywords" description="Enter one keyword per line">
            <textarea rows={3} placeholder="free music download\\npirated\\nillegal streaming" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
          </FormField>
          <div className="grid grid-cols-2 gap-4">
            <FormField label="Match Type">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>Broad</option><option>Exact</option><option>Phrase</option>
              </select>
            </FormField>
            <FormField label="Apply To">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>All campaigns</option><option>Selected campaigns</option>
              </select>
            </FormField>
          </div>
          <Button>Add Keywords</Button>
        </div>
      </div>
    </div>
  );
}
''')

write_page("tools/video-editor", '''"use client";

import { PageHeader, Button, CardGrid } from "@/components/ads/ui";

export default function VideoEditorPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader title="Video Editor" description="Trim, crop, and enhance your video ads with our built-in editor." />
      <div className="rounded-xl border border-neutral-100 bg-white p-8 text-center">
        <div className="mx-auto max-w-2xl">
          <div className="mb-6 rounded-lg border border-dashed border-neutral-300 p-12">
            <p className="text-sm text-neutral-400">Drag & drop a video file or click to browse</p>
            <p className="mt-1 text-xs text-neutral-400">MP4, MOV, or AVI — Max 500MB</p>
          </div>
          <div className="grid grid-cols-4 gap-4 mb-6">
            {["Trim", "Crop", "Add Text", "Add Music"].map((tool) => (
              <button key={tool} className="rounded-lg border border-neutral-200 px-3 py-2.5 text-sm font-medium text-neutral-700 hover:bg-neutral-50">
                {tool}
              </button>
            ))}
          </div>
          <div className="flex items-center justify-center gap-3">
            <Button variant="secondary">Upload New</Button>
            <Button disabled>Select a file to begin</Button>
          </div>
        </div>
      </div>
      <h2 className="mt-8 mb-4 text-lg font-semibold text-neutral-900">Recent Edits</h2>
      <CardGrid cards={[
        { label: "Brand Story — 30s Cut", description: "Last edited 2 hours ago", href: "#" },
        { label: "Product Demo — Square", description: "Last edited yesterday", href: "#" },
        { label: "Summer Promo — Vertical", description: "Last edited 3 days ago", href: "#" },
      ]} />
    </div>
  );
}
''')

write_page("tools/integrations", '''"use client";

import { PageHeader, DataTable, StatusBadge, Button, MetricCard } from "@/components/ads/ui";

const integrations = [
  { id: "i1", name: "Google Analytics", type: "Analytics", status: "active" as const, connected: "Jan 10, 2025", dataFlow: "Bidirectional" },
  { id: "i2", name: "Shopify", type: "Commerce", status: "active" as const, connected: "Dec 5, 2024", dataFlow: "Import" },
  { id: "i3", name: "Slack", type: "Notifications", status: "active" as const, connected: "Feb 14, 2025", dataFlow: "Export" },
  { id: "i4", name: "Salesforce", type: "CRM", status: "paused" as const, connected: "Nov 20, 2024", dataFlow: "Bidirectional" },
  { id: "i5", name: "Segment", type: "CDP", status: "active" as const, connected: "Mar 1, 2025", dataFlow: "Export" },
  { id: "i6", name: "Meta Ads", type: "Cross-Platform", status: "pending_review" as const, connected: "Pending", dataFlow: "—" },
];

const columns = [
  { key: "name", label: "Integration" },
  { key: "type", label: "Type" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "connected", label: "Connected" },
  { key: "dataFlow", label: "Data Flow" },
];

export default function ToolsIntegrationsPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader title="Integrations" description="Connect external tools and platforms to enhance your advertising workflow." actions={<Button>+ Add Integration</Button>} />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Active" value="4" delta="integrations" deltaType="neutral" />
        <MetricCard label="Paused" value="1" delta="integration" deltaType="neutral" />
        <MetricCard label="Pending" value="1" delta="integration" deltaType="neutral" />
      </div>
      <DataTable columns={columns} data={integrations} />
    </div>
  );
}
''')

write_page("tools/mcp", '''"use client";

import { PageHeader, DataTable, StatusBadge, Button, MetricCard, FormField } from "@/components/ads/ui";

const servers = [
  { id: "s1", name: "Analytics MCP Server", version: "1.2.0", status: "active" as const, tools: 12, lastPing: "2 min ago" },
  { id: "s2", name: "Campaign Manager MCP", version: "2.0.1", status: "active" as const, tools: 8, lastPing: "30 sec ago" },
  { id: "s3", name: "Creative Tools MCP", version: "1.0.0", status: "active" as const, tools: 5, lastPing: "1 min ago" },
  { id: "s4", name: "Audience MCP Server", version: "1.1.3", status: "paused" as const, tools: 6, lastPing: "Offline" },
];

const columns = [
  { key: "name", label: "Server" },
  { key: "version", label: "Version" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status} /> },
  { key: "tools", label: "Available Tools" },
  { key: "lastPing", label: "Last Ping" },
];

export default function MCPPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader title="MCP Server Installation" description="Manage Model Context Protocol servers for AI-powered advertising tools." actions={<Button>+ Install Server</Button>} />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Active Servers" value="3" delta="1 paused" deltaType="neutral" />
        <MetricCard label="Total Tools" value="31" delta="available" deltaType="neutral" />
        <MetricCard label="Uptime" value="99.8%" delta="last 30 days" deltaType="positive" />
      </div>
      <DataTable columns={columns} data={servers} />
      <div className="mt-8 rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Install New MCP Server</h3>
        <div className="space-y-3">
          <FormField label="Server URL or Package Name">
            <input placeholder="e.g., @ads/mcp-analytics or https://mcp.example.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
          </FormField>
          <FormField label="Configuration (JSON)">
            <textarea rows={4} placeholder='{"apiKey": "...", "region": "us"}' className="w-full rounded-lg border border-neutral-200 px-3 py-2 font-mono text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
          </FormField>
          <Button>Install Server</Button>
        </div>
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 22-25. /ads/policies-security/* pages
# ═══════════════════════════════════════════════════════════════════════════
write_page("policies-security", '''"use client";

import { PageHeader, CardGrid, MetricCard } from "@/components/ads/ui";

export default function PoliciesSecurityPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader title="Advertising Policies & Security" description="Review advertising policies, privacy settings, security configurations, and brand safety controls." />
      <div className="mb-8 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Policy Compliance" value="98%" delta="2 campaigns flagged" deltaType="neutral" />
        <MetricCard label="Security Score" value="A+" delta="All checks passed" deltaType="positive" />
        <MetricCard label="Brand Safety Events" value="3" delta="last 30 days" deltaType="neutral" />
      </div>
      <CardGrid cards={[
        { label: "Advertising Policies", description: "Content policies, prohibited categories, and restricted content guidelines", href: "/ads/policies-security/privacy" },
        { label: "Privacy & Data", description: "Data collection policies, consent management, and user privacy controls", href: "/ads/policies-security/privacy" },
        { label: "Security", description: "Account security, API access controls, and fraud prevention", href: "/ads/policies-security/security" },
        { label: "Brand Safety", description: "Content adjacency controls, blocklists, and suitability settings", href: "/ads/policies-security/brand-safety" },
      ]} />
    </div>
  );
}
''')

write_page("policies-security/privacy", '''"use client";

import { PageHeader, MetricCard, Button, FormField } from "@/components/ads/ui";

export default function PrivacyPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Privacy & Data Policies"
        description="Manage data collection, user consent, and privacy compliance for your advertising."
        breadcrumbs={[{ label: "Policies & Security", href: "/ads/policies-security" }, { label: "Privacy" }]}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Consent Rate" value="94.2%" delta="+1.2% vs last month" deltaType="positive" />
        <MetricCard label="Data Retention" value="90 days" delta="default period" deltaType="neutral" />
        <MetricCard label="Active Data Sources" value="7" delta="connected" deltaType="neutral" />
      </div>
      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Data Collection Policies</h3>
          <div className="space-y-3">
            {[
              { policy: "First-party cookie consent", status: true },
              { policy: "Third-party tracking disclosure", status: true },
              { policy: "Retargeting opt-out compliance", status: true },
              { policy: "Cross-device identification consent", status: false },
              { policy: "Location data collection", status: true },
            ].map((item) => (
              <div key={item.policy} className="flex items-center justify-between rounded-lg border border-neutral-50 px-4 py-3">
                <span className="text-sm text-neutral-700">{item.policy}</span>
                <span className={`text-xs font-medium ${item.status ? "text-emerald-600" : "text-amber-600"}`}>
                  {item.status ? "Enabled" : "Disabled"}
                </span>
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Data Retention Settings</h3>
          <div className="space-y-3">
            <FormField label="User Data Retention Period">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>30 days</option><option>60 days</option><option>90 days</option><option>180 days</option><option>365 days</option>
              </select>
            </FormField>
            <FormField label="Audience Data Retention Period">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>30 days</option><option>60 days</option><option>90 days</option><option>180 days</option>
              </select>
            </FormField>
            <Button>Save Settings</Button>
          </div>
        </div>
      </div>
    </div>
  );
}
''')

write_page("policies-security/security", '''"use client";

import { PageHeader, MetricCard, DataTable, StatusBadge, Button, FormField } from "@/components/ads/ui";

const securityEvents = [
  { id: "se1", event: "Login from new device", detail: "iPhone — San Francisco, CA", time: "2 hr ago", severity: "info" as const },
  { id: "se2", event: "API key rotated", detail: "Campaign Management API", time: "1 day ago", severity: "info" as const },
  { id: "se3", event: "Failed login attempt", detail: "Unknown IP — 192.168.1.45", time: "3 days ago", severity: "warning" as const },
];

const columns = [
  { key: "event", label: "Event" },
  { key: "detail", label: "Detail" },
  { key: "time", label: "Time" },
  { key: "severity", label: "Severity", render: (v: string) => (
    <span className={`text-xs font-medium ${v === "warning" ? "text-amber-600" : "text-blue-600"}`}>{v}</span>
  )},
];

export default function SecurityPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Security"
        description="Manage account security, API access, and review security events."
        breadcrumbs={[{ label: "Policies & Security", href: "/ads/policies-security" }, { label: "Security" }]}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Security Score" value="A+" delta="All checks passed" deltaType="positive" />
        <MetricCard label="Two-Factor Auth" value="On" delta="for all team members" deltaType="positive" />
        <MetricCard label="API Keys" value="3" delta="active" deltaType="neutral" />
      </div>
      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Security Settings</h3>
          <div className="space-y-3">
            {[
              { setting: "Two-factor authentication", desc: "Require 2FA for all team members", enabled: true },
              { setting: "IP allowlist", desc: "Restrict access to approved IP ranges", enabled: false },
              { setting: "Session timeout", desc: "Auto-logout after 30 minutes of inactivity", enabled: true },
              { setting: "API key rotation", desc: "Require key rotation every 90 days", enabled: true },
            ].map((item) => (
              <div key={item.setting} className="flex items-center justify-between rounded-lg border border-neutral-50 px-4 py-3">
                <div>
                  <p className="text-sm font-medium text-neutral-900">{item.setting}</p>
                  <p className="text-xs text-neutral-500">{item.desc}</p>
                </div>
                <span className={`text-xs font-medium ${item.enabled ? "text-emerald-600" : "text-neutral-400"}`}>
                  {item.enabled ? "Enabled" : "Disabled"}
                </span>
              </div>
            ))}
          </div>
        </div>
        <div>
          <h3 className="text-sm font-semibold text-neutral-900 mb-3">Recent Security Events</h3>
          <DataTable columns={columns} data={securityEvents} />
        </div>
      </div>
    </div>
  );
}
''')

write_page("policies-security/brand-safety", '''"use client";

import { PageHeader, MetricCard, DataTable, Button, FormField } from "@/components/ads/ui";

const blocklist = [
  { id: "bl1", category: "Violence & Gore", action: "Block", campaigns: "All", items: 24 },
  { id: "bl2", category: "Hate Speech", action: "Block", campaigns: "All", items: 18 },
  { id: "bl3", category: "Adult Content", action: "Block", campaigns: "All", items: 31 },
  { id: "bl4", category: "Illegal Drugs", action: "Block", campaigns: "All", items: 12 },
  { id: "bl5", category: "Political Content", action: "Flag", campaigns: "Awareness only", items: 8 },
  { id: "bl6", category: "Misinformation", action: "Block", campaigns: "All", items: 15 },
];

const columns = [
  { key: "category", label: "Category" },
  { key: "action", label: "Action" },
  { key: "campaigns", label: "Applies To" },
  { key: "items", label: "Blocked Items" },
];

export default function BrandSafetyPolicyPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Brand Safety Controls"
        description="Configure content adjacency rules, blocklists, and brand suitability settings."
        breadcrumbs={[{ label: "Policies & Security", href: "/ads/policies-security" }, { label: "Brand Safety" }]}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Blocked Categories" value="5" delta="fully blocked" deltaType="neutral" />
        <MetricCard label="Flagged Categories" value="1" delta="requires review" deltaType="neutral" />
        <MetricCard label="Safety Score" value="98%" delta="across all placements" deltaType="positive" />
      </div>
      <DataTable columns={columns} data={blocklist} />
      <div className="mt-6 rounded-xl border border-neutral-100 bg-white p-6">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Custom Blocklist</h3>
        <FormField label="URLs or Keywords" description="Add specific URLs or keywords to block your ads from appearing alongside">
          <textarea rows={3} placeholder="example.com/bad-content\\nproblematic-keyword" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
        </FormField>
        <Button className="mt-3">Add to Blocklist</Button>
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 26. /ads/setup/page.tsx - Account Setup Wizard (6 steps)
# ═══════════════════════════════════════════════════════════════════════════
write_page("setup", '''"use client";

import { useState } from "react";
import { PageHeader, Button, FormField } from "@/components/ads/ui";

const STEPS = ["Business Info", "Account Type", "Payment", "Targeting Defaults", "Team Members", "Review"];

export default function SetupPage() {
  const [step, setStep] = useState(0);
  const [businessName, setBusinessName] = useState("");
  const [industry, setIndustry] = useState("");
  const [accountType, setAccountType] = useState("advertiser");
  const [paymentMethod, setPaymentMethod] = useState("credit-card");

  return (
    <div className="mx-auto max-w-3xl p-6">
      <PageHeader
        title="Account Setup"
        description={`Step ${step + 1} of 6 — ${STEPS[step]}`}
      />

      {/* Progress bar */}
      <div className="mb-8 flex items-center gap-1">
        {STEPS.map((s, i) => (
          <div key={s} className="flex items-center gap-1">
            <div className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-semibold ${
              i === step ? "bg-neutral-900 text-white" : i < step ? "bg-emerald-500 text-white" : "bg-neutral-100 text-neutral-400"
            }`}>
              {i + 1}
            </div>
            {i < STEPS.length - 1 && <div className={`h-0.5 w-8 ${i < step ? "bg-emerald-500" : "bg-neutral-100"}`} />}
          </div>
        ))}
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        {/* Step 1: Business Info */}
        {step === 0 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Business Information</h2>
            <FormField label="Business Name">
              <input value={businessName} onChange={(e) => setBusinessName(e.target.value)} placeholder="Your company name" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
            </FormField>
            <FormField label="Industry">
              <select value={industry} onChange={(e) => setIndustry(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option value="">Select industry…</option>
                <option>Music & Entertainment</option><option>Technology</option><option>Retail & E-commerce</option><option>Financial Services</option><option>Healthcare</option><option>Education</option><option>Other</option>
              </select>
            </FormField>
            <FormField label="Business Website">
              <input placeholder="https://yourcompany.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
            </FormField>
          </div>
        )}

        {/* Step 2: Account Type */}
        {step === 1 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Account Type</h2>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
              {[
                { id: "advertiser", label: "Advertiser", desc: "Run ads for your own business" },
                { id: "agency", label: "Agency", desc: "Manage ads for multiple clients" },
              ].map((t) => (
                <button key={t.id} onClick={() => setAccountType(t.id)} className={`rounded-xl border-2 p-5 text-left ${accountType === t.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                  <h3 className="text-sm font-semibold text-neutral-900">{t.label}</h3>
                  <p className="mt-1 text-xs text-neutral-500">{t.desc}</p>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Step 3: Payment */}
        {step === 2 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Payment Method</h2>
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
              {[
                { id: "credit-card", label: "Credit Card", desc: "Visa, Mastercard, Amex" },
                { id: "bank-transfer", label: "Bank Transfer", desc: "ACH or wire transfer" },
                { id: "invoice", label: "Invoice", desc: "Monthly invoicing (qualified)" },
              ].map((m) => (
                <button key={m.id} onClick={() => setPaymentMethod(m.id)} className={`rounded-xl border-2 p-4 text-left ${paymentMethod === m.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                  <h3 className="text-sm font-semibold text-neutral-900">{m.label}</h3>
                  <p className="mt-1 text-xs text-neutral-500">{m.desc}</p>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Step 4: Targeting Defaults */}
        {step === 3 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Default Targeting</h2>
            <FormField label="Default Geographic Target">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>United States</option><option>Canada</option><option>United Kingdom</option><option>European Union</option><option>Worldwide</option>
              </select>
            </FormField>
            <FormField label="Default Language">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>English</option><option>Spanish</option><option>French</option><option>German</option><option>All Languages</option>
              </select>
            </FormField>
            <FormField label="Default Age Range">
              <div className="flex gap-2">
                <select className="rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>18</option><option>21</option><option>25</option>
                </select>
                <span className="py-2 text-sm text-neutral-400">to</span>
                <select className="rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>34</option><option>44</option><option>54</option><option>65+</option>
                </select>
              </div>
            </FormField>
          </div>
        )}

        {/* Step 5: Team Members */}
        {step === 4 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Team Members</h2>
            <p className="text-sm text-neutral-500">Invite team members to help manage your advertising account.</p>
            <FormField label="Invite by Email">
              <div className="flex gap-2">
                <input placeholder="colleague@company.com" className="flex-1 rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
                <Button variant="secondary">Invite</Button>
              </div>
            </FormField>
            <div className="rounded-lg border border-neutral-100 p-4 text-sm text-neutral-500">
              You are the account owner. You can add more team members later from Account Settings.
            </div>
          </div>
        )}

        {/* Step 6: Review */}
        {step === 5 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Review Setup</h2>
            <div className="space-y-3 rounded-lg border border-neutral-100 p-4">
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Business:</span><span className="font-medium text-neutral-900">{businessName || "—"}</span></div>
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Industry:</span><span className="font-medium text-neutral-900">{industry || "—"}</span></div>
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Account Type:</span><span className="font-medium text-neutral-900 capitalize">{accountType}</span></div>
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Payment:</span><span className="font-medium text-neutral-900">{paymentMethod.replace("-", " ")}</span></div>
            </div>
          </div>
        )}
      </div>

      <div className="mt-6 flex items-center justify-between">
        <Button variant="ghost" onClick={() => setStep(Math.max(0, step - 1))} disabled={step === 0}>Back</Button>
        {step < STEPS.length - 1 ? (
          <Button onClick={() => setStep(Math.min(STEPS.length - 1, step + 1))}>Continue</Button>
        ) : (
          <Button onClick={() => window.location.href = "/ads/dashboard"}>Complete Setup</Button>
        )}
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# 27-29. /ads/account/settings, customer-review, audience-controls
# ═══════════════════════════════════════════════════════════════════════════
write_page("account/settings", '''"use client";

import { PageHeader, FormField, Button } from "@/components/ads/ui";

export default function AccountSettingsPage() {
  return (
    <div className="mx-auto max-w-4xl p-6">
      <PageHeader
        title="Account Settings"
        description="Configure your advertising account preferences and defaults."
        breadcrumbs={[{ label: "Account", href: "/ads/account" }, { label: "Settings" }]}
      />
      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">General Settings</h3>
          <div className="space-y-4">
            <FormField label="Account Name">
              <input defaultValue="My Ad Account" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
            </FormField>
            <FormField label="Time Zone">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>US/Eastern (ET)</option><option>US/Central (CT)</option><option>US/Mountain (MT)</option><option>US/Pacific (PT)</option><option>UTC</option>
              </select>
            </FormField>
            <FormField label="Currency">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>USD — US Dollar</option><option>EUR — Euro</option><option>GBP — British Pound</option><option>CAD — Canadian Dollar</option>
              </select>
            </FormField>
          </div>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Ad Defaults</h3>
          <div className="space-y-4">
            <FormField label="Default Bid Strategy">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>Automatic — Maximize results</option><option>Manual CPM</option><option>Target CPA</option>
              </select>
            </FormField>
            <FormField label="Default Placement">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>Automatic placements</option><option>Audio only</option><option>Video only</option><option>Editorial</option>
              </select>
            </FormField>
          </div>
        </div>
        <Button>Save Settings</Button>
      </div>
    </div>
  );
}
''')

write_page("account/customer-review", '''"use client";

import { PageHeader, DataTable, StatusBadge, Button, MetricCard } from "@/components/ads/ui";

const reviews = [
  { id: "cr1", campaign: "Summer Launch 2025", ad: "Summer Anthem — Audio", status: "approved" as const, reviewer: "Policy Team", date: "Mar 20, 2025", notes: "All checks passed" },
  { id: "cr2", campaign: "Brand Awareness Q2", ad: "Brand Story — Video", status: "in_review" as const, reviewer: "Policy Team", date: "Mar 22, 2025", notes: "Under review" },
  { id: "cr3", campaign: "Lead Gen - Newsletter", ad: "Sign Up Form", status: "rejected" as const, reviewer: "Policy Team", date: "Mar 18, 2025", notes: "Misleading claims in headline" },
];

const columns = [
  { key: "campaign", label: "Campaign" },
  { key: "ad", label: "Ad" },
  { key: "status", label: "Status", render: (_: any, row: any) => <StatusBadge status={row.status === "approved" ? "active" : row.status} /> },
  { key: "reviewer", label: "Reviewer" },
  { key: "date", label: "Date" },
  { key: "notes", label: "Notes" },
];

export default function CustomerReviewPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Customer Review"
        description="Track the review status of your ads through our policy and quality review process."
        breadcrumbs={[{ label: "Account", href: "/ads/account" }, { label: "Customer Review" }]}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Approved" value="1" delta="ad" deltaType="neutral" />
        <MetricCard label="In Review" value="1" delta="ad" deltaType="neutral" />
        <MetricCard label="Rejected" value="1" delta="ad" deltaType="negative" />
      </div>
      <DataTable columns={columns} data={reviews} />
    </div>
  );
}
''')

write_page("account/audience-controls", '''"use client";

import { PageHeader, MetricCard, Button, FormField } from "@/components/ads/ui";

export default function AudienceControlsPage() {
  return (
    <div className="mx-auto max-w-7xl p-6">
      <PageHeader
        title="Audience Controls"
        description="Manage account-level audience restrictions, exclusions, and privacy controls."
        breadcrumbs={[{ label: "Account", href: "/ads/account" }, { label: "Audience Controls" }]}
      />
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <MetricCard label="Excluded Segments" value="3" delta="active exclusions" deltaType="neutral" />
        <MetricCard label="Restricted Categories" value="2" delta="age-restricted" deltaType="neutral" />
        <MetricCard label="Custom Exclusions" value="1.2M" delta="users excluded" deltaType="neutral" />
      </div>
      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Account-Level Exclusions</h3>
          <div className="space-y-3">
            {[
              { label: "Exclude existing customers", desc: "Don\\'t show ads to users who have already purchased", enabled: true },
              { label: "Exclude app users", desc: "Don\\'t retarget users who already have your app installed", enabled: false },
              { label: "Age restriction: 18+", desc: "All campaigns restricted to users 18 and older", enabled: true },
            ].map((item) => (
              <div key={item.label} className="flex items-center justify-between rounded-lg border border-neutral-50 px-4 py-3">
                <div>
                  <p className="text-sm font-medium text-neutral-900">{item.label}</p>
                  <p className="text-xs text-neutral-500">{item.desc}</p>
                </div>
                <button className={`relative inline-flex h-5 w-9 shrink-0 rounded-full border-2 border-transparent transition-colors ${item.enabled ? "bg-emerald-500" : "bg-neutral-200"}`}>
                  <span className={`pointer-events-none inline-block h-4 w-4 rounded-full bg-white shadow transition-transform ${item.enabled ? "translate-x-4" : "translate-x-0"}`} />
                </button>
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-3">Upload Exclusion List</h3>
          <FormField label="Upload a list of user IDs or emails to exclude from all campaigns">
            <div className="rounded-lg border border-dashed border-neutral-300 p-6 text-center text-sm text-neutral-400">
              Drag & drop CSV file or click to browse
            </div>
          </FormField>
          <Button className="mt-3">Upload List</Button>
        </div>
      </div>
    </div>
  );
}
''')

# ═══════════════════════════════════════════════════════════════════════════
# Print summary
# ═══════════════════════════════════════════════════════════════════════════
print(f"\n✅ Pages created: {created}")
print(f"⏭️  Pages skipped (already exist): {skipped}")
if errors:
    print(f"❌ Errors: {len(errors)}")
    for e in errors:
        print(f"  - {e}")
else:
    print("✅ No errors")
